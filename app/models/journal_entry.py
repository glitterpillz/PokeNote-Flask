from .db import db, environment, SCHEMA, add_prefix_for_prod

class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    accomplishments = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=None)
    photo = db.Column(db.String(255), nullable=True)
    is_private = db.Column(db.Boolean, nullable=True, default=False)

    user = db.relationship(
        add_prefix_for_prod('User'),
        back_populates='journal_entries'
    )

    comments = db.relationship(
        add_prefix_for_prod('Comment'),
        back_populates='journal_entry',
        cascade='all, delete-orphan'
    )

    likes = db.relationship(
        add_prefix_for_prod('Like'),
        back_populates='journal_entry',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        formatted_timestamp = (
            self.timestamp.strftime('%Y-%m-%d') if self.timestamp else None
        )
        return {
            'id': self.id,
            'user_id': self.user_id,
            'username': self.user.username,
            'profile_picture': self.user.profile_picture,
            'title': self.title,
            'content': self.content,
            'accomplishments': self.accomplishments,
            'timestamp': formatted_timestamp,
            'photo': self.photo,
            'is_private': self.is_private,
            'comments': [comment.to_dict() for comment in self.comments],
            'like_count': len(self.likes)
        }