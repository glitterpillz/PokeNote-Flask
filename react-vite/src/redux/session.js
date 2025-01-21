import { createSlice, createAsyncThunk } from "@reduxjs/toolkit"

const initialState = {
  user: null,
  loading: false,
  errors: null,
  userAccount: null,
};

export const restoreUser = createAsyncThunk(
  "session/restoreUser",
  async (_, { rejectWithValue }) => {
    try {
      const res = await fetch("/api/auth/session");
      const data = await res.json();

      if (!res.ok) {
        return rejectWithValue(data);
      }

      return data.user || data;
    } catch (error) {
      return rejectWithValue(error.message || "Trouble getting current user");
    }
  }
);

export const getUserById = createAsyncThunk(
  "session/getUserById",
  async (id, { rejectWithValue }) => {
    try {
      const res = await fetch(`/api/users/${id}`);
      const data = await res.json();
      return data;
    } catch (error) {
      return rejectWithValue(error.message || "User couldn't be found")
    }
  }
)

export const login = createAsyncThunk(
  "session/login",
  async ({ email, password }, { rejectWithValue }) => {
    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        return rejectWithValue(data.errors || { general: "Account disabled. Please contact support." });
      }

      return data.user || data;
    } catch (error) {
      return rejectWithValue({ general: error.message || "Login failed" });
    }
  }
);


export const signup = createAsyncThunk(
  "session/signup",
  async (
    {
      username,
      email,
      password,
      fname,
      lname,
      admin,
    },
    { rejectWithValue }
  ) => {
    try {
      const res = await fetch("/api/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username,
          email,
          password,
          fname,
          lname,
          admin,
        }),
      });
      const data = await res.json();

      if (!res.ok) {
        return rejectWithValue(data);
      }

      return data;
    } catch (error) {
      return rejectWithValue(error.message || "Signup failed");
    }
  }
);


export const logout = createAsyncThunk(
  "session/logout",
  async (_, { rejectWithValue }) => {
    try {
      await fetch("/api/auth/logout");
      return;
    } catch (error) {
      return rejectWithValue(error.message || "Logout failed");
    }
  }
);

// get user account
export const userAccount = createAsyncThunk(
  "session/account",
  async (_, { rejectWithValue }) => {
    try {
      const response = await fetch ('/api/auth/account');
      const data = await response.json();
      
      if (!response.ok) {
        throw { errors: data.errors || { general: "Error getting account"} };
      }
      return data;
    } catch (error) {
      return rejectWithValue(error.message || "Error fetching user account data");
    }
  }
)

// update user account
export const updateAccount = createAsyncThunk(
  "account/updateAccount",
  async ({ userId, formData }, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/auth/account/${userId}`, {
        method: 'PUT',
        body: formData,
      });

      const text = await response.text();

      if (!response.ok) {
        console.error('Error response:', text);
        return rejectWithValue(text);
      }

      try {
        const data = JSON.parse(text);
        return data;
      } catch (error) {
        return rejectWithValue('Failed to parse JSON');
      }

    } catch (error) {
      return rejectWithValue(error.message || 'Error updating user account');
    }
  }
);


export const deleteAccount = createAsyncThunk(
  "session/deleteAccount",
  async (_, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/auth/account`, {
        method: "DELETE",
        credentials: "include",
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(`Error deleting user account: ${data.message || "Unknown error"}`);
      }
      return data.message;
    } catch (error) {
      return rejectWithValue(error.message || "Error with fetch for deleting user account");
    }
  }
);


const sessionSlice = createSlice({
  name: "session",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(restoreUser.pending, (state) => {
        state.loading = true;
        state.errors = null;
      })
      .addCase(restoreUser.rejected, (state, action) => {
        state.loading = false;
        state.errors = action.payload;
      })
      .addCase(restoreUser.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.errors = null;
      })
      .addCase(login.rejected, (state, action) => {
        state.loading = false;
        state.errors = action.payload;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(signup.pending, (state) => {
        state.loading = true;
        state.errors = null;
      })
      .addCase(signup.rejected, (state, action) => {
        state.loading = false;
        state.errors = action.payload;
      })
      .addCase(signup.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload;
      })
      .addCase(logout.pending, (state) => {
        state.loading = true;
        state.errors = null;
      })
      .addCase(logout.rejected, (state, action) => {
        state.loading = false;
        state.errors = action.payload;
      })
      .addCase(logout.fulfilled, (state) => {
        state.loading = false;
        state.user = null;
      })
      .addCase(userAccount.pending, (state) => {
        state.loading = true;
        state.errors = null;
      })
      .addCase(userAccount.rejected, (state, action) => {
        state.loading = false;
        state.errors = action.payload;
      })
      .addCase(userAccount.fulfilled, (state, action) => {
        state.loading = false;
        state.userAccount = action.payload;
      })
      .addCase(updateAccount.pending, (state) => {
        state.loading = true;
        state.errors = null;
      })
      .addCase(updateAccount.rejected, (state, action) => {
        state.loading = false;
        state.errors = action.payload;
      })
      .addCase(updateAccount.fulfilled, (state, action) => {
        state.loading = false;
        state.userAccount = action.payload;
      })
      .addCase(deleteAccount.fulfilled, (state) => {
        state.user = null;
        state.userAccount = null;
      });
  },
});


export default sessionSlice.reducer;