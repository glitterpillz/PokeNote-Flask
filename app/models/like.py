from .db import db, environment, SCHEMA, add_prefix_for_prod

class Like(db.Model):
    __tablename__ = add_prefix_for_prod('likes')

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(f'{SCHEMA}.users.id' if environment == "production" else 'users.id'), nullable=False)
    journal_entry_id = db.Column(db.Integer, db.ForeignKey(f'{SCHEMA}.journal_entries.id' if environment == "production" else 'journal_entries.id'), nullable=False)

    user = db.relationship(
        'User',
        back_populates='likes'
    )

    journal_entry = db.relationship(
        'JournalEntry',
        back_populates='likes'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'journal_entry_id': self.journal_entry_id
        }