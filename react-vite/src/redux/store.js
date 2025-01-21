import { configureStore } from '@reduxjs/toolkit';
import { default as logger } from "redux-logger";
import sessionReducer from './session';
import pokemonReducer from './pokemon';
import userReducer from './user';
import journalReducer from './journal'
import MessageReducer from './message'

const store = configureStore({
  reducer: {
    session: sessionReducer,
    pokemon: pokemonReducer,
    user: userReducer,
    journal: journalReducer,
    message: MessageReducer,
  },
  middleware: (getDefaultMiddleware) => {
    const middlewares = getDefaultMiddleware();
    if (process.env.NODE_ENV === "development") {
      middlewares.push(logger);
    }
    return middlewares;
  },
  devTools: process.env.NODE_ENV !== "production",
});

export default store;
