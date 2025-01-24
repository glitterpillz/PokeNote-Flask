from flask import Blueprint, jsonify, request
from app.models import User, Message, db
from flask_login import current_user, login_required

message_routes = Blueprint('messages', __name__)


# SEND A DIRECT MESSAGE
@message_routes.route('/send', methods=['POST'])
@login_required
def send_message():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request. JSON data is required.'}), 400

        receiver_username = data.get('receiver')
        content = data.get('content')

        if not receiver_username or not content:
            return jsonify({'error': 'Receiver username and content are required.'}), 400

        receiver = User.query.filter_by(username=receiver_username).first()
        if not receiver:
            return jsonify({'error': f'User with username "{receiver_username}" not found.'}), 404

        message = Message(
            sender_id=current_user.id,
            receiver_id=receiver.id,
            content=content
        )

        db.session.add(message)
        db.session.commit()

        return jsonify({'message': 'Message sent successfully.', 'sent_message': message.to_dict()}), 201

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# DELETE MESSAGE FROM INBOX
@message_routes.route('/inbox/<int:message_id>', methods=['DELETE'])
@login_required
def delete_inbox_message(message_id):
    try:
        message = Message.query.get(message_id)

        if not message:
            return jsonify({'error': 'Message not found'}), 404

        if message.receiver_id != current_user.id:
            return jsonify({'error': 'Unauthorized'}), 403
        
        message.is_deleted_by_receiver = True
        db.session.commit()

        return jsonify({'message': 'Message deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

                             
# DELETE MESSAGE FROM SENT BOX
@message_routes.route('/sent/<int:message_id>', methods=['DELETE'])
@login_required
def delete_sent_message(message_id):
    try:
        message = Message.query.get(message_id)

        if not message:
            return jsonify({'error': 'Message not found'}), 404

        if message.sender_id != current_user.id:
            return jsonify({'error': 'Unauthorized'}), 403

        message.is_deleted_by_sender = True
        db.session.commit()

        return jsonify({'message': 'Message deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# GET USER INBOX
@message_routes.route('/inbox')
@login_required
def get_inbox():
    inbox = Message.query.filter(
        Message.receiver_id == current_user.id,
        Message.sender_id != current_user.id,
        Message.is_deleted_by_receiver == False
    ).all()

    if inbox:
        return jsonify([message.to_dict() for message in inbox])
    else:
        return jsonify({'error': f'No messages found for User {current_user.id}.'}), 404
    

# GET USER SENT BOX
# @message_routes.route('/sent')
# @login_required
@message_routes.route('/sent')
@login_required
def get_sent_box():
    sent_box = Message.query.filter(
        Message.sender_id == current_user.id,
        Message.is_deleted_by_sender == False,
        Message.receiver_id != current_user.id
    ).all()

    if sent_box:
        return jsonify([message.to_dict() for message in sent_box])
    else:
        return jsonify({'error': f'No sent messages found for User {current_user.id}.'}), 404

# def get_sent_box():
#     sent_box = Message.query.filter(
#         Message.sender_id == current_user.id,
#         Message.receiver_id != current_user.id,
#         Message.is_deleted_by_sender == False
#     ).all()

#     if sent_box:
#         return jsonify([message.to_dict() for message in sent_box])
#     else:
        # return jsonify({'error': f'No messages found for User {current_user.id}.'}), 404
      

# GET DELETED MESSAGES
@message_routes.route('/deleted')
@login_required
def get_deleted_messages():
    deleted_box = Message.query.filter(
        (
            (Message.receiver_id == current_user.id) & (Message.is_deleted_by_receiver == True)
        ) | (
            (Message.sender_id == current_user.id) & (Message.is_deleted_by_sender == True)
        )
    ).all()

    if deleted_box:
        return jsonify([message.to_dict() for message in deleted_box])
    else:
        return jsonify({'error': f'No messages found'}), 404


# CLEANUP DELETED MESSAGES
@message_routes.route('/deleted', methods=['DELETE'])
@login_required
def cleanup_deleted_messages():
    try:
        messages_to_delete = Message.query.filter(
            (
                (Message.receiver_id == current_user.id) & (Message.is_deleted_by_receiver == True)
            ) | (
                (Message.sender_id == current_user.id) & (Message.is_deleted_by_sender == True)
            )
        ).all()

        if not messages_to_delete:
            return jsonify({'message': 'No messages to delete'}), 200

        for message in messages_to_delete:
            db.session.delete(message)

        db.session.commit()

        return jsonify({'message': f'{len(messages_to_delete)} messages permanently deleted'}), 200

    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500