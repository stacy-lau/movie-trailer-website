""" fresh_tomatoes.py and media.py need to be included within the same
directory as this .py file in order for the code to work"""
import fresh_tomatoes
import media

""" Six instances of a movie are listed below. Each instance contains the
movie_title, movie_storyline, poster_image, and trailer_youtube attributes."""
lion = media.Movie("Lion",
                   "A five-year-old Indian boy gets lost on the streets of \
                    Calcutta, thousands of kilometers from home. 25 years \
                    later, he sets out to find his lost family.",
                   "https://upload.wikimedia.org/wikipedia/en/f/f0/Lion_%282016_film%29.png",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")

moonlight = media.Movie("Moonlight",
                        "A chronicle of the childhood, adolescence and \
                         burgeoning adulthood of a young, African-American, \
                         gay man growing up in a rough neighborhood of Miami.",
                        "https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png",
                        "https://www.youtube.com/watch?v=9NJj12tJzqc")

fences = media.Movie("Fences",
                     "A working-class African-American father tries to raise \
                      his family in the 1950s, while coming to terms with the \
                      events of his life.",
                     "https://upload.wikimedia.org/wikipedia/en/0/0d/Fences_%28film%29.png",
                     "https://www.youtube.com/watch?v=a2m6Jvp0bUw")

hidden_figures = media.Movie("Hidden Figures",
                             "The story of a team of female African-American \
                              mathematicians who served a vital role in NASA \
                              during the early years of the U.S. \
                              space program.",
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",
                             "https://www.youtube.com/watch?v=RK8xHq6dfAo")

lala_land = media.Movie("La La Land",
                        "While waiting for their big breaks, two proper L.A. \
                         dreamers, a suavely- charming, soft-spoken \
                         jazz pianist and a brilliant, vivacious playwright, \
                         attempt to reconcile aspirations and relationship \
                         in a magical old-school romance.",
                        "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")


guardians = media.Movie("Guardians of the Galaxy Vol. 2",
                        "The Guardians must fight to keep their newfound \
                         family together as they unravel the mystery of \
                         Peter Quill's true parentage.",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                        "https://www.youtube.com/watch?v=pr7tDrwQ3t8")

""" NOTE: I realize that the poster_image URLs are longer than 80 \
characters long but I didn't want to break the URLs."""

""" Movie objects stored in a list data structure."""
movies = [lion, moonlight, fences, hidden_figures, lala_land, guardians]

""" Function uses list of movies to build HTML file to display website."""
fresh_tomatoes.open_movies_page(movies)

""" All movie storylines quoted from respective IMDb entries \
for each film. \
All poster images retrieved from respective Wikipedia entries \
for each film."""
