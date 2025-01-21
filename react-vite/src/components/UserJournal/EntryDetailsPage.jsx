import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchEntryDetails, deleteEntry } from "../../redux/journal";
import { useModal } from "../../context/Modal";
import UpdateEntryModal from "./UpdateEntryModal";
import { sendMessage } from "../../redux/message";
import { useParams, useNavigate } from "react-router-dom";
import Navigation from "../Navigation";
import { restoreUser } from "../../redux/session";
import journ from './EntryDetailsPage.module.css';

function EntryDetailsPage() {
    const { id } = useParams();
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { setModalContent } = useModal();
    const entryDetails = useSelector((state) => state.journal.entryDetails);
    const isLoading = useSelector((state) => state.journal.loading);
    const errors = useSelector((state) => state.journal.errors);
    const currentUser = useSelector((state) => state.session.user);

    useEffect(() => {
        if (!currentUser) {
            dispatch(restoreUser());
        }
    }, [dispatch, currentUser]);

    useEffect(() => {
        if (currentUser) {
            dispatch(fetchEntryDetails(id));
        }
    }, [dispatch, currentUser, id]);

    const handleUpdateEntry = (entryDetails) => {
        setModalContent(
            <UpdateEntryModal
                entryDetails={entryDetails}
                closeModal={() => setModalContent(null)} 
            />
        );
    };

    const handleDelete = async (id) => {
        const userConfirmed = window.confirm(
            "Are you sure you want to delete this entry?"
        );

        if (!userConfirmed) return;

        try {
            await dispatch(deleteEntry(id)).unwrap();
            const messageData = {
                receiver: entryDetails.username,
                content: `Your journal entry (ID: ${id}) has been removed by Admin)`
            };
            await dispatch(sendMessage(messageData)).unwrap();
            alert("Journal entry successfully deleted!");
            navigate('/journal/user');
        } catch (error) {
            console.error("Error deleting journal entry", error);
            alert("Failed to delete entry. Please try again.");
        }
    };

    if (isLoading) {
        return <div className={journ.pageDiv}>Loading...</div>;
    }

    if (errors) {
        return <div className={journ.pageDiv}>Error: {errors}</div>;
    }

    if (!entryDetails || !entryDetails.title) {
        return <div className={journ.pageDiv}>Journal entry not found.</div>;
    }

    const canEdit = currentUser.id === entryDetails.user_id;
    const canDelete = currentUser.id === entryDetails.user_id || currentUser.admin;

    return (
        <div className={journ.mainContainer}>
            <div className={journ.navbar}>
                <Navigation />
            </div>
            <div className={journ.mainDetailsContainer}>
                <div className={journ.headerBox}>
                    <h1 className={journ.h1}>{entryDetails.title}</h1>
                    <p className={journ.date}>{new Date(entryDetails.timestamp).toLocaleDateString()}</p>
                </div>
                <div className={journ.detailsContainer}>
                    <div className={journ.usernameDiv}>
                        <label className={journ.label}>Username:</label>
                        <p>{entryDetails.username}</p>
                    </div>
                    <div className={journ.contentDiv}>
                        <label className={journ.label}>Content:</label>
                        <p>{entryDetails.content}</p>
                    </div>
                    {canEdit && (
                        <div className={journ.contentDiv}>
                            <label className={journ.label}>Accomplishments:</label>
                            <p>{entryDetails.accomplishments}</p>
                        </div>
                    )}
                    <div className={journ.photoDiv}>
                        <label className={journ.label}>Entry Photo:</label>
                        {entryDetails.photo ? (
                            <img className={journ.photo} src={entryDetails.photo} alt="Entry Photo" />
                        ) : (
                            <p>No photo</p>
                        )}
                    </div>
                    <div className={journ.buttonsContainer}>

                        {canEdit && (
                            <button
                                className={journ.button}
                                onClick={() => handleUpdateEntry(entryDetails)}
                            >
                                Edit
                            </button>
                        )}
                        {canDelete && (
                            <button
                                className={journ.button}
                                onClick={() => handleDelete(entryDetails.id)}
                            >
                                Delete
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default EntryDetailsPage;

