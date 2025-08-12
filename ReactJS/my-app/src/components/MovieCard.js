import "../styles.css";
import React from "react";

export default function MovieCard({ movie, isWatchlisted, toggleWatchlist}) {
  const handleError = (e) => {
    //Error Handling
    e.target.src = "images/default.jpg";
  };

  const getRatingclass = (rating) => {
    if (rating >= 8) {
      return "rating-good";
    }
    if (rating >= 5 && rating < 8) return "rating-ok";

    if (rating < 5) return "rating-bad";


  };

  const getRatingclass1 = (rating) => rating>=8 ? "rating-good" : rating < 5 ? "rating-bad" : "rating-ok";
    



  return (
    <div key={movie.id} className="movie-card">
      <img
        src={`images/${movie.image}`}
        alt={movie.title}
        onError={handleError}
      />
      <div className="movie-card-info">
        <h3 className="movie-card-tile">{movie.title}</h3>
        <div>
            <span className="movie-card-genre">{movie.genre}/</span>
            <span className={`movie-card-rating ${getRatingclass(movie.rating)}`}>
          {movie.rating}
        </span>
        </div>
        <label className="switch">
            <input type="checkbox" checked={isWatchlisted} onChange={() => toggleWatchlist(movie.id)}>
            </input>
            <span className="slider">
                <span className="slider-label">
                    {isWatchlisted ? "In Watchlist" : "Add to Watchlist"}
                </span>
            </span>
        </label>
      </div>
    </div>
  ); // calling the rating getRating class
}
