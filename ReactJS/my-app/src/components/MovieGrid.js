import { useEffect, useState } from "react"
import '../styles.css'
import MovieCard from "./MovieCard"

export default function MovieGrid() {

    const [movies, setMovies] = useState([]) //movies array, setMovies function, useState to modify the state

    const [searchTerm, setsearchTerm] = useState("") //creating Search bar logic

    const [genre, setGenre] = useState("All Genres")
    const [rating, setRating] = useState("All")

    const handleSearchChange = (e) => {
        setsearchTerm(e.target.value)
    }

    const matchGenre = (movie, genre) => {
        return genre === "All Genres" || movie.genre.toLowerCase() === genre.toLowerCase()
    }

    const matcSearchTerm = (movie, searchTerm) => {
        return movie.title.toLowerCase().includes(searchTerm.toLowerCase())
    }

    const matchRating = (movie, rating) => {
        switch (rating) {
            case 'All':
                return true
            case 'Good':
                return movie.rating >= 8
            case 'Ok':
                return  movie.rating >= 5 && movie.rating < 8
            case 'Bad':
                return movie.rating < 5
            default:
                return false
        }
    }

    const filteredMovies = movies.filter(movie =>
        matchGenre(movie, genre) && matcSearchTerm(movie, searchTerm) && matchRating(movie, rating) //filter logic
    )

    const handleGenreChange = (e) => {
        setGenre(e.target.value)
    }

    const handleRatingChange = (e) => {
        setRating(e.target.value)
    }

    useEffect(() => {
        fetch("movies.json")
            .then(response => response.json()) //response is converted to json
            .then(data => setMovies(data))
    },
        [])

    return (
        <div>
            <input type="text" placeholder="Search Movies" className="search-input" value={searchTerm} onChange={handleSearchChange} /> {/*creating search bar*/}
            <div className="filter-bar">
                <div className="filter-slot">
                    <label>Genre</label>
                    <select className="filter-dropdown" value={genre} onChange={handleGenreChange}>
                        <option>All Genres</option>
                        <option>Action</option>
                        <option>Drama</option>
                        <option>Fantasy</option>
                        <option>Horror</option>
                    </select>
                </div>
                <div className="filter-slot">
                    <label>Rating</label>
                    <select className="filter-dropdown" value={rating} onChange={handleRatingChange}>
                        <option>All</option>
                        <option>Good</option>
                        <option>Ok</option>
                        <option>Bad</option>
                    </select>
                </div>
            </div>
            <div className="movies-grid">
                {
                    filteredMovies.map(movie => //map is a loop function to loop through each of the element
                    (
                        <MovieCard movie={movie} key={movie.id}></MovieCard>
                    ))}
            </div>
        </div>
    )
}