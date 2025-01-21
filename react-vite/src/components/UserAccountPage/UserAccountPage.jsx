import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as sessionActions from '../../redux/session'
import { getPokemonParty } from "../../redux/pokemon";
import Navigation from "../Navigation";
import acc from './UserAccountPage.module.css'
import { useNavigate } from "react-router-dom";

const UserAccountPage = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { userAccount, loading, errors } = useSelector((state) => state.session);

    const { pokemons, loading: partyLoading } = useSelector((state) => state.pokemon)

    useEffect(() => {
      dispatch(sessionActions.userAccount());
    }, [dispatch]);

    useEffect(() => {
      dispatch(getPokemonParty())
    }, [dispatch])


    if (loading || partyLoading) {
      return <div className={acc.loading}>Loading...</div>;
    }
  
    if (errors) {
      return <div className={acc.errors}>Error: {errors.general || "Something went wrong"}</div>;
    }
  
    if (!userAccount || !userAccount.user) {
      return <div className={acc.errors}>No account data available.</div>;
    }
  
    const { user } = userAccount;

    const journalEntries = [...(user.journal_entries || [])]
      .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
      .slice(0, 5);

    const pokemonParty = pokemons?.Pokemon || [];
  
    return (
      <div>
        <div className={acc.navbar}>
            <Navigation />
        </div>
        <div className={acc.accountMainContainer}>
          <img className={acc.backgroundImg} src={user.banner_url} alt="" />
          <div className={acc.header}>
            <div className={acc.profilePicBox}>
              {user.profile_picture ? (
                <img
                    className={acc.profilePicImg}
                    src={user.profile_picture}
                    alt={`${user.username}'s profile picture`}
                />
                ) : (
                <p><strong>Profile Picture:</strong> None</p>
                )}
                <div className={acc.profileInfoBox}>
                  <p>
                    <strong>{user.username}</strong> <br />
                    {user.email || "N/A"}
                  </p>
                </div>
            </div>
            <button onClick={() => navigate('/account/update')}>
              Edit
            </button>
          </div>
          <hr className={acc.hr}/>
          <div className={acc.mainInfoContainer}>
            <div className={acc.nameContainer}>
              <div className={acc.nameBox}>
                 <p>First Name</p>
                 <p className={acc.nameTitle}>{user.fname || "N/A"}</p>
              </div>
              <div className={acc.nameBox}>
                <p>Last Name</p>
                <p className={acc.nameTitle}>{user.lname || "N/A"}</p>
              </div>
            </div>
            <div className={acc.linkContainer}>
              <div className={acc.linkHeader}>
                <h2 className={acc.h2}>Pokemon Party</h2>
                <button
                  type="button"
                  className={acc.manageButton}
                  onClick={() => navigate('/pokemon/collection')}
                >
                  See All
                </button>
              </div>
              <hr />
              {pokemonParty.length > 0 ? (
                <div className={acc.entryList}>
                    {pokemonParty.slice(0, 6).map((pokemon, index) => (
                      <div 
                        key={index} 
                        className={acc.listEntry}
                        onClick={() => navigate(`/pokemon/collection/${pokemon.id}`)}
                      >
                        <p>{pokemon.pokemon.name || "Unnamed Pokemon"}</p>
                        {pokemon?.nickname && (
                          <p>Nickname: {pokemon.nickname}</p>
                        )}
                        <p>Level: {pokemon.level}</p>
                      </div>
                    ))}
                </div>
              ) : (
                <p className={acc.noEntries}>No Pokémon in collection.</p>
              )}
            </div>
            <div className={acc.linkContainer}>
              <div className={acc.linkHeader}>
                <h2 className={acc.h2}>Journal Entries</h2>
                <button
                  type="button"
                  className={acc.manageButton}
                  onClick={() => navigate('/journal/user')}
                >
                  See All
                </button>
              </div>
              <hr />
              {journalEntries.length > 0 ? (
                <div className={acc.entryList}>
                    {journalEntries.slice(0, 5).map((entry, index) => (
                      <div 
                        key={index} 
                        className={acc.listEntry}
                        onClick={() => navigate(`/journal/${entry.id}`)}
                      >
                        <p>{entry.timestamp}</p>
                        <p>{entry.title || "Untitled Entry"}</p>
                      </div>
                    ))}
                </div>
                ) : (
                <p className={acc.noEntries}>No journal entries yet.</p>
                )}          
              </div>            
            </div>
          </div>
      </div>
    );
  };
  
  export default UserAccountPage;