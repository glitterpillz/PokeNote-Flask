import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import * as sessionActions from "../../redux/session";
import login from "./LoginForm.module.css";

function LoginFormModal({ navigate }) {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      sessionActions.login({ email, password })
    );

    if (serverResponse.type === "session/login/rejected") {
      setErrors(serverResponse.payload || {});
    } else {
      navigate("/");
      closeModal();
    }
  };

  return (
    <div className={login.loginModalContainer}>
      <h1 className={login.h1}>Log In</h1>
      <form className={login.form} onSubmit={handleSubmit}>
        <div className={login.inputBox}>
          <label>Email</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className={login.formInput}
            required
          />
        </div>
        {errors.email && <p className={login.errorText}>{errors.email}</p>}
        <div className={login.inputBox}>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className={login.formInput}
            required
          />
        </div>
        {errors.password && <p className={login.errorText}>{errors.password}</p>}
        {errors.general && <p className={login.errorText}>{errors.general}</p>}
        <button type="submit" className={login.loginSubmit}>
          Submit
        </button>
      </form>
    </div>
  );
}

export default LoginFormModal;
