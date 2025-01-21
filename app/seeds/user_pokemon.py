from app.models import db, UserPokemon, environment, SCHEMA
# from app.models.db import db, environment, SCHEMA
from sqlalchemy.sql import text

def seed_user_pokemon():
    user1_pokemon1 = UserPokemon(
        user_id=1,
        pokemon_id=1,
        nickname="Leafy",
        level=10,
        custom_moves={"move1": "Vine Whip", "move2": "Tackle"}
    )
    user1_pokemon2 = UserPokemon(
        user_id=1,
        pokemon_id=4,
        nickname="Flare",
        level=12,
        custom_moves={"move1": "Ember", "move2": "Scratch"}
    )

    # User 2's Pokémon
    user2_pokemon1 = UserPokemon(
        user_id=2,
        pokemon_id=7,
        nickname="Shellshock",
        level=8,
        custom_moves={"move1": "Water Gun", "move2": "Tackle"},
        selected_party=True
    )
    user2_pokemon2 = UserPokemon(
        user_id=2,
        pokemon_id=10,
        nickname="Bugsy",
        level=5,
        custom_moves={"move1": "String Shot", "move2": "Tackle"}
    )

    # User 3's Pokémon
    user3_pokemon1 = UserPokemon(
        user_id=3,
        pokemon_id=13,
        nickname="Stinger",
        level=7,
        custom_moves={"move1": "Poison Sting", "move2": "String Shot"}
    )
    user3_pokemon2 = UserPokemon(
        user_id=3,
        pokemon_id=3,
        nickname="BigLeaf",
        level=20,
        custom_moves={"move1": "Razor Leaf", "move2": "Solar Beam"}
    )

    all_user_pokemon = [
        user1_pokemon1, user1_pokemon2,
        user2_pokemon1, user2_pokemon2,
        user3_pokemon1, user3_pokemon2
    ]

    for user_pokemon in all_user_pokemon:
        db.session.add(user_pokemon)

    db.session.commit()


def undo_user_pokemon():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_pokemon RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_pokemon"))

    db.session.commit()
