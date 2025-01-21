from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Comment, JournalEntry

comment_routes = Blueprint('comments', __name__)


# ADD A COMMENT
@comment_routes.route('/<int:journal_id>', methods=['POST'])
@login_required
def add_comment(journal_id):
    journal_entry = JournalEntry.query.get(journal_id)

    if not journal_entry:
        return jsonify({'error': 'Journal entry not found'}), 404
    
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content is required for the comment'}), 400
    
    comment = Comment(
        content=content,
        user_id=current_user.id,
        journal_entry_id=journal_id
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify(comment.to_dict()), 201


# GET COMMENTS OF A JOURNAL ENTRY
@comment_routes.route('/<int:journal_id>')
@login_required
def get_entry_comments(journal_id):
    journal_entry = JournalEntry.query.get(journal_id)

    if not journal_entry:
        return jsonify({'error': 'Journal entry not found'}), 404

    comments = Comment.query.filter_by(journal_entry_id=journal_id).all()

    if not comments:
        return jsonify({'error': 'No comments found for this journal entry'}), 404
    
    return jsonify([comment.to_dict() for comment in comments]), 200


# EDIT COMMENT
@comment_routes.route('/<int:comment_id>', methods=['PUT'])
@login_required
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({'error': 'Comment not found'}), 404
    
    if comment.user_id != current_user.id:
        return jsonify({'error': 'You can only edit your own comments'}), 403
    
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content in required'}), 400
    
    comment.content = content
    db.session.commit()

    return jsonify({'message': 'Comment updated successfully', 'comment': comment.to_dict()}), 200


# DELETE COMMENT
@comment_routes.route('/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({'error': 'Comment not found'}), 404
    
    if comment.user_id != current_user.id:
        return jsonify({'error': 'You can only delete your own comments'}), 403
    
    db.session.delete(comment)
    db.session.commit()

    return jsonify({'message': 'Comment deleted successfully'}), 200
