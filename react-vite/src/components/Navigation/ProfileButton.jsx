import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { RiUser4Line } from "react-icons/ri";
import * as sessionActions from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import profile from "./ProfileButton.module.css";

function ProfileButton() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((state) => state.session.user);
  const ulRef = useRef();

  const toggleMenu = (e) => {
    e.stopPropagation();
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!user) {
      dispatch(sessionActions.restoreUser());
    }

    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu, dispatch, user]);

  const closeMenu = () => setShowMenu(false);

  const logout = async (e) => {
    e.preventDefault();
    await dispatch(sessionActions.logout());
    navigate("/");
    closeMenu();
  };

  const userIcon = <RiUser4Line />;

  return (
    <div className={profile.profileButtonContainer}>
      <button className={profile.profileButton} onClick={toggleMenu}>{userIcon}</button>
      {showMenu && (
        <div className={profile.profileDropdown} ref={ulRef}>
          <ul>
            {user ? (
              <>
                <li className={profile.hiMessage}>Hi, {user.fname}!</li>
                <li>{user.username}</li>
                <li>{user.email}</li>
                <hr />
                <li>
                  <NavLink className={profile.accountLink} to="/inbox">Inbox</NavLink>
                </li>
                <li>
                  <NavLink className={profile.accountLink} to="/account">Manage Account</NavLink>
                </li>
                <li>
                  <NavLink className={profile.accountLink} to={`/user/${user.id}/profile`}>View Profile</NavLink>
                </li>
                {user.admin && (
                  <li>
                    <NavLink className={profile.accountLink} to="/users">User Accounts</NavLink>
                  </li>
                )}
                <hr />
                <li>
                  <button onClick={logout} className={profile.modalButton}>
                    Log Out
                  </button>
                </li>
              </>
            ) : (
              <>
                <div className={profile.modalButtonContainer}>
                  <OpenModalMenuItem
                    itemText="Log In"
                    onItemClick={closeMenu}
                    modalComponent={<LoginFormModal navigate={navigate} />}
                    className={profile.modalButton}
                  />
                  <OpenModalMenuItem
                    itemText="Sign Up"
                    onItemClick={closeMenu}
                    modalComponent={<SignupFormModal navigate={navigate} />}
                    className={profile.modalButton}
                  />
                </div>
              </>
            )}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ProfileButton;
