
// src/api/client.js
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
});

// Attach token automatically (if present)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers = config.headers || {};
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;

export const login = (data) => api.post("/login", data);
export const register = (data) => api.post("/register", data);
export const getItems = (token) =>
  api.get("/items", { headers: { Authorization: `Bearer ${token}` } });
export const createItem = (data, token) =>
  api.post("/items", data, { headers: { Authorization: `Bearer ${token}` } });
