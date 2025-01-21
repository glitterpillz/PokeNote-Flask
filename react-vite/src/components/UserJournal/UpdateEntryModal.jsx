import { useState } from "react";
import { useDispatch } from "react-redux";
import ent from "./CreateJournalEntryModal.module.css";
import { fetchEntryDetails } from "../../redux/journal";


const UpdateEntryModal = ({ entryDetails, closeModal }) => {
    const dispatch = useDispatch();
    const [errors, setErrors] = useState({});

    const [formData, setFormData] = useState({
        title: entryDetails?.title || "",
        content: entryDetails?.content || "",
        accomplishments: entryDetails?.accomplishments || "",
        timestamp: entryDetails?.timestamp?.split("T")[0] || "",
        photo: null,
        is_private: entryDetails?.is_private || false,
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData((prevState) => ({
            ...prevState,
            [name]: type === "checkbox" ? checked : value,
        }));
    };

    const handlePhotoChange = (e) => {
        const file = e.target.files[0];
        setFormData((prevState) => ({
            ...prevState,
            photo: file,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const errors = {};
        if (formData.title.length > 100) {
            errors.title = "Title cannot exceed 100 characters.";
        }
        if (formData.content.length > 2000) {
            errors.content = "Content cannot exceed 2000 characters.";
        }
        if (formData.accomplishments.length > 1000) {
            errors.accomplishments = "Accomplishments cannot exceed 1000 characters.";
        }

        if (Object.keys(errors).length > 0) {
            setErrors(errors);
            return;
        }

        const formDataToSend = new FormData();
        formDataToSend.append("title", formData.title);
        formDataToSend.append("content", formData.content);
        formDataToSend.append("accomplishments", formData.accomplishments);
        formDataToSend.append("is_private", formData.is_private);
        formDataToSend.append("timestamp", formData.timestamp);
        if (formData.photo) {
            formDataToSend.append("photo", formData.photo);
        }

        try {
            const response = await fetch(`/api/journal/${entryDetails.id}`, {
                method: "PUT",
                body: formDataToSend,
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || "Failed to update journal entry");
            }

            alert("Journal entry updated successfully!");

            dispatch(fetchEntryDetails(entryDetails.id))

            closeModal();
        } catch (error) {
            console.error("Error updating journal entry:", error);
            alert(error.message || "An error occurred.");
        }
    };

    return (
        <div className={ent.mainFormContainer}>
            <h2>Update Journal Entry</h2>
            <form onSubmit={handleSubmit} className={ent.form}>
                <div className={ent.inputBox}>
                    <label htmlFor="timestamp">Date:</label>
                    <input
                        id="timestamp"
                        type="date"
                        name="timestamp"
                        value={formData.timestamp}
                        onChange={handleChange}
                        className={ent.formInput}
                    />
                </div>
                
                <div className={ent.inputBox}>
                    <label htmlFor="title">Title:</label>
                    <input
                        id="title"
                        type="text"
                        name="title"
                        value={formData.title}
                        onChange={handleChange}
                        className={ent.formInput}
                        required
                    />
                </div>
                {errors.title && <div className={ent.error}>{errors.title}</div>}

                <div className={ent.contentBox}>
                    <label 
                        htmlFor="content"
                        className={ent.formLabel}   
                    >
                        Entry:
                    </label>
                    <textarea
                        id="content"
                        name="content"
                        value={formData.content}
                        onChange={handleChange}
                        className={ent.contentTextArea}
                        required
                    ></textarea>
                </div>
                {errors.content && <div className={ent.error}>{errors.content}</div>}

                <div className={ent.accomplishBox}>
                    <label 
                        htmlFor="accomplishments"
                        className={ent.formLabel}
                    >
                        Accomplishments:</label>
                    <textarea
                        id="accomplishments"
                        name="accomplishments"
                        value={formData.accomplishments}
                        onChange={handleChange}
                        className={ent.accomplishTextArea}
                    ></textarea>
                </div>
                {errors.accomplishments && <div className={ent.error}>{errors.accomplishments}</div>}

                <div className={ent.photoBox}>
                    <label htmlFor="photo">Upload Photo:</label>
                    <input
                        id="photo"
                        type="file"
                        onChange={handlePhotoChange}
                        className={ent.fileInput}
                    />
                    {formData.photo && (
                        <p>Selected Photo: {formData.photo.name}</p>
                    )}
                </div>

                <div className={ent.privateBox}>
                    <label
                        htmlFor="is_private"
                        className={ent.formLabel}
                    >
                        Private:
                    </label>
                    <input
                        id="is_private"
                        type="checkbox"
                        name="is_private"
                        checked={formData.is_private}
                        onChange={handleChange}
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
};

export default UpdateEntryModal;
