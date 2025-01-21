import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import * as sessionActions from "../../redux/session";
import Navigation from "../Navigation";
import lan from "./LandingPage.module.css";
import { useNavigate } from "react-router-dom";

function LandingPage() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(sessionActions.restoreUser()).then(() => setIsLoaded(true));
  }, [dispatch]);

  if (!isLoaded) {
    return <div className={lan.loading}>Loading...</div>;
  }

  return (
    <div className={lan.landingPageMain}>
        <div className={lan.navContainer}>
          <Navigation />
        </div>
        <div className={lan.landingPageContainer}>
          <div className={lan.welcomeImageBox}>
            <div className={lan.infoBox}>
              <h2>Journal your Training Journey!</h2>
              <p>Connect with other Trainers and share your achievements</p>
            </div>
            <img src="/images/logo-main-cropped.png" alt="" />
          </div>
          <div className={lan.bodyContainer}>
            <div 
              className={lan.featuresContainer}
              onClick={() => navigate('/journal/user')}  
            >
              <div className={lan.journalIcon}>
                <img src="/images/journal.png" alt="" />
              </div>
              <h3>Journal</h3>
              <p>Capture and cherish your Pokémon trainer journey with personalized journal entries, where you can reflect on your adventures and accomplishments. Keep them private or share with others on the Discover tab.</p>
            </div>
            <div 
              className={lan.featuresContainer}
              onClick={() => navigate('/pokedex')}
            >
              <div className={lan.searchIcon}>
                <img src="/images/search-icon.png" alt="" />
              </div>
              <h3>Pokedex</h3>
              <p>Explore the world of Pokémon with ease using the comprehensive Pokédex, allowing you to search, learn, and strategize with detailed Pokémon data. Add pokémon to your collection and keep track of their progress!</p>
            </div>
            <div 
              className={lan.featuresContainer}
              onClick={() => navigate('/discover')}
            >
              <div className={lan.globeIcon}>
                <img src="/images/globe.png" alt="" />
              </div>
              <h3>Discover</h3>
              <p>Dive into the adventures of fellow trainers by browsing their public journal entries. Share your experiences with others, and engage with likes and comments to build a vibrant Pokémon community.</p>
            </div>
          </div>
        </div>
    </div>
  )
}

export default LandingPage;