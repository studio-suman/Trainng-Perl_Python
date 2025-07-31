import axios from "axios";

const API = axios.create({ baseURL: "http://localhost:8000" });

export const login = (data) => API.post("/login", data);
export const register = (data) => API.post("/register", data);
export const getItems = (token) =>
  API.get("/items", { headers: { Authorization: `Bearer ${token}` } });
export const createItem = (data, token) =>
  API.post("/items", data, { headers: { Authorization: `Bearer ${token}` } });
