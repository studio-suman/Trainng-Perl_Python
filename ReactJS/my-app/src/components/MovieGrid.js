import React, {useEffect, useState} from "react"
import '../styles.css'

export default function MovieGrid () {

    const [movies, setMovies] = useState([]) //movies array, setMovies function, useState to modify the state

    useEffect(() => {
        fetch("movies.json")
        .then(response => response.json()) //response is converted to json
        .then(data => setMovies(data))  
    },
        [])

    return (
        <div className="movies-grid">
            {
                movies.map(movie => //map is a loop function to loop through each of the element
                (
                    <div key={movie.id} className="movie-card">
                        <img src= {`images/${movie.image}`} alt={movie.title}/>
                        <div className="movie-card-info">
                            <h3 className="movie-card-tile">{movie.title}</h3>
                            <p className="movie-card-genre">{movie.genre}</p>
                            <p className="movie-card-rating">{movie.rating}</p>
                        </div>
                    </div>
                    )
                )
            }
        </div>
    )
}