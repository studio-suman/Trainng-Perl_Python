import '../styles.css'

export default function MovieCard({ movie }) {

    const handleError = (e) => {                //Error Handling
        e.target.src = "images/default.jpg"
    }

    const getRatingclass = (rating) => {
        if(rating >= 8 ) {
            return 'rating-good'
        }
        if(rating >=5 && rating <8) return 'rating-ok'

        if (rating <5) return 'rating-bad'
    }

    return (
        <div key={movie.id} className="movie-card">
            <img src={`images/${movie.image}`} alt={movie.title} onError={handleError} />
            <div className="movie-card-info">
                <h3 className="movie-card-tile">{movie.title}</h3>
                <p className="movie-card-genre">{movie.genre}</p>
                <p className={`movie-card-rating ${getRatingclass(movie.rating)}`}>{movie.rating}</p> 
            </div>
        </div>
    ) // calling the rating getRating class
}