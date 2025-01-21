import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as sessionActions from "../../redux/session";
import * as journalActions from "../../redux/journal";
import { sendMessage } from "../../redux/message";
import Navigation from "../Navigation";
import { Link } from "react-router-dom";
import { IoMdArrowRoundUp } from "react-icons/io";
import dis from "./DiscoverPage.module.css";

function DiscoverPage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [isLoaded, setIsLoaded] = useState(false);
    const { journal, loading, errors } = useSelector((state) => state.journal);
    const [scrollTopButton, setScrollTopButton] = useState(false);

    const currentUser = useSelector((state) => state.session.user)

    useEffect(() => {
        dispatch(sessionActions.restoreUser()).then(() => setIsLoaded(true));
    }, [dispatch]);

    useEffect(() => {
        dispatch(journalActions.getAllEntries());
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

    const handleReport = async (postId, username) => {
        const userConfirmed = window.confirm(
            " Are you sure you want to report this entry? WARNING - Admin will be notified, and entry may be removed."
        );

        if (!userConfirmed) {
            return;
        }
        
        const messageData = {
            receiver: 'admin_user',
            content: `Journal entry reported. Post ID: ${postId}, Username: ${username}`
        };

        try {
            await dispatch(sendMessage(messageData)).unwrap();
            alert('Journal entry reported!')
        } catch (error) {
            alert("Failed to report the journal entry. Please try again.")
        }
    }

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    };

    if (loading || !isLoaded) {
        return <div className={dis.loading}>Loading...</div>;
    }

    if (errors) {
        return <div className={dis.errors}>Error: {errors}</div>;
    }

    const renderJournalEntries = (entryList) => {

        return entryList.map((entry) => (
            <div key={entry.id} className={dis.entryCard}>
                <div className={dis.mainHeaderContainer}>
                    <div className={dis.profilePicBox}>
                        <img src={entry.profile_picture} alt="" />
                    </div>
                    <div className={dis.header}>
                        <Link to={`/user/${entry.user_id}/profile`} className={dis.profileLink}>
                            {entry.username}
                        </Link>
                        <p className={dis.timestamp}>{entry.timestamp}</p>
                    </div>
                </div>
                <div className={dis.entryInfo}>
                    <h1 className={dis.h1}>{entry.title}</h1>
                    <p className={dis.entryBody}>{entry.content}</p>
                    <img  className={dis.entryPic} src={entry.photo} alt="" />
                    {currentUser.admin ? (
                        <button
                            className={dis.reviewButton}
                            onClick={() => navigate(`/journal/${entry.id}`)}
                        >
                            Review
                        </button>
                    ) : (
                        <button 
                            className={dis.reportButton}
                            onClick={() => handleReport(entry.id, entry.username)}
                        >
                            Report
                        </button>
                    )}
                    
                    
                </div>
            </div>
        ));
    };

    const upArrow = <IoMdArrowRoundUp 
        className={dis.upArrow} 
        style={{ 
            'color': '#ffd444',
            'borderRadius': '50%',
            'fontSize': '40px',
            'cursor': 'pointer'
        }}
    />

    return (
        <div className={dis.mainContainer}>
            <Navigation />

            {scrollTopButton && (
                <div
                    className={`${dis.scrollTopButton} ${scrollTopButton ? dis.show : ''}`}
                    onClick={scrollToTop}
                >
                    {upArrow}
                </div>
            )}

                <div className={dis.mainHeader}>
                    <img className={dis.bannerImg} src="/images/adventure.jpg" alt="" />
                    <h4 className={dis.h4}>Explore the adventures of trainers around the world!</h4>
                    <p className={dis.headerMessage}>Discover stories, milestones, and moments shared by the community</p>
                </div>

            <div className={dis.mainBodyContainer}>
                {journal.length > 0 ? renderJournalEntries(journal) : <p className={dis.errors}>No entries found.</p>}
            </div>
        </div>
    );
}

export default DiscoverPage;
