import os
import boto3
import uuid
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
from flask import Blueprint,jsonify, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from app.forms import UpdateAccountForm
from flask_login import current_user, login_user, logout_user, login_required

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

def upload_to_s3(file, bucket_name, folder='images'):
    try:
        filename = secure_filename(file.filename)
        unique_filename = f"{folder}/{uuid.uuid4().hex}_{filename}"

        try:
            s3_client.upload_fileobj(
                file,
                bucket_name,
                unique_filename,
                ExtraArgs={'ContentType': file.content_type}
            )
        except Exception as s3_error:
            print(f"S3 upload error: {str(s3_error)}")
            raise

        file_url = f"https://{bucket_name}.s3.{S3_REGION}.amazonaws.com/{unique_filename}"
        return file_url
    except Exception as e:
        raise ValueError(f"Issue uploading file: {e}")



auth_routes = Blueprint('auth', __name__)


# AUTHENTICATE USER
@auth_routes.route('/session')
def authenticate():
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict())
    return {'errors': {'message': 'Unauthorized'}}, 401


# LOGIN
@auth_routes.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.data['email']).first()

        if user:
            if user.disabled:
                return {'error': 'This account has been disabled. Please contact support.'}, 403

            if not check_password_hash(user.password, form.data['password']):
                return {'errors': {'password': 'Invalid password'}}, 401

            login_user(user)
            return user.to_dict()

    return {"errors": form.errors or {"general": "Invalid credentials"}}, 401


# LOGOUT
@auth_routes.route('/logout')
def logout():
    logout_user()
    return {'message': 'User logged out'}


# SIGNUP
@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password'],
            fname=form.data['fname'],
            lname=form.data['lname'],
            admin=form.data['admin'],
        )

        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and file.filename:
                try:
                    profile_picture_url = upload_to_s3(file, S3_BUCKET)
                    user.profile_picture = profile_picture_url
                except ValueError as e:
                    return jsonify({'message': str(e)}), 400
                

        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


# RETURNS UNAUTHORIZED RESPONSE
@auth_routes.route('/unauthorized')
def unauthorized():
    return {'errors': {'message': 'Unauthorized'}}, 401


# GET USER ACCOUNT
@auth_routes.route('/account')
@login_required
def get_account():
    user = User.query.get(current_user.id)
    if not user:
        return {'error': 'User not found'}, 404
    
    return jsonify(user.to_dict())


# EDIT USER ACCOUNT
@auth_routes.route('/account/<int:id>', methods=['PUT'])
@login_required
def update_account(id):
    if id != current_user.id:
        return {'error': 'Unauthorized'}, 403

    form = UpdateAccountForm()
    form.current_user_id = current_user.id
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        user = User.query.get(id)
        if not user:
            return {'error': 'User not found'}, 404

        if form.username.data:
            user.username = form.username.data

        if form.email.data:
            user.email = form.email.data

        user.fname = form.fname.data or user.fname
        user.lname = form.lname.data or user.lname

        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and file.filename:
                try:
                    profile_picture_url = upload_to_s3(file, S3_BUCKET, folder='profile_pictures')
                    user.profile_picture = profile_picture_url
                except ValueError as e:
                    return jsonify({'message': f"Profile picture upload failed: {str(e)}"}), 400

        if 'banner_url' in request.files:
            file = request.files['banner_url']
            if file and file.filename:
                try:
                    banner_url = upload_to_s3(file, S3_BUCKET, folder='banners')
                    user.banner_url = banner_url
                except ValueError as e:
                    return jsonify({'message': f"Banner upload failed: {str(e)}"}), 400

        try:
            db.session.commit()
        except Exception as db_error:
            db.session.rollback()
            return {'error': 'Failed to update account', 'details': str(db_error)}, 500

        return user.to_dict()

    return {'errors': form.errors}, 400


# DELETE USER ACCOUNT
@auth_routes.route('/account', methods=['DELETE'])
@login_required
def delete_account(user_id=None):
    if user_id is None:
        user = User.query.get(current_user.id)
    else:
        if not current_user.admin:
            return {'error': 'Unauthorized. Admin privileges required.'}, 403
        user = User.query.get(user_id)
    
    if not user:
        return {'error': 'User not found'}, 404

    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to delete account', 'details': str(e)}, 400

    if user.id == current_user.id:
        logout_user()
        return jsonify({'message': 'Your account has been deleted successfully.'})

    return jsonify({'message': f"User account with ID {user.id} has been deleted successfully."})
