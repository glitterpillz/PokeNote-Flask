import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { restoreUser } from "../../redux/session";
import { fetchPokemonDetail, deleteUserPokemon } from "../../redux/pokemon";
import { useModal } from '../../context/Modal';
import EditPokemonModal from "./EditPokemonModal";
import dets from './UserPokemonDetails.module.css'
import Navigation from "../Navigation";

function UserPokemonDetails() {
    const { id } = useParams();
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { setModalContent } = useModal();
    const pokemons = useSelector((state) => state.pokemon);
    const currentUser = useSelector((state) => state.session.user);

    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        if (!currentUser) {
            dispatch(restoreUser());
        }
    }, [dispatch, currentUser]);

    useEffect(() => {
        if (currentUser) {
            setIsLoading(true);
            dispatch(fetchPokemonDetail(id)).finally(() => {
                setIsLoading(false);
            });
        }
    }, [dispatch, currentUser, id]);

    const handleEditPokemon = (pokemon) => {
        setModalContent(
            <EditPokemonModal 
                pokemon={pokemon} 
                closeModal={() => setModalContent(null)} 
            />
        );
    };
    
    const handleDeletePokemon = async (pokemonId) => {
        const isConfirmed = window.confirm('Are you sure you want to remove this Pokémon from your collection?');
    
        if (isConfirmed) {
            try {
                const result = await dispatch(deleteUserPokemon(pokemonId)).unwrap();
                alert(result.message || "Pokémon deleted successfully!");
                navigate("/pokemon/collection");
            } catch (error) {
                console.error("Error deleting Pokémon:", error);
                alert(
                    typeof error === 'string'
                        ? error
                        : "Failed to delete Pokémon. Please try again."
                );
            }
        } else {
            return;
        }
    };
        
    const pokemonList = pokemons.pokemons ? Object.values(pokemons.pokemons) : [];

    const typeColors = {
        Fire: '#f89055',
        Water: '#469ae4',
        Grass: '#30d884',
        Electric: '#fdd75a',
        Psychic: '#f165ef',
        Ice: '#98D8D8',
        Dragon: '#9269f1',
        Dark: '#604667',
        Fairy: '#ee99c6',
        Normal: '#89a6a9',
        Poison: '#c677cf',
        Flying: '#a9c4ec',
        Bug: '#91e0b0',
        Ground: '#9c7979',
        Rock: '#ababaf',
    };

    if (isLoading) {
        return <p className={dets.loading}>Loading Pokémon details...</p>;
    }

    return (
        <div className={dets.mainContainer}>
            <div className={dets.navbar}>
                <Navigation />
            </div>
            {pokemonList.length === 0 ? (
                <p className={dets.errors}>No Pokémon found.</p>
            ) : (
                pokemonList.map((pokemonDetail) => (
                    <div key={pokemonDetail.id} className={dets.detailsContainer}>
                        <div className={dets.imageBox}>
                            <img
                                className={`${dets.image} ${pokemonDetail.pokemon?.can_fly ? dets.canFly : ""}`}
                                src={pokemonDetail.pokemon?.image || "placeholder-image-url"}
                                alt={pokemonDetail.pokemon?.name || "Unknown Pokémon"}
                            />
                        </div>
                        <div className={dets.headerContainer}>
                            <div className={dets.h1Div}>
                                <img className={dets.pokeball} src="/images/pokeball.png" alt="" />
                                <h1 className={dets.h1}>{pokemonDetail.pokemon.name}</h1>
                                <img className={dets.pokeball} src="/images/pokeball-right.png" alt="" />
                            </div>
                            <div className={dets.typesContainer}>
                                {pokemonDetail.pokemon?.types.map((type, index) => (
                                    <div
                                        key={index}
                                        className={dets.pokemonType}
                                        style={{ backgroundColor: typeColors[type] || '#ccc' }}
                                    >
                                        {type}
                                    </div>
                                ))}
                            </div>
                        </div>
                        <div className={dets.bioContainer}>
                            <div className={dets.bioBox}>
                                <label>Nickname:</label>
                                <p>{pokemonDetail.nickname}</p>
                            </div>
                            <div className={dets.bioBox}>
                                <label>Level:</label>
                                <p>{pokemonDetail.level}</p>
                            </div>
                        </div>
                        <hr className={dets.hr}/>
                        <div className={dets.infoContainer}>
                            <div className={dets.statsContainer}>
                                <div className={dets.labelDiv}>
                                    <label>Stats:</label>
                                </div>
                                {pokemonDetail.pokemon?.stats.map((stat, index) => (
                                    <div key={index} className={dets.statBox}>
                                        <div className={dets.statName}>
                                            {stat.stat_name}
                                        </div>
                                        <div className={dets.statValue}>
                                            {stat.stat_value}
                                        </div>
                                    </div>
                                ))}                                        
                            </div>
                            <div className={dets.movesContainer}>
                                <div className={dets.labelDiv}>
                                    <label>Moves:</label>
                                </div>
                                {pokemonDetail.custom_moves ? (
                                    Object.values(pokemonDetail.custom_moves).map((move, index) => (
                                        <p key={index}>{move || "N/A"}</p>
                                    ))
                                ) : (
                                    <p>No moves available</p>
                                )}
                            </div>
                        </div>
                        <div className={dets.buttonsContainer}>
                            <button 
                                onClick={() => handleEditPokemon(pokemonDetail)}
                                className={dets.button}
                            >
                                Edit
                            </button>
                            <button 
                                onClick={() => handleDeletePokemon(pokemonDetail.id)}
                                className={dets.button}
                            >
                                Remove
                            </button>
                        </div>
                    </div>
                ))
            )}
        </div>
    );
}

export default UserPokemonDetails;

