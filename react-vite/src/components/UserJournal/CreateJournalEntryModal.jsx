import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import { createJournalEntry, getUserJournal } from '../../redux/journal';
import ent from './CreateJournalEntryModal.module.css'

function CreateJournalEntryModal() {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [accomplishments, setAccomplishments] = useState('');
    const [date, setDate] = useState('');
    const [isPrivate, setIsPrivate] = useState(false);
    const [photo, setPhoto] = useState(null);
    const [errors, setErrors] = useState({});

    const handleSubmit = async (e) => {
        e.preventDefault();

        const entryData = new FormData();
        entryData.append('title', title);
        entryData.append('content', content);
        entryData.append('accomplishments', accomplishments);
        entryData.append('date', date);
        entryData.append('is_private', isPrivate);
        if (photo) {
            entryData.append('photo', photo);
        }

        try {
            await dispatch(createJournalEntry(entryData)).unwrap();
            alert('Journal entry created successfully!');

            dispatch(getUserJournal());

            closeModal();
        } catch (error) {
            console.error('Error creating journal entry:', error);
            setErrors(error.errors || {}); 
            alert('Failed to create journal entry. Please try again.');
        }
    };

    const handlePhotoChange = (e) => {
        setPhoto(e.target.files[0]);
    }

    return (
        <div className={ent.mainFormContainer}>
            <div className={ent.mewPic}>
                <img src="/images/mew.png" alt="" />
            </div>
            <form className={ent.form} onSubmit={handleSubmit}>
                <div className={ent.formHeading}>
                    <div className={ent.inputBox}>
                        <label>
                            Date:
                        </label>
                        <input
                            type="date"
                            value={date}
                            onChange={(e) => setDate(e.target.value)}
                            className={ent.formInput}
                        />
                    </div>

                    <div className={ent.inputBox}>
                        <label>
                            Title:
                        </label>
                        <input
                            type="text"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            className={ent.formInput}
                            required
                        />
                    </div>
                    {errors.title && (
                        <div className={ent.error}>{errors.title[0]}</div> 
                    )}

                </div>

                <div className={ent.contentBox}>
                    <label className={ent.formLabel}>
                        Entry:
                    </label>
                    <textarea
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        className={ent.contentTextArea}
                        required
                    />
                    {errors.content && (
                        <div className={ent.error}>{errors.content[0]}</div> 
                    )}
                </div>

                <div className={ent.accomplishBox}>
                    <label className={ent.formLabel}>
                        Accomplishments:
                    </label>
                    <textarea
                        value={accomplishments}
                        onChange={(e) => setAccomplishments(e.target.value)}
                        className={ent.accomplishTextArea}
                    />
                    {errors.accomplishments && (
                        <div className={ent.error}>{errors.accomplishments[0]}</div>
                    )}
                </div>

                <div className={ent.photoBox}>
                    <div className={ent.photoLabelBox}>
                        <label className={ent.formLabel} htmlFor="photo">Upload Photo:</label>
                        <label className={ent.optional}>(optional)</label>
                        <input
                            id="photo"
                            type="file"
                            onChange={handlePhotoChange}
                            className={`${ent.fileInput} ${ent.hiddenFileInput}`}
                        />
                    </div>
                    <div className={ent.fileButtonField}>
                        <button
                            type="button"
                            className={ent.customFileButton}
                            onClick={() => document.getElementById('photo').click()}
                        >
                            Choose File
                        </button>
                        <span className={ent.fileName}>
                            {photo ? photo.name : "No file chosen"}
                        </span>
                    </div>
                </div>

                <div className={ent.privateBox}>
                    <label className={ent.formLabel}>
                        Private Entry:
                    </label>
                    <input
                        type="checkbox"
                        checked={isPrivate}
                        onChange={() => setIsPrivate((prev) => !prev)}
                    />
                </div>

                <div className={ent.formButtons}>
                    <button type="submit" className={ent.button}>
                        Save
                    </button>
                    <button 
                        type="button" 
                        className={ent.button} 
                        onClick={closeModal}
                    >
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    );
}

export default CreateJournalEntryModal;
