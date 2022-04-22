import React, { useState, useRef, useEffect, useContext } from "react";
import AuthContext from "./AuthProvider.js";
import axios from "/workspace/Buddy-App/src/api/axios.js";
import { Link } from "react-router-dom";
import "../css/login.css";

const LOGIN_URL = "./auth";
const LoginForm = ({ Login, error }) => {
  // const [details, setDetails] = useState({ username: "", password: "" });

  const submitHandler = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        LOGIN_URL,
        JSON.stringify({ user, pwd }),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(JSON.stringify(response?.data));
      const accessToken = response?.data?.accessToken;
      const roles = response?.data?.roles;
      setAuth({user, pwd, roles, accessToken})
      setUser("");
      setPwd("");
    } catch (err) {
      console.log("No response dawg");
    }
  };

  const { setAuth } = useContext(AuthContext);

  const userRef = useRef();
  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");

  // useEffect(() =>{
  //   userRef.current.focus();
  // }, [])

  return (
    <>
      <div className="inputs">
        <form onSubmit={submitHandler}>
          {error != "" ? <div className="error">{error}</div> : ""}
          <label>
            <input
              type="text"
              className="username"
              name="name"
              placeholder="Username"
              id="username"
              ref={userRef}
              autoComplete="off"
              onChange={(e) => setUser(e.target.value)}
              value={user}
              required
            />
          </label>
          <br></br>
          <label>
            <input
              type="password"
              className="password"
              placeholder="Password"
              id="password"
              ref={userRef}
              onChange={(e) => setPwd(e.target.value)}
              value={pwd}
              required
            />
          </label>
          <br></br>
          <br></br>

          <Link to="/ForgotPassword">
            <label href="/" className="iforgor">
              Forgot Password?
            </label>
          </Link>

          <div>
            <Link to="/WelcomeApp">
              <button type="submit" value="Login" className="login-button">
                Login
              </button>
            </Link>
            <Link to="/AccountApp">
              <button className="account-button">Create a new account</button>
            </Link>
          </div>
        </form>
      </div>
    </>
  );
};

export default LoginForm;
