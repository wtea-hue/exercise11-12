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
        file.readline()
        for line in file:
            items = line.split(",")
            movie_id = int(items[0])
            titles[movie_id] = items[1]
            ratings[movie_id] = float(items[4])
  

        return titles, ratings

def get_movie_title(movie_id, titles):
    if movie_id in titles:
        return titles[movie_id]
    else:
        return "Movie not found"
    """
    Returns the title of the movie with the given ID.
    If the movie ID is not in the dictionary,
    returns "Movie not found".
    """
    # TODO


def get_highly_rated_movies(min_rating, titles, ratings):
    result = []
    for movie_id in ratings:
        if ratings[movie_id] >= min_rating:
            result.append(titles[movie_id])


    return result


def main():
    titles, ratings = read_movies("movies.csv")
    print(get_movie_title(1, titles))
    print(get_movie_title(100, titles))

    print(get_highly_rated_movies(8.4, titles, ratings))


main()