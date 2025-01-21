from flask import Blueprint, request, jsonify
from datetime import datetime
from app.models import db, JournalEntry, Like
from app.forms import JournalEntryForm
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
import boto3
import uuid
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.environ.get('AWS_BUCKET_NAME')
S3_REGION = os.environ.get('AWS_BUCKET_REGION')
S3_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
S3_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

s3_client = boto3.client(
    's3',
    region_name=S3_REGION,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)

def upload_to_s3(file, bucket_name, folder='uploads'):
    try:
        filename = secure_filename(file.filename)
        unique_filename = f"{folder}/{uuid.uuid4().hex}_{filename}"

        s3_client.upload_fileobj(
            file,
            bucket_name,
            unique_filename,
            ExtraArgs={'ContentType': file.content_type}
        )

        return f"https://{bucket_name}.s3.{S3_REGION}.amazonaws.com/{unique_filename}"

    except Exception as e:
        raise ValueError(f"Failed to upload to S3: {e}")



journal_routes = Blueprint('journal', __name__)


# POST JOURNAL ENTRY
@journal_routes.route('/post', methods=['POST'])
@login_required
def create_journal_entry():
    form = JournalEntryForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        timestamp = form.timestamp.data if form.timestamp.data else datetime.utcnow()

        journal_entry = JournalEntry(
            user_id=current_user.id,
            title=form.title.data,
            content=form.content.data,
            accomplishments=form.accomplishments.data,
            is_private=form.is_private.data,
            timestamp=timestamp,
        )

        if 'photo' in request.files:
            file = request.files['photo']
            if file and file.filename:
                try:
                    photo = upload_to_s3(file, S3_BUCKET, folder='journal_photos')
                    journal_entry.photo = photo
                except ValueError as e:
                    return jsonify({'message': f"Photo upload failed: {str(e)}"}), 400

        try:
            db.session.add(journal_entry)
            db.session.commit()
        except Exception as db_error:
            db.session.rollback()
            return jsonify({'error': 'Failed to create journal entry', 'details': str(db_error)}), 500

        return jsonify(journal_entry.to_dict()), 201

    return jsonify({'errors': form.errors}), 400


# GET JOURNAL ENTRY
@journal_routes.route('/<int:id>')
def get_journal_entry(id):
    journal_entry = JournalEntry.query.get(id)

    if not journal_entry:
        return jsonify({'error': 'Journal entry not found'}), 404
    
    return jsonify(journal_entry.to_dict())


# EDIT JOURNAL ENTRY
@journal_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_entry(id):
    journal_entry = JournalEntry.query.get(id)

    if not journal_entry:
        return jsonify({'error': 'Journal entry not found'}), 404

    if journal_entry.user_id != current_user.id:
        return jsonify({'error': 'You can only edit your own journal entries'}), 403

    data = request.form
    title = data.get('title', journal_entry.title)
    content = data.get('content', journal_entry.content)
    accomplishments = data.get('accomplishments', journal_entry.accomplishments)
    is_private = data.get('is_private', journal_entry.is_private) == 'true'
    timestamp = data.get('timestamp', journal_entry.timestamp)

    if timestamp and isinstance(timestamp, str):
        try:
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    journal_entry.title = title
    journal_entry.content = content
    journal_entry.accomplishments = accomplishments
    journal_entry.is_private = is_private
    journal_entry.timestamp = timestamp

    if 'photo' in request.files:
        file = request.files['photo']
        if file and file.filename:
            try:
                photo_url = upload_to_s3(file, S3_BUCKET, folder='journal_photos')
                journal_entry.photo = photo_url
            except ValueError as e:
                return jsonify({'error': f"Photo upload failed: {str(e)}"}), 400

    try:
        db.session.commit()
    except Exception as db_error:
        db.session.rollback()
        return jsonify({'error': 'Failed to update journal entry', 'details': str(db_error)}), 500

    return jsonify({'message': 'Journal entry updated successfully', 'journal_entry': journal_entry.to_dict()})


# DELETE JOURNAL ENTRY
@journal_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_journal_entry(id):
    journal_entry = JournalEntry.query.get(id)

    if not journal_entry:
        return jsonify({'error': 'Journal entry not found'}), 404
    
    if not current_user.admin and journal_entry.user_id != current_user.id:
        return jsonify({'error': 'You can only view your own journal entries'}), 403

    db.session.delete(journal_entry)
    db.session.commit()

    return jsonify({'message': 'Journal entry successfully deleted'}), 200


# GET ALL PUBLIC JOURNAL ENTRIES
@journal_routes.route('/', methods=['GET'])
def get_all_journal_entries():
    journal_entries = JournalEntry.query.filter_by(is_private=False).all()

    if not journal_entries:
        return jsonify({'error': 'No journal entries found'}), 404
    
    return jsonify([entry.to_dict() for entry in journal_entries])


# GET ALL USER JOURNAL ENTRIES
@journal_routes.route('/user', methods=['GET'])
def get_user_journal():
    if not current_user.is_authenticated:
        return jsonify({'message': 'User not authenticated'}), 401

    journal = JournalEntry.query.filter(JournalEntry.user_id == current_user.id).all()
    journal_dict = [journal_entry.to_dict() for journal_entry in journal]
    return jsonify({"Journal": journal_dict})


# LIKE A JOURNAL ENTRY
@journal_routes.route('/<int:id>/like', methods=['POST'])
@login_required
def like_journal_entry(id):
    journal_entry = JournalEntry.query.get(id)

    if not journal_entry:
        return jsonify({'error': 'Journal entry not found'}), 404
    
    existing_like = Like.query.filter_by(user_id=current_user.id, journal_entry_id=id).first()

    if existing_like:
        return jsonify({'error': 'You have already liked this entry'}), 400
    
    like = Like(user_id=current_user.id, journal_entry_id=id)
    db.session.add(like)
    db.session.commit()

    return jsonify({'message': 'Journal entry liked successfully', 'like': like.to_dict()}), 201


# UNLIKE A JOURNAL ENTRY
@journal_routes.route('/<int:journal_entry_id>/like', methods=['DELETE'])
@login_required
def unlike_journal_entry(journal_entry_id):
    like = Like.query.filter_by(user_id=current_user.id, journal_entry_id=journal_entry_id).first()

    if not like:
        return jsonify({'error': 'Like not found or already removed'}), 404

    db.session.delete(like)
    db.session.commit()

    return jsonify({'message': 'Like removed successfully'})
