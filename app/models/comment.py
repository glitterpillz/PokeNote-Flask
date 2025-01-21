from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    journal_entry_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('journal_entries.id')), nullable=False)

    user = db.relationship(
        add_prefix_for_prod('User'),
        back_populates='comments'
    )

    journal_entry = db.relationship(
        add_prefix_for_prod('JournalEntry'), 
        back_populates='comments'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'timestamp': self.timestamp,
            'user_id': self.user_id,
            'journal_entry_id': self.journal_entry_id
        }
