import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./styles.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import MovieGrid from "./components/MovieGrid";
import Watchlist from "./components/Watchlist";
import Login from "./components/LoginPage";
import api from "./services/api";
import Registration from "./components/Registration";

function App() {
  const [movies, setMovies] = useState([]);
  const [watchlist, setWatchlist] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [loggedIn, setLoggedIn] = useState(() => {
    return !!localStorage.getItem("token");
  });

  const handleRegistration = () => {
    setLoggedIn(true);
  };

  const toggleWatchlist = (movieId) => {
    setWatchlist((prev) =>
      prev.includes(movieId)
        ? prev.filter((id) => id !== movieId)
        : [...prev, movieId]
    );
  };

  useEffect(() => {
    const controller = new AbortController();

    const load = async () => {
      setLoading(true);
      setError("");
      try {
        const res = await api.get("/movies", { signal: controller.signal });
        setMovies(res.data);
      } catch (err) {
        if (err.name === "CanceledError" || err.code === "ERR_CANCELED") {
          // request was aborted; ignore
          return;
        }
        const status = err.response?.status;
        if (status === 401) {
          // optional: auto-logout on auth failure
          localStorage.removeItem("token");
          setLoggedIn(false);
        }
        setError(
          err.response?.data?.message ||
            err.message ||
            "Something went wrong while fetching movies."
        );
      } finally {
        setLoading(false);
      }
    };

    load();
    return () => controller.abort();
  }, [loggedIn]);

  return (
    <Router>
      <div className="App">
        <Header />
        <div className="container">
          {loggedIn && (
            <nav>
              <ul>
                <li>
                  <Link to="/Home">Home</Link>
                </li>
                <li>
                  <Link to="/Watchlist">Watchlist</Link>
                </li>
              </ul>
            </nav>
          )}
          <Routes>
            <Route path="/" element={<Login onLogin={handleRegistration} />} />
            <Route path="/Registration" element={<Registration onLogin={handleRegistration} />} />
            <Route
              path="/Home"
              element={
                <MovieGrid
                  movies={movies}
                  watchlist={watchlist}
                  toggleWatchlist={toggleWatchlist}
                />
              }
            />
            <Route
              path="/watchlist"
              element={
                <Watchlist
                  movies={movies}
                  watchlist={watchlist}
                  toggleWatchlist={toggleWatchlist}
                />
              }
            />
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
