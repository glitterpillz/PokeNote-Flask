from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app.models import db, Pokemon, PokemonStat, UserPokemon, User


pokemon_routes = Blueprint('pokemon', __name__)


# GET ALL POKEMON:
@pokemon_routes.route('/')
def pokemons():
    pokemons = Pokemon.query.filter(
        Pokemon.id.in_(
            [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
                51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                71, 72
            ]
    )).order_by(Pokemon.id).all()

    return jsonify({"Pokemon": [pokemon.to_dict() for pokemon in pokemons]})


# GET POKEMON BY ID:
@pokemon_routes.route('/<int:id>')
def get_pokemon_by_id(id):
    pokemon = Pokemon.query.get(id)

    if pokemon:
        return jsonify(pokemon.to_dict())
    
    return jsonify({'message': 'Pokemon not found'}), 404


# ADD POKEMON TO USER:
@pokemon_routes.route('/<int:id>', methods=['POST'])
@login_required
def add_pokemon_to_user(id):
    pokemon = Pokemon.query.get(id)

    if not pokemon:
        return jsonify({'error': 'Pokemon not found'}), 404
    
    new_entry = UserPokemon(
        user_id=current_user.id,
        pokemon_id=pokemon.id,
        selected_party=False,
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'message': 'Pokemon added to your collection'}), 201


# SEARCH POKEMON:
@pokemon_routes.route('/search', methods=['GET'])
def search_pokemon():
    search_query = request.args.get('query', '').strip()

    if not search_query:
        return {'error': 'Search query cannot be empty'}, 400
    
    if search_query.isdigit():
        pokemon = Pokemon.query.filter(Pokemon.id == int(search_query)).first()
        if not pokemon:
            return {'error': 'Pokemon not found'}, 404
        return jsonify({"Pokemon": [pokemon.to_dict()]})
    
    pokemons = Pokemon.query.filter(Pokemon.name.like(f"%{search_query}%")).all()
    
    if not pokemons:
        return {'error': 'No Pokémon found'}, 404
    
    return jsonify({"Pokemon": [pokemon.to_dict() for pokemon in pokemons]})


# GET USER POKEMON COLLECTION:
@pokemon_routes.route('/collection', methods=['GET'])
def get_user_pokemons():
    if not current_user.is_authenticated:
        return jsonify({'message': 'User not authenticated'})
    
    pokemons = UserPokemon.query.filter(UserPokemon.user_id == current_user.id).all()
    pokemons_dict = [pokemon.to_dict() for pokemon in pokemons]
    return jsonify({"Pokemon": pokemons_dict})


# GET USER POKEMON PARTY:
@pokemon_routes.route('/party', methods=['GET'])
def get_user_party():
    if not current_user.is_authenticated:
        return jsonify({'message': 'User not authenticated'})
    
    pokemons = UserPokemon.query.filter(
        UserPokemon.user_id == current_user.id,
        UserPokemon.selected_party == True
    ).all()
    pokemons_dict = [pokemon.to_dict() for pokemon in pokemons]
    return jsonify({"Pokemon": pokemons_dict})


# GET USER POKEMON DETAILS:
@pokemon_routes.route('/collection/<int:collection_id>', methods=['GET'])
def get_user_pokemon_by_collection_id(collection_id):
    user_pokemon = UserPokemon.query.get(collection_id)
    if not user_pokemon:
        return jsonify({'error': 'Pokemon not found in your collection'}), 404
    return jsonify({'pokemon': user_pokemon.to_dict()})


# EDIT USER POKEMON:
@pokemon_routes.route('/collection/<int:collection_id>', methods=['PUT'])
@login_required
def edit_user_pokemon(collection_id):
    """
    Edit a Pokémon in the user's collection, including optional updates to stats and custom moves.
    """
    user_pokemon = UserPokemon.query.filter_by(id=collection_id, user_id=current_user.id).first()

    if not user_pokemon:
        return {'error': 'Pokémon not found in your collection'}, 404

    pokemon = Pokemon.query.get(user_pokemon.pokemon_id)
    if not pokemon:
        return {'error': 'Pokémon data not found'}, 404

    data = request.get_json()

    user_pokemon.nickname = data.get('nickname', user_pokemon.nickname)
    user_pokemon.level = data.get('level', user_pokemon.level)
    selected_party = data.get('selected_party', None)
    if selected_party is not None:
        if isinstance(selected_party, str): 
            user_pokemon.selected_party = selected_party.lower() == 'true'
        else: 
            user_pokemon.selected_party = bool(selected_party)


    update_stats(user_pokemon, data.get('stats', []))

    update_custom_moves(user_pokemon, data.get('custom_moves', []))

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update Pokémon', 'details': str(e)}), 400

    return jsonify({'message': 'Pokémon updated successfully', 'pokemon': user_pokemon.to_dict()})

def update_stats(user_pokemon, stats_data):
    """
    Update the stats for a specific Pokémon in the user's collection.
    """
    for stat_data in stats_data:
        stat_name = stat_data.get('stat_name')
        stat_value = stat_data.get('stat_value')
        if stat_name and stat_value is not None:
            stat = PokemonStat.query.filter_by(pokemon_id=user_pokemon.pokemon_id, stat_name=stat_name).first()

            if stat:
                stat.stat_value = stat_value
            else:
                new_stat = PokemonStat(
                    pokemon_id=user_pokemon.pokemon_id,
                    stat_name=stat_name,
                    stat_value=stat_value
                )
                db.session.add(new_stat)

def update_custom_moves(user_pokemon, custom_moves):
    """
    Update or add the custom moves for the user's Pokémon.
    """
    if custom_moves is not None:
        user_pokemon.custom_moves = custom_moves


# DELETE USER POKEMON
@pokemon_routes.route('/collection/<int:collection_id>', methods=['DELETE'])
@login_required
def delete_user_pokemon(collection_id):
    user_pokemon = UserPokemon.query.filter_by(id=collection_id, user_id=current_user.id).first()

    if not user_pokemon:
        return jsonify({'error': 'Pokémon not found in your collection'}), 404
    
    try:
        db.session.delete(user_pokemon)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete Pokémon', 'details': str(e)}), 400
    
    return jsonify({'message': 'Pokémon successfully removed from your collection'}), 200
