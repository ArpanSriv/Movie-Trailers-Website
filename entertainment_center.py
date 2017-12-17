import media
import fresh_tomatoes

# Defining Movies
spider_man = media.Movie(
    "Spider-Man Homecoming",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man_Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=n9DwoQ7HWvI"
)
avengers = media.Movie(
    "Avengers: Infinity War",
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Avengers_Infinity_War.jpg/220px-Avengers_Infinity_War.jpg",  # noqa
    "https://www.youtube.com/watch?v=B65hW9YYY5A"
)
rampage = media.Movie(
    "Rampage",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Rampage_teaser_film_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=5AhfGD3Ly8k"
)
justice_league = media.Movie(
    "Justice League",
    "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=K11ZpbZ_r78"
)

# List of Movies
Movies = [
    spider_man,
    avengers,
    rampage,
    justice_league
]

# Passing List of Movies to open_movies_page function
fresh_tomatoes.open_movies_page(Movies)
