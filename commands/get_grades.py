from __future__ import print_function
import os
from utils.movie_util import filenames_to_search_strings, print_movies
from utils.filmtipset_util import get_grades

def is_proper_movie_file(filename):
    FILE_ENDINGS = [".mkv", ".mp4", ".avi", ".iso", ".mov", ".mpeg"]
    # Proper filenames
    for ending in FILE_ENDINGS:
        if filename.endswith(ending):
            return True

    # Not other filenames, or files starting with .
    if "." in filename[-4:] or filename.startswith("."):
        return False

    # Not stuff that ends with "-ignore"
    if filename.endswith("-ignore"):
        return False

    # Only directories left
    return True

def get_movies(dir):
    movies = os.listdir(dir)
    movies = [movie for movie in movies if is_proper_movie_file(movie)]
    return movies

def main(directory):
    print("Loading movies from: %s" % directory)
    movies = get_movies(directory)
    movies = filenames_to_search_strings(movies)
    graded = get_grades(movies)

    print_movies("Movies seen, by your grade (and Filmtipset grade)", filter(lambda x: x["type"] == u'seen', graded))
    print_movies("Movies not seen, by your grade (and Filmtipset grade)", filter(lambda x: x["type"] != u'seen', graded))
