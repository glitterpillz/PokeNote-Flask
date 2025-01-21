from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .message import Message

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    fname = db.Column(db.String(40), nullable=False)
    lname = db.Column(db.String(40), nullable=False)
    admin = db.Column(db.Boolean, nullable=True)
    disabled = db.Column(db.Boolean, default=False)
    profile_picture = db.Column(db.String(255), nullable=True, default="https://i.ibb.co/g61kyQY/placeholder-prof-pic.png")
    banner_url = db.Column(db.String(255), nullable=True, default="https://i.ibb.co/QKPFB1t/placeholder-banner.jpg")

    pokemon_collection = db.relationship(
        add_prefix_for_prod('UserPokemon'),
        back_populates='user',
        cascade='all, delete-orphan'
    )

    journal_entries = db.relationship(
        add_prefix_for_prod('JournalEntry'),
        back_populates='user',
        cascade='all, delete-orphan'
    )

    comments = db.relationship(
        add_prefix_for_prod('Comment'),
        back_populates='user',
        cascade='all, delete-orphan'
    )

    likes = db.relationship(
        add_prefix_for_prod('Like'),
        back_populates='user',
        cascade='all, delete-orphan'
    )

    sent_messages = db.relationship(
        add_prefix_for_prod('Message'),
        foreign_keys=[Message.sender_id],
        back_populates='sender'
    )

    received_messages = db.relationship(
        add_prefix_for_prod('Message'),
        foreign_keys=[Message.receiver_id],
        back_populates='receiver'
    )

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
        "user": {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'fname': self.fname,
            'lname': self.lname,
            'admin': self.admin,
            'disabled': self.disabled,
            'pokemon_collection': [entry.to_dict() for entry in self.pokemon_collection],
            'journal_entries': [entry.to_dict() for entry in self.journal_entries],
            'comments': [entry.to_dict() for entry in self.comments],
            'profile_picture': self.profile_picture,
            'banner_url': self.banner_url,
            'sent_messages': [msg.to_dict() for msg in self.sent_messages],
            'received_messages': [msg.to_dict() for msg in self.received_messages]
        }
    }
