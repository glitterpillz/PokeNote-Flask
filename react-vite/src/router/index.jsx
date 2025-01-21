import { createBrowserRouter } from 'react-router-dom';
import LandingPage from '../components/LandingPage/LandingPage';
import PokedexPage from '../components/PokedexPage/PokedexPage';
import UserAccountPage from '../components/UserAccountPage/UserAccountPage';
import UpdateAccountPage from '../components/UpdateAccountPage.jsx';
import UserProfilePage from '../components/UserProfilePage/index.js';
import PokemonDetailsPage from '../components/PokemonDetailsPage/PokemonDetailsPage.jsx';
import UserJournalPage from '../components/UserJournal/UserJournalPage.jsx';
import DiscoverPage from '../components/DiscoverPage/DiscoverPage.jsx';
import UserPokemonCollection from '../components/UserPokemon/UserPokemonCollection.jsx';
import UserPokemonDetails from '../components/UserPokemon/UserPokemonDetails.jsx';
import EntryDetailsPage from '../components/UserJournal/EntryDetailsPage.jsx';
import UserInboxPage from '../components/UserMessages/UserInboxPage.jsx';
import AdminAllUsersPage from '../components/Admin/AdminAllUsersPage.jsx';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <LandingPage />
  },
  {
    path: '/pokedex',
    element: <PokedexPage />
  },
  {
    path: '/pokemon/:id',
    element: <PokemonDetailsPage />
  },
  {
    path: '/pokemon/collection',
    element: <UserPokemonCollection />
  },
  {
    path: '/pokemon/collection/:id',
    element: <UserPokemonDetails />
  },
  {
    path: '/user/:id/profile',
    element: <UserProfilePage />
  },
  {
    path: '/journal/user',
    element: <UserJournalPage />
  },
  {
    path: '/journal/:id',
    element: <EntryDetailsPage />
  },
  {
    path: '/discover',
    element: <DiscoverPage />
  },
  {
    path: '/account',
    element: <UserAccountPage />
  },
  {
    path: '/account/update',
    element: <UpdateAccountPage />
  },
  {
    path: '/inbox',
    element: <UserInboxPage />
  },
  {
    path: '/users',
    element: <AdminAllUsersPage />
  }
]);
