from .db import db, environment, SCHEMA, add_prefix_for_prod


class UserPokemon(db.Model):
    __tablename__ = 'user_pokemon'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('pokemons.id')), nullable=False)
    nickname = db.Column(db.String(100), nullable=True)
    level = db.Column(db.Integer, nullable=True, default=1)
    custom_moves = db.Column(db.JSON, nullable=True)
    selected_party = db.Column(db.Boolean, nullable=True, default=False)

    user = db.relationship(
        add_prefix_for_prod('User'),
        back_populates='pokemon_collection'
    )
    
    pokemon = db.relationship(
        add_prefix_for_prod('Pokemon'),
        back_populates='user_instances'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'pokemon_id': self.pokemon_id,
            'nickname': self.nickname,
            'level': self.level,
            'custom_moves': self.custom_moves,
            'selected_party': self.selected_party,
            'pokemon': self.pokemon.to_dict()
        }
