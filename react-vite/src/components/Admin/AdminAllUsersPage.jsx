import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as adminActions from '../../redux/user';
import { restoreUser } from "../../redux/session";
import Navigation from "../Navigation";
import all from './AdminAllUsersPage.module.css';

function AdminAllUsersPage() {
    const dispatch = useDispatch();
    const [isLoaded, setIsLoaded] = useState(false);

    const { users, loading, errors } = useSelector((state) => state.user);

    useEffect(() => {
        dispatch(restoreUser()).then(() => setIsLoaded(true));
    }, [dispatch]);

    useEffect(() => {
        dispatch(adminActions.getAllUsers());
    }, [dispatch]);

    const handleDisableUser = async (userId, isDisabled) => {
        const disabled = !isDisabled;
        await dispatch(adminActions.toggleUserDisabled({ userId, disabled }));
        dispatch(adminActions.getAllUsers());
    };

    if (loading || !isLoaded) {
        return <div className={all.loading}>Loading...</div>;
    }

    if (errors) {
        return <div className={all.errors}>Error: {errors}</div>;
    }

    const renderUsers = (userList) => {
        if (!userList || userList.length === 0) {
            return <p>No users found.</p>;
        }

        return userList.map((item, index) => {
            const user = item.user; 
            if (!user) return null;

            return (
                <div
                    key={user.id || `${user.username}-${index}`}
                    className={all.userCard}
                >
                    <div className={all.statusBox}>
                        <p className={all.adminStatus}>{user.admin ? 'Admin' : 'User'}</p>
                    </div>

                    <img 
                        src={user.profile_picture || "default-avatar.png"} 
                        alt={user.username || "user"} 
                        className={all.profilePic}
                    />
                    
                    <div className={all.userDataDiv}>
                        <div className={all.dataBox}>
                            <label>username:</label>
                            <p>{user.username || "N/A"}</p>
                        </div>
                        <div className={all.dataBox}>
                            <label>first name:</label>
                            <p>{user.fname || "N/A"}</p>
                        </div>                        
                    </div>

                    <div className={all.userDataDiv}>
                        <div className={all.dataBox}>
                            <label>email:</label>
                            <p>{user.email || "N/A"}</p>
                        </div>
                        <div className={all.dataBox}>
                            <label>last name:</label>
                            <p>{user.lname || "N/A"}</p>
                        </div>
                    </div>

                    <button
                        className={all.disableButton}
                        onClick={() => handleDisableUser(user.id, user.disabled)}
                    >
                        {user.disabled ? "Enable" : "Disable"}
                    </button>
                </div>
            );
        });
    };

    return (
        <div className={all.mainContainer}>
            <div>
                <Navigation />
            </div>
            <div className={all.header}>
                <h2>Manage Users</h2>
            </div>
            <div className={all.mainBodyContainer}>
                {renderUsers(users || [])}
            </div>
        </div>
    );
}

export default AdminAllUsersPage;
