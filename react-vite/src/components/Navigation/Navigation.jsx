import { useState } from "react";
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import nav from "./Navigation.module.css";
import { useDispatch, useSelector } from "react-redux";
import { login } from "../../redux/session"; 
import { useNavigate } from "react-router-dom";

function Navigation() {
  const [isSidePanelOpen, setIsSidePanelOpen] = useState(false);
  const { user } = useSelector((state) => state.session); 
  const [isDropdownOpen, setIsDropdownOpen] = useState(false); 
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const openSidePanel = () => {
    setIsSidePanelOpen(true);
  };

  const closeSidePanel = () => {
    setIsSidePanelOpen(false);
  };

  const handleLogin = (userType) => {
    let email, password;
    if (userType === "demoUser") {
      email = "demo@example.com";
      password = "password";
    } else if (userType === "demoAdmin") {
      email = "admin@example.com";
      password = "password";
    }

    dispatch(login({ email, password })).then(() => {
      navigate("/");
      setIsDropdownOpen(false);
    });
  };

  return (
    <div className={nav.mainNavContainer}>
      <div className={nav.sidePanelContainer}></div>
      <button className={nav.sidePanelOpenBtn} onClick={openSidePanel}>
        ☰
      </button>

      <div
        className={`${nav.sidePanel} ${isSidePanelOpen ? nav.open : ""}`}
      >
        <button className={nav.sidePanelCloseBtn} onClick={closeSidePanel}>
          &times;
        </button>
        <nav>
          <img src="/images/logo-main.png" alt="" />
          <ul className={nav.navList}>
            <li className={nav.navItem}>
              <NavLink
                to="/"
                className={nav.navLink}
                onClick={closeSidePanel}
              >
                Home
              </NavLink>
              <NavLink
                to="/journal/user"
                className={nav.navLink}
                onClick={closeSidePanel}
              >
                Journal
              </NavLink>
              <NavLink
                to="/pokemon/collection"
                className={nav.navLink}
                onClick={closeSidePanel}
              >
                Collection
              </NavLink>
              <NavLink
                to="/pokedex"
                className={nav.navLink}
                onClick={closeSidePanel}
              >
                Pokedex
              </NavLink>
              <NavLink
                to="/discover"
                className={nav.navLink}
              >
                Discover
              </NavLink>
              <hr />
              <p
                onClick={() => window.alert('Feature coming soon!')}
                className={nav.navLink}
              >
                About
              </p>
              <p
                onClick={() => window.alert('Feature coming soon!')}
                className={nav.navLink}
              >
                Contact Us
              </p>
            </li>
          </ul>
        </nav>
      </div>

      <div className={nav.profileButton}>
        <ProfileButton />
        {!user && (
          <div className={nav.dropdownContainer}>
            <button
              className={nav.dropdownButton}
              onClick={() => setIsDropdownOpen(!isDropdownOpen)}
            >
              Demo
            </button>
            {isDropdownOpen && (
              <div className={nav.dropdownMenu}>
                <button className={nav.dropButton} onClick={() => handleLogin("demoUser")}>Demo User</button>
                <button className={nav.dropButton} onClick={() => handleLogin("demoAdmin")}>Demo Admin</button>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default Navigation;


