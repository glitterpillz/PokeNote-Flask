import os
from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.models import db, User

user_routes = Blueprint('users', __name__)


# ADMIN - GET ALL USERS:
@user_routes.route('/all')
@login_required
def users():
    if not current_user.admin:
        return {'error': 'Unauthorized. Admin privileges required.'}, 403

    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


# ADMIN - DISABLE USER:
@user_routes.route('/<int:id>/disable', methods=['PUT'])
@login_required
def disable_user(id):
    if not current_user.admin:
        return {'error': 'Unauthorized. Admin privileges required.'}, 403
   
    user = User.query.get(id)

    if user:
        user.disabled = True
        db.session.commit()
        return jsonify({'message': 'User disabled successfully'}), 200
    return jsonify({'error': 'User not found'}), 404


# ADMIN - ENABLE USER:
@user_routes.route('/<int:id>/enable', methods=['PUT'])
@login_required
def enable_user(id):
    if not current_user.admin:
        return {'error': 'Unauthorized. Admin privileges required.'}, 403

    user = User.query.get(id)

    if user:
        user.disabled = False  
        db.session.commit()
        return jsonify({'message': 'User enabled successfully'}), 200
    return jsonify({'error': 'User not found'}), 404


# ADMIN - GET USER DETAILS
@user_routes.route('/<int:id>')
@login_required
def user(id):
    if not current_user.admin:
        return {'error': 'Unauthorized. Admin privileges required.'}, 403

    user = User.query.get(id)
    if not user:
        return {'error': 'User not found'}, 404

    return user.to_dict()


# GET USER PUBLIC PROFILE
@user_routes.route('/<int:id>/profile')
def public_profile(id):
    user = User.query.get(id)
    if not user:
        return {'error': 'User not found'}, 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'fname': user.fname,
        'lname': user.lname,
        'profile_picture': user.profile_picture,
        'banner_url': user.banner_url,
        'disabled': user.disabled,
        'pokemon_collection': [pokemon.to_dict() for pokemon in user.pokemon_collection],
        'journal_entries': [entry.to_dict() for entry in user.journal_entries]
    })
