from __future__ import print_function
import os
import sys
from movie_util import filenames_to_search_strings, print_movies
from filmtipset_util import get_grades

def is_proper_movie_file(filename):
    FILE_ENDINGS = [".mkv", ".mp4", ".avi", ".iso", "mpeg", ]
    if filename[-4:] in FILE_ENDINGS:
        return True
    elif (filename.find(".") == -1 and not filename.endswith("-ignore")):
        return True
    return False

def get_movies(dir):
    movies = os.listdir(dir)
    movies = [movie for movie in movies if is_proper_movie_file(movie)]
    return movies

def main(directory, debug=False):
    print("Loading movies from: %s" % directory)
    movies = get_movies(directory)
    movies = filenames_to_search_strings(movies)
    graded = get_grades(movies, debug=debug)

    print_movies("Movies seen, by grade", sorted(filter(lambda x: x[1] == u'seen', graded), reverse=True))
    print_movies("Movies not seen, by grade", sorted(filter(lambda x: x[1] != u'seen', graded), reverse=True))

# Possible calls:
# lookup_from_filesystem.py /My-Movies/
# lookup_from_filesystem.py /My-Movies/ --verbose
if __name__ == "__main__":
    directory = sys.argv[1]
    debug = False
    if len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            debug = True
    main(directory=directory, debug=debug)