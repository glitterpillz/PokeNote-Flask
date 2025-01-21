from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from sqlalchemy.schema import MetaData

metadata = MetaData(schema="public")

class Message(db.Model):
    __tablename__ = 'messages'

    if environment == 'production':
        __table_args__ = {'schema': "public"}

    # if environment == 'production':
    #     __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_deleted_by_sender = db.Column(db.Boolean, nullable=False, default=False)
    is_deleted_by_receiver = db.Column(db.Boolean, nullable=False, default=False)

    sender = db.relationship(
        add_prefix_for_prod('User'),
        foreign_keys=[sender_id],
        back_populates='sent_messages'
    )

    receiver = db.relationship(
        add_prefix_for_prod('User'),
        foreign_keys=[receiver_id],
        back_populates='received_messages'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'profile_picture': self.sender.profile_picture,
            'content': self.content,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %I:%M %p'),            
            'sender': self.sender.username,
            'receiver': self.receiver.username,
            'is_deleted_by_sender': self.is_deleted_by_sender,
            'is_deleted_by_receiver': self.is_deleted_by_receiver
        }