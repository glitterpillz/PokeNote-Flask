import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import { editUserPokemon, fetchPokemonDetail } from '../../redux/pokemon';
import { useState } from 'react';
import edit from './EditPokemonModal.module.css';

function EditPokemonModal({ pokemon }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const [nickname, setNickname] = useState(pokemon.nickname || '');
    const [level, setLevel] = useState(pokemon.level || '');
    const [stats, setStats] = useState(
        pokemon.pokemon.stats.map((stat) => ({
            ...stat,
        }))
    );
    const [customMoves, setCustomMoves] = useState({
        move1: pokemon.custom_moves?.move1 || '',
        move2: pokemon.custom_moves?.move2 || '',
        move3: pokemon.custom_moves?.move3 || '',
        move4: pokemon.custom_moves?.move4 || '',
    });
    const [selectedParty, setSelectedParty] = useState(pokemon.selected_party);
    
    const [errors, setErrors] = useState({
        level: '',
        nickname: '',
    });

    const handleStatChange = (index, value) => {
        setStats((prevStats) =>
            prevStats.map((stat, i) =>
                i === index ? { ...stat, stat_value: value } : stat
            )
        );
    };

    const handleCustomMoveChange = (moveKey, value) => {
        setCustomMoves((prevMoves) => ({
            ...prevMoves,
            [moveKey]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        let validationErrors = {};
        
        if (level < 1) {
            validationErrors.level = 'Level must be at least 1';
        }
    
        if (nickname.length > 100) {
            validationErrors.nickname = 'Nickname cannot be longer than 100 characters';
        }
    
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        }
    
        const payload = {
            nickname,
            level,
            stats: stats.map((stat) => ({
                stat_name: stat.stat_name,
                stat_value: Number(stat.stat_value),
            })),
            custom_moves: customMoves,
            selected_party: selectedParty,
        };
    
        try {
            await dispatch(editUserPokemon({ id: pokemon.id, payload })).unwrap();
            alert('Pokémon updated successfully!');
            dispatch(fetchPokemonDetail(pokemon.id));
            closeModal();
        } catch (error) {
            console.error('Error updating Pokémon:', error);
            alert('Failed to update Pokémon. Please try again.');
        }
    };

    return (
        <form className={edit.form} onSubmit={handleSubmit}>
            <div className={edit.header}>
                <h2 className={edit.h2}>Edit Pokémon</h2>
            </div>
            <div className={edit.inputBox}>
                <label className={edit.label}>
                    Nickname:
                </label>
                <input
                    type="text"
                    value={nickname}
                    onChange={(e) => setNickname(e.target.value)}
                    className={edit.input}
                />
            </div>
            {errors.nickname && <div className={edit.errors}>{errors.nickname}</div>}
            <div className={edit.inputBox}>
                <label className={edit.label}>
                    Level:
                </label>
                <input
                    type="number"
                    value={level}
                    onChange={(e) => setLevel(e.target.value)}
                    className={edit.input}
                />
            </div>
            {errors.level && <div className={edit.errors}>{errors.level}</div>}
            <h3 className={edit.h3}>Stats:</h3>
            <div className={edit.inputContainer}>
                {stats.map((stat, index) => (
                    <div key={index} className={edit.inputBox}>
                        <label className={edit.label}>
                            {stat.stat_name}:
                        </label>
                        <input
                            type="number"
                            value={stat.stat_value}
                            onChange={(e) =>
                                handleStatChange(index, e.target.value)
                            }
                            className={edit.input}
                        />
                    </div>
                ))}
            </div>
            <h3 className={edit.h3}>Moves:</h3>
            <div className={edit.inputContainer}>
                {['move1', 'move2', 'move3', 'move4'].map((moveKey, index) => (
                    <div key={index} className={edit.inputBox}>
                        <label className={edit.label}>
                            {`Move ${index + 1}:`}
                        </label>
                        <input
                            type="text"
                            value={customMoves[moveKey]}
                            onChange={(e) => handleCustomMoveChange(moveKey, e.target.value)}
                            className={edit.input}
                        />
                    </div>
                ))}
            </div>
            <div className={edit.addPartyDiv}>
                <label>Add to Party</label>
                <input
                    type="checkbox"
                    checked={selectedParty}
                    onChange={(e) => setSelectedParty(e.target.checked)}
                />
            </div>
            <div className={edit.buttonsContainer}>
                <button className={edit.button} type="submit">Save</button>
                <button className={edit.button} type="button" onClick={closeModal}>
                    Cancel
                </button>
            </div>
        </form>
    );
}

export default EditPokemonModal;
