from .db import db, environment, SCHEMA, add_prefix_for_prod

class Pokemon(db.Model):
    __tablename__='pokemons'

    if environment == 'production':
        __table_args__={'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    types = db.Column(db.JSON, nullable=False)
    can_fly = db.Column(db.Boolean, nullable=True)
    is_floating = db.Column(db.Boolean, nullable=True)

    image = db.Column(db.String(255), nullable=True)

    stats = db.relationship(
        add_prefix_for_prod('PokemonStat'),
        back_populates='pokemon',
        cascade='all, delete-orphan'
    )

    user_instances = db.relationship(
        add_prefix_for_prod('UserPokemon'),
        back_populates='pokemon',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'types': self.types,
            'can_fly': self.can_fly,
            'is_floating': self.is_floating,
            'image': self.image,
            'stats': [stat.to_dict() for stat in self.stats] if self.stats else []
        }
    
class PokemonStat(db.Model):
    __tablename__ = 'pokemon_stats'

    __table_args__ = {'schema': SCHEMA} if environment == 'production' else {}

    id = db.Column(db.Integer, primary_key=True)
    stat_name = db.Column(db.String(50), nullable=False)
    stat_value = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('pokemons.id')), nullable=False)

    pokemon = db.relationship('Pokemon', back_populates='stats')

    def to_dict(self):
        return {
            'stat_name': self.stat_name,
            'stat_value': self.stat_value
        }