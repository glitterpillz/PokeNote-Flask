import { createContext, useContext, useState } from "react";

const MessageContext = createContext();

export const MessageProvider = ({ children }) => {
    const [view, setView] = useState("inbox");

    return (
        <MessageContext.Provider value={{ view, setView }}>
            {children}
        </MessageContext.Provider>
    );
};

export const useMessageContext = () => useContext(MessageContext);