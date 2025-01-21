import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const initialState = {
    inbox: [],
    sentBox: [],
    deleteBox: [],
    messageDetails: null,
    loading: false,
    errors: null
}

export const getUserInbox = createAsyncThunk(
    "/message/getUserInbox",
    async (_, { rejectWithValue }) => {
        try {
            const response = await fetch('/api/messages/inbox', {
                method: 'GET'
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Error getting user inbox: ${data.message}`);
            }
            return data;
        } catch (error) {
            return rejectWithValue(error.message || "Error fetching inbox");
        }
    }
)

export const getUserSentBox = createAsyncThunk(
    "/message/getUserSentBox",
    async (_, { rejectWithValue }) => {
        try {
            const response = await fetch('/api/messages/sent', {
                method: 'GET'
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Error getting user sent box: ${data.message}`);
            }
            return data;
        } catch (error) {
            return rejectWithValue(error.message || "Error fetching sent box");
        }
    }
)   


export const getDeletedMessages = createAsyncThunk(
    "/message/getDeletedMessages",
    async (_, { rejectWithValue }) => {
        try {
            const response = await fetch('/api/messages/deleted', {
                method: 'GET'
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Error getting user deleted messages: ${data.message}`);
            }
            return data;
        } catch (error) {
            return rejectWithValue(error.message || "Error fetching deleted messages");
        }
    }
)


export const sendMessage = createAsyncThunk(
    "message/sendMessage",
    async (messageData, { rejectWithValue }) => {
        try {
            const response = await fetch('/api/messages/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(messageData),
            });
            const data = await response.json();
            if (!response.ok) {
                return rejectWithValue(data);
            }
            return data.sent_message;
        } catch (error) {
            return rejectWithValue(error.message || "Error sending direct message");
        }
    }
);


export const deleteInboxMessage = createAsyncThunk(
    "message/deleteInboxMessage",
    async (id, { rejectWithValue }) => {
        try {
            const response = await fetch(`/api/messages/inbox/${id}`, {
                method: 'DELETE'
            })
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Error deleting message: ${data.message}`);
            }
            return data.deleted_message || id;
        } catch (error) {
            return rejectWithValue(error.message || "Error deleting message");
        }
    }
)


export const deleteSentMessage = createAsyncThunk(
    "message/deleteSentMessage",
    async (id, { rejectWithValue }) => {
        try {
            const response = await fetch(`/api/messages/sent/${id}`, {
                method: 'DELETE'
            })
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Error deleting message: ${data.message}`);
            }
            return data.deleted_message || id;
        } catch (error) {
            return rejectWithValue(error.message || "Error deleting message");
        }
    }
)


export const cleanupDeletedBox = createAsyncThunk(
    "/message/cleanupDeletedBox",
    async (_, { rejectWithValue }) => {
        try {
            const response = await fetch('/api/messages/deleted', {
                method: 'DELETE'
            })
            const data = await response.json();
            if (!response.ok) {
                return rejectWithValue(data);
            }
            return data;
        } catch (error) {
            return rejectWithValue(error.message || "Error fetching delete all messages")
        }
    }
)


const MessageSlice = createSlice({
    name: "message",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(getUserInbox.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(getUserInbox.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(getUserInbox.fulfilled, (state, action) => {
                state.loading = false;
                state.inbox = action.payload;
            })
            .addCase(getUserSentBox.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(getUserSentBox.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(getUserSentBox.fulfilled, (state, action) => {
                state.loading = false;
                state.sentBox = action.payload;
            })
            .addCase(getDeletedMessages.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(getDeletedMessages.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(getDeletedMessages.fulfilled, (state, action) => {
                state.loading = false;
                state.deleteBox = action.payload;
            })
            .addCase(sendMessage.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(sendMessage.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(sendMessage.fulfilled, (state, action) => {
                state.loading = false;
                if (Array.isArray(state.sentBox)) {
                    state.sentBox.push(action.payload);
                } else {
                    console.error("State sentBox is not an array", state.sentBox)
                }
            })
            .addCase(deleteInboxMessage.fulfilled, (state, action) => {
                const messageId = action.payload;
                if (messageId) {
                    const deletedMessage = state.inbox.find((message) => message.id === messageId);
                    if (deletedMessage) {
                        state.inbox = state.inbox.filter((message) => message.id !== messageId);
                        state.deleteBox.push(deletedMessage);
                    }
                } else {
                    console.error("deleteMessage.fulfilled: action.payload is undefined");
                }
            })
            .addCase(deleteSentMessage.fulfilled, (state, action) => {
                const messageId = action.payload;
                if (messageId) {
                    const deletedMessage = state.sentBox.find((message) => message.id === messageId);
                    if (deletedMessage) {
                        state.sentBox= state.sentBox.filter((message) => message.id !== messageId);
                        state.deleteBox.push(deletedMessage);
                    }
                } else {
                    console.error("deleteMessage.fulfilled: action.payload is undefined");
                }
            })
            .addCase(cleanupDeletedBox.fulfilled, (state, action) => {
                state.loading = false;
                state.deleteBox = action.payload || [];
            })
            
    }
})

export default MessageSlice.reducer;