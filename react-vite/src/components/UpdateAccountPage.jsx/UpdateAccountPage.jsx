import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as sessionActions from '../../redux/session';
import update from './UpdateAccountPage.module.css';
import { useNavigate } from "react-router-dom";
import Navigation from "../Navigation";
import { FaArrowLeft } from "react-icons/fa";

const UpdateAccountPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const currentUser = useSelector((state) => state.session.userAccount?.user);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [profilePicture, setProfilePicture] = useState(null);
  const [bannerUrl, setBannerUrl] = useState(null);
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (!currentUser) {
      dispatch(sessionActions.userAccount());
    }
  }, [dispatch, currentUser]);

  useEffect(() => {
    if (currentUser) {
      setUsername(currentUser.username || "");
      setEmail(currentUser.email || "");
    }
  }, [currentUser]);

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (!currentUser) {
      setErrors({ general: "User not found" });
      return;
    }
  
    const updatedData = new FormData();
    updatedData.append("username", username !== currentUser.username ? username : currentUser.username);
    updatedData.append("email", email !== currentUser.email ? email : currentUser.email);
  
    if (profilePicture instanceof File) {
      updatedData.append("profile_picture", profilePicture);
    }
    if (bannerUrl instanceof File) {
      updatedData.append("banner_url", bannerUrl);
    }
  
    try {
      await dispatch(
        sessionActions.updateAccount({ userId: currentUser.id, formData: updatedData })
      ).unwrap();
  
      alert("Account updated successfully!");
      navigate("/account");
    } catch (backendErrors) {
      try {
        const parsedErrors = JSON.parse(backendErrors);
        if (parsedErrors.errors) {
          setErrors(parsedErrors.errors); 
        } else {
          setErrors({ general: "An unexpected error occurred." });
        }
      } catch (error) {
        setErrors({ general: "An error occurred while processing the response." });
      }
    }
  };
    
  
  const handleProfilePictureChange = (e) => {
    setProfilePicture(e.target.files[0]);
  };

  const handleBannerUrlChange = (e) => {
    setBannerUrl(e.target.files[0]);
  };

  const handleDelete = async () => {
    if (window.confirm("Are you sure you want to delete your account?")) {
        try {
            const message = await dispatch(sessionActions.deleteAccount()).unwrap();
            alert(message || "Account deleted successfully.");
            navigate("/");
        } catch (error) {
            console.error("Delete account error:", error);
            alert(`Failed to delete account: ${error}`);
        }
    }
};


  const backArrow = <div className={update.backArrow}><FaArrowLeft /></div>

  return (
    <div className={update.updateMainContainer}>
      <div className={update.navbar}>
        <Navigation />
      </div>
      <div className={update.updateBodyContainer}>
        <h1 className={update.h1}>Edit Account</h1>
        <form onSubmit={handleSubmit} className={update.form}>
          <div className={update.formField}>
            <label>Username</label>
            <input
              className={update.input}
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Username"
              required
            />            
          </div> 
          {errors.username && <div className={update.validateError}>{errors.username}</div>}
          <div className={update.formField}>
            <label>Email</label>
              <input
                className={update.input}
                name="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                required
              />
          </div> 
          {errors.email && <div className={update.validateError}>{errors.email}</div>} 
          <div className={update.fileFormField}>
            <label htmlFor="profilePicture">Profile Picture</label>
            <input
              id="profilePicture"
              type="file"
              onChange={handleProfilePictureChange}
              className={update.fileInput}
            />
            <div className={update.fileButtonField}>
              <button
                type="button"
                className={update.customFileButton}
                onClick={() => document.getElementById('profilePicture').click()}
              >
                Choose File
              </button>
              <span className={update.fileName}>
                {profilePicture ? profilePicture.name : "No file chosen"}
              </span>
            </div>
          </div>
          <div className={update.fileFormField}>
            <label htmlFor="bannerUrl">Banner Image</label>
            <input
                id="bannerUrl"
                type="file"
                onChange={handleBannerUrlChange}
                className={update.fileInput}
              />
            <div className={update.fileButtonField}>
              <button
                type="button"
                className={update.customFileButton}
                onClick={() => document.getElementById('bannerUrl').click()}
              >
                Choose File
              </button>
              <span className={update.fileName}>
                {bannerUrl ? bannerUrl.name : "No file chosen"}
              </span>
            </div>
          </div>
          <button type="submit" className={update.button}>
            Update Account
          </button>
        </form>
        <div className={update.footerButtons}>
          <button 
            type="button" 
            className={update.backButton}
            onClick={() => navigate('/account')}
          >
            {backArrow}Back
          </button>
          <button
            type="button"
            className={update.deleteButton}
            onClick={handleDelete}
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
};

export default UpdateAccountPage;