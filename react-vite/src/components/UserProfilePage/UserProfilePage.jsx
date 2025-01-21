import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getUserProfile } from "../../redux/user"; 
import { getPokemonParty } from "../../redux/pokemon";
import Navigation from "../Navigation";
import pro from './UserProfilePage.module.css';
import { useParams } from "react-router-dom"; 

function UserProfilePage() {
    const dispatch = useDispatch();
    const { id } = useParams(); 
    const { userProfile, loading, errors } = useSelector((state) => state.user); 

    const { pokemons, loading: partyLoading } = useSelector((state) => state.pokemon)

    useEffect(() => {
        if (id) {
            dispatch(getUserProfile(id)); 
        }
    }, [dispatch, id]);

    useEffect(() => {
        dispatch(getPokemonParty())
    }, [dispatch])
    
    if (loading || partyLoading) { 
        return <div className={pro.loading}>Loading...</div>;
    }

    if (errors) {
        return <div className={pro.errors}>Error: {errors || "Something went wrong."}</div>;
    }

    if (!userProfile || userProfile.disabled) {
        return <div className={pro.errors}>No profile found.</div>;
    }
    
    const { banner_url, journal_entries, profile_picture, username } = userProfile;

    const pokemonParty = pokemons?.Pokemon || [];

    const recentJournalEntries = [...journal_entries]
        .filter((entry) => entry.is_private === false)
        .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
        .slice(0, 5);

    return (
        <div>
            <div className={pro.navbar}>
                <Navigation />
            </div>
            <div className={pro.profileContainer}>
                <img
                    className={pro.bannerPic}
                    src={banner_url}
                    alt=""
                />
                <div className={pro.profileBox}>
                    <div className={pro.profileHeader}>
                        <img
                            className={pro.profilePic}
                            src={profile_picture}
                            alt={`${username}'s profile`}
                        />
                        <div className={pro.usernameDiv}>
                            <button 
                                className={pro.friendButton}
                                onClick={() => window.alert("Feature coming soon!")}
                            >
                                Add Friend
                            </button>
                            <h2>{username}</h2>
                            <button
                                className={pro.messageButton}
                                onClick={() => window.alert("Feature coming soon!")}
                            >
                                Send Message
                            </button>
                        </div>
                    </div>
                    <div className={pro.profileDetails}>

                        <div className={pro.pokemonPartyHeader}>
                            <img src="/images/pokeball.png" alt="" />
                            <h3 className={pro.h3}>Pokémon Party</h3>
                            <img src="/images/pokeball-right.png" alt="" />
                        </div>
                        <div className={pro.pokemonContainer}>
                            {pokemonParty.length > 0 ? (
                            <div className={pro.pokemonBox}>
                                {pokemonParty.slice(0, 6).map((pokemon, index) => (
                                    <div 
                                    key={index} 
                                    className={pro.pokemonCard}
                                    >
                                        <div className={pro.pokemonImg}>
                                            <img 
                                                src={pokemon.pokemon.image} 
                                                alt={pokemon.pokemon.name} 
                                                className={pro.image}
                                            />
                                        </div>
                                        <div className={pro.cardBody}>
                                            <p className={pro.name}>{pokemon.pokemon.name}</p>
                                            {pokemon?.nickname && (
                                                <p><strong>{pokemon.nickname}</strong></p>
                                            )}
                                            <div className={pro.levelBox}>
                                                <label>Level:</label>
                                                <p>{pokemon.level}</p>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                            ) : (
                            <p className={pro.noPokemon}>No Pokémon in party.</p>
                            )}
                        </div>        

                        <div className={pro.journalContainer}>
                            <h3 className={pro.h3}>Recent Journal Entries</h3>
                            <div className={pro.journalBodyContainer}>
                                {recentJournalEntries.length > 0 ? (
                                    <div className={pro.journalBox}>
                                        {recentJournalEntries.map((entry, index) => (
                                            <div key={index} className={pro.journalCard}>
                                                <div className={pro.journalHeader}>
                                                    <h2 className={pro.h2}>{entry.title}</h2>
                                                    <p className={pro.date}>{entry.timestamp}</p>
                                                </div>
                                                <div className={pro.journalBody}>
                                                    <p>{entry.content}</p>
                                                </div>
                                                <div className={pro.journalImgBox}>
                                                    <img src={entry.photo} alt="" />
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                ) : (
                                    <p className={pro.noEntries}>No journal entries yet.</p>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default UserProfilePage;
