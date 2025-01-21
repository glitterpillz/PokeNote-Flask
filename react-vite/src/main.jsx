import React from "react";
import ReactDOM from "react-dom/client";
import { Provider as ReduxProvider } from "react-redux";
import { RouterProvider } from "react-router-dom";
import store from "./redux/store";
import { router } from "./router";
import { ModalProvider, Modal } from "./context/Modal";
import { MessageProvider } from "./context/MessageContext"; // Added for additional context
import * as sessionActions from "./redux/session";
import "./index.css";

if (import.meta.env.MODE !== "production") {
  window.store = store;
  window.sessionActions = sessionActions;
}

export const AppProviders = ({ children }) => (
  <ReduxProvider store={store}>
    <MessageProvider>
      <ModalProvider>{children}</ModalProvider>
    </MessageProvider>
  </ReduxProvider>
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AppProviders>
      <RouterProvider router={router} />
      <Modal />
    </AppProviders>
  </React.StrictMode>
);
