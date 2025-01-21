import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { getUserJournal } from "../../redux/journal";
import { useModal } from "../../context/Modal";
import Navigation from "../Navigation";
import CreateJournalEntryModal from "./CreateJournalEntryModal";
import ent from './UserJournalPage.module.css'
import { useNavigate } from "react-router-dom";
import { IoMdArrowRoundUp } from "react-icons/io";


const UserJournalPage = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { setModalContent } = useModal();
    const currentUser = useSelector((state) => state.session.user);
    const { journal, loading, errors } = useSelector((state) => state.journal);
    const [scrollTopButton, setScrollTopButton] = useState(false);
    

    useEffect(() => {
        dispatch(getUserJournal());
    }, [dispatch]);

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


    const handleCreateJournal = () => {
        setModalContent(<CreateJournalEntryModal closeModal={() => setModalContent(null)} />);
    };        

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    };

    if (loading) {
        return <div className={ent.loading}>Loading...</div>;
    }

    if (errors) {
        return <div className={ent.errors}>Error: {errors.general || "Something went wrong"}</div>;
    }
    
    const journalEntries = journal?.Journal || [];
    
    const upArrow = <IoMdArrowRoundUp 
        className={ent.upArrow} 
        style={{ 
            'color': '#ffd444',
            'borderRadius': '50%',
            'fontSize': '40px',
            'cursor': 'pointer'
        }}
    />

    return (
        <div>
            <div className={ent.navbar}>
                <Navigation />
                {scrollTopButton && (
                    <div
                        className={`${ent.scrollTopButton} ${scrollTopButton ? ent.show : ''}`}
                        onClick={scrollToTop}
                    >
                        {upArrow}
                    </div>
                )}
                
            </div>
            <div className={ent.mainBodyContainer}>
                <div className={ent.headerBox}>
                    <h1 className={ent.h1}>{currentUser?.fname}&apos;s Journal</h1>
                    <button 
                        className={ent.headerButton} 
                        onClick={handleCreateJournal}
                    >
                        Create Entry
                    </button>
                </div>
                <div className={ent.entriesContainer}>
                    {journalEntries.length > 0 ? (
                        <div className={ent.entryCardBox}>
                            {journalEntries.map((entry) => (
                                <div key={entry.id} className={ent.entryCard}>
                                    
                                    <div className={ent.entryHeader}>
                                        <h2 className={ent.h2}>{entry.title}</h2>
                                        <p className={ent.entryDate}>{new Date(entry.timestamp).toLocaleDateString()}</p>
                                    </div>

                                    <button
                                        className={ent.button}
                                        onClick={() => navigate(`/journal/${entry.id}`)}
                                    >
                                        View
                                    </button>

                                    <div className={ent.entryBody}>
                                        <div className={ent.contentBox}>
                                            <h5 className={ent.h5}>Entry:</h5>
                                            <p>{entry.content}</p>
                                        </div>
                                        <div className={ent.contentBox}>
                                            <h5 className={ent.h5}>Accomplishments:</h5>
                                            <p>{entry.accomplishments}</p>
                                        </div>
                                    </div>
                                    
                                    {entry.photo && (
                                        <div className={ent.photoBox}>
                                            <img className={ent.entryPhoto} src={entry.photo}
                                            alt="Journal Entry"
                                        />
                                        </div>
                                    )}
                                </div>
                            ))}
                        </div>
                    ) : (
                        <p className={ent.errors}>No journal entries found.</p>
                    )}
                </div>
            </div>
        </div>
    );
};

export default UserJournalPage;
