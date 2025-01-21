import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as sessionActions from "../../redux/session";
import * as pokemonActions from "../../redux/pokemon";
import Navigation from "../Navigation";
import { IoMdArrowRoundUp } from "react-icons/io";
import pok from "./PokedexPage.module.css";

function PokedexPage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [isLoaded, setIsLoaded] = useState(false);
    const [searchQuery, setSearchQuery] = useState("");
    const [searchResults, setSearchResults] = useState([]);
    const [scrollTopButton, setScrollTopButton] = useState(false);
    const [typingTimeout, setTypingTimeout] = useState(null);

    const { pokemons, loading, errors } = useSelector((state) => state.pokemon);

    useEffect(() => {
        dispatch(sessionActions.restoreUser()).then(() => setIsLoaded(true));
    }, [dispatch]);

    useEffect(() => {
        dispatch(pokemonActions.getAllPokemon())
    }, [dispatch])

    useEffect(() => {
        const handleScroll = () => {
            if (window.scrollY > 300) {
                setScrollTopButton(true);
            } else {
                setScrollTopButton(false);
            }
        };

        window.addEventListener("scroll", handleScroll);

        return () => {
            window.removeEventListener("scroll", handleScroll);
        };
    }, []);

    const handleSearch = (query) => {
        if (typingTimeout) {
            clearTimeout(typingTimeout);
        }

        setTypingTimeout(
            setTimeout(async () => {
                if (query.trim() === "") {
                    setSearchResults([]);
                    return;
                }

                const response = await fetch(`/api/pokemon/search?query=${query}`);
                if (response.ok) {
                    const results = await response.json();
                    setSearchResults(results.Pokemon);
                } else {
                    setSearchResults([]);
                }
            }, 300)
        );
    };

    const handleCardClick = (id) => {
        navigate(`/pokemon/${id}`);
    };

    if (loading || !isLoaded) {
        return <div className={pok.loading}>Loading...</div>;
    }

    if (errors) {
        return <div className={pok.errors}>Error: {errors}</div>;
    }

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

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    };

    const renderPokemonCards = (pokemonList) => {
        return pokemonList.map((pokemon) => (
            <div
                key={pokemon.id}
                className={pok.pokemonCard}
                onClick={() => handleCardClick(pokemon.id)}
                style={{ cursor: "pointer" }}
            >
                <img src={pokemon.image} alt={pokemon.name} />
                <h3>{pokemon.name}</h3>
                <div className={pok.typesContainer}>
                    {pokemon.types.map((type, index) => (
                        <div
                            key={index}
                            className={pok.pokemonType}
                            style={{ backgroundColor: typeColors[type] || '#ccc' }}
                        >
                            {type}
                        </div>
                    ))}
                </div>
            </div>
        ));
    };

    const upArrow = <IoMdArrowRoundUp
        className={pok.upArrow}
        style={{
            'color': '#ffd444',
            'borderRadius': '50%',
            'fontSize': '40px',
            'cursor': 'pointer'
        }}
    />

    return (
        <div className={pok.mainContainer}>
            <div className={pok.navContainer}>
                <Navigation />
                {scrollTopButton && (
                    <div
                        className={`${pok.scrollTopButton} ${scrollTopButton ? pok.show : ''}`}
                        onClick={scrollToTop}
                    >
                        {upArrow}
                    </div>
                )}
            </div>
            <img className={pok.bannerImg} src="/images/catch-em-all.png" alt="" />
            <div className={pok.searchContainer}>
                <div className={pok.searchForm}>
                    <input
                        type="text"
                        placeholder="Search Pokémon by name or ID..."
                        value={searchQuery}
                        onChange={(e) => {
                            setSearchQuery(e.target.value);
                            handleSearch(e.target.value);
                        }}
                        className={pok.searchInput}
                    />
                </div>
            </div>
            <div className={pok.resultsContainer}>
                {searchQuery.length > 0 ? (
                    searchResults.length > 0 ? (
                        renderPokemonCards(searchResults)
                    ) : (
                        <p className={pok.errors}>No Pokémon found.</p>
                    )
                ) : (
                    pokemons.length > 0 ? (
                        renderPokemonCards(pokemons)
                    ) : (
                        <p className={pok.errors}>No Pokémon to display.</p>
                    )
                )}
            </div>
        </div>
    );
}

export default PokedexPage;
