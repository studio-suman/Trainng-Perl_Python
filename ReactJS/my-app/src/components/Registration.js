import React, { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

function Registration({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [useremail, setEmail] = useState("");   
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleRegistration = async () => {
    setLoading(true);
    try {
      const res = await api.post("/register", {
        username,
        password,
        useremail,
        valid: "True"
      });
      //localStorage.setItem("token", res.data.access_token);
      onLogin(); // Navigate or update state after login
      navigate("/");
      alert(res.data?.detail || "Registration Successfull");
    } catch (err) {
      alert(err.response?.data?.detail || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-96 bg-black-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h2 className="text-2xl font-bold mb-4 text-black">Registration</h2>
        <input
          type="email"
          placeholder="Email"
          className="w-full p-2 mb-4 border text-black border-gray-300 rounded"
          value={useremail}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="text"
          placeholder="Username"
          className="w-full p-2 mb-4 border text-black border-gray-300 rounded"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full p-2 mb-4 border text-black border-gray-300 rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          onClick={handleRegistration}
          disabled={loading}
          className={`w-full p-2 rounded ${
            loading ? "bg-gray-400" : "bg-blue-500 hover:bg-blue-600"
          } text-white`}
        >
          {loading ? "Registering in..." : "Register"}
        </button>
      </div>
    </div>
  );
}

export default Registration;
