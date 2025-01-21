import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const initialState = {
    journal: [],
    entryDetails: null,
    loading: false,
    errors: null
}


export const getAllEntries = createAsyncThunk(
    "journal/getAllEntries",
    async (_, { rejectWithValue }) => {
        try {
            const response = await fetch("/api/journal", {
                method: 'GET'
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Error getting journal entries: ${data.message}`);
            }
            return data;
        } catch (error) {
            return rejectWithValue(error.message || "Error fetching all journal entries")
        }
    }
)


export const getUserJournal = createAsyncThunk(
    "journal/getUserJournal",
    async (_, { rejectWithValue }) => {
        try {
            const response = await fetch("/api/journal/user");
            const data = await response.json();
            if (!response.ok) {
                return rejectWithValue(data);
            }
            return data;
        } catch (error) {
            console.error("getUserJournal error:", error);
            return rejectWithValue(error.message || "Error fetching user journal")
        }
    }
)

export const createJournalEntry = createAsyncThunk(
    "journal/createJournalEntry",
    async (formData, { rejectWithValue }) => {
        try {
            const response = await fetch('/api/journal/post', { method: 'POST', body: formData });
            const data = await response.json();
            console.log("Backend response:", data); 
            if (!response.ok) {
                return rejectWithValue(data);
            }
            return data.journal;
        } catch (error) {
            return rejectWithValue(error.message || "Error posting journal entry");
        }
    }
);


export const fetchEntryDetails = createAsyncThunk(
    "journal/fetchEntryDetails",
    async (id, { rejectWithValue }) => {
        try {
            const response = await fetch(`/api/journal/${id}`);
            const data = await response.json();
            console.log("API Response:", data);
            if (!response.ok) {
                return rejectWithValue(data.error || "Error fetching journal entry");
            }
            return data;
        } catch (error) {
            console.error("fetchEntryDetails error:", error);
            return rejectWithValue(error.message || "Error fetching entry");
        }
    }
);


export const updateEntry = createAsyncThunk(
    "journal/updateEntry",
    async ({ id, payload }, { rejectWithValue }) => {
        try {
            const response = await fetch(`/api/journal/${id}`, {
                method: "PUT",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || 'Failed to update journal entry') 
            }
            return data.entryDetails;
        } catch (error) {
            return rejectWithValue(error.message || 'Error updating journal entry')
        }
    }
)

export const deleteEntry = createAsyncThunk(
    "journal/deleteEntry",
    async (id, { rejectWithValue }) => {
        try {
            const response = await fetch(`/api/journal/${id}`, {
                method: 'DELETE',
            });
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Failed to delete entry");
            }
            return { id, message: data.message || "Journal entry deleted successfully"}
        } catch (error) {
            return rejectWithValue(error.message || "Error removing journal entry")
        }
    }
);



const journalSlice = createSlice({
    name: "journal",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(getAllEntries.pending, (state) => {
                state.loading = true;
                state.errors = false;
            })
            .addCase(getAllEntries.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload.message || action.payload;
            })
            .addCase(getAllEntries.fulfilled, (state, action) => {
                state.loading = false;
                state.journal = action.payload.journal || action.payload;
            })
            .addCase(getUserJournal.pending, (state) => {
                state.loading = true;
                state.errors = false;
            })
            .addCase(getUserJournal.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload.message || action.payload;
            })
            .addCase(getUserJournal.fulfilled, (state, action) => {
                state.loading = false;
                state.journal = action.payload.journal || action.payload; 
                state.entryDetails = action.payload.entryDetails || null;
            })
            .addCase(createJournalEntry.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(createJournalEntry.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(createJournalEntry.fulfilled, (state, action) => {
                state.loading = false;
                if (Array.isArray(state.journal)) {
                    state.journal.push(action.payload); 
                } else {
                    console.error("State journal is not an array:", state.journal);
                }
            })
            .addCase(fetchEntryDetails.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(fetchEntryDetails.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(fetchEntryDetails.fulfilled, (state, action) => {
                state.loading = false;
                state.entryDetails = action.payload;
            })
            .addCase(updateEntry.pending, (state) => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(updateEntry.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(updateEntry.fulfilled, (state, action) => {
                state.loading = false;
                state.entryDetails = action.payload;
            })                  
            .addCase(deleteEntry.fulfilled, (state, action) => {
                state.journal = (Array.isArray(state.journal) ? state.journal : []).filter(
                    (entry) => entry.id !== action.payload.id
                )
            })
    }
});

export default journalSlice.reducer;
