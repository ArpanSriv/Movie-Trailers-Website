class Movie():
    """Stores the details of any particular website."""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Constructor requires three parameters,
        :param title: Stores the title of the Movie
        :param poster_image_url: The Poster Image Url of the Movie
        :param trailer_youtube_url: The YouTube Trailer URL of the Movie

        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
