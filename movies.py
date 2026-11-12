def read_movies(filename):
    """
    Reads movie data from a CSV file.
    Creates two dictionaries:
    - titles: maps movie ID to movie title
    - ratings: maps movie ID to movie rating

    Returns both dictionaries.
    """
    titles = {}
    ratings = {}
    with open(filename, "r") as file:
        # TODO
        pass
  

    return titles, ratings

def get_movie_title(movie_id, titles):
    """
    Returns the title of the movie with the given ID.
    If the movie ID is not in the dictionary,
    returns "Movie not found".
    """
    # TODO
    pass


def get_highly_rated_movies(min_rating, titles, ratings):
    """
    Returns a list of titles of movies whose ratings
    are greater than or equal to min_rating.
    """
    result = []
    # TODO

    return result


def main():
    titles, ratings = read_movies("movies.csv")

    print(get_movie_title(1, titles))
    print(get_movie_title(100, titles))

    print(get_highly_rated_movies(8.4, titles, ratings))


main()