from flask.cli import AppGroup
from .users import seed_users, undo_users
from .pokemons import seed_pokemon, undo_pokemon
from .journal_entries import seed_journal_entries, undo_journal_entries
from .user_pokemon import seed_user_pokemon, undo_user_pokemon

from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_journal_entries()
        undo_user_pokemon()
        undo_pokemon()
        undo_users()
    seed_users()
    seed_pokemon()
    seed_user_pokemon()
    seed_journal_entries()


@seed_commands.command('undo')
def undo():
    undo_journal_entries()
    undo_user_pokemon()
    undo_pokemon()
    undo_users()
