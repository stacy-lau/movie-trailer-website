""" This module allows users to view web-based documents in browsers."""
import webbrowser


""" The class below provides a way to store movie-related information. \
Creating a class creates a new type of object. Classes contain data and/or \
methods for objects."""


class Movie():

    """ The __init__ function/method lives within the class and \
    creates space in memory to remember data provided in \
    the arguments. 'Self' is the instance being created. Each \
    argument that follows 'self' receives the correct value once \
    'init' is called. These inputs (values provided in \
    entertainment_center.py) will be used as outputs on the \
    Fresh Tomatoes HTML page and in the instance method below."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ This is an instance method, which is a function within this class. \
    A browser window opens with the appropriate movie trailer URL."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
