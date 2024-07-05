class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    # TODO 3) Instantiate a NetflixQueue object.
    # TODO 4) Add your movies to the Netflix queue.
    # TODO 5) Print all the movies in your queue.
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."

    shrek_2 = Movie("Shrek 2", 5)
    twilight = Movie("twilight", 0)
    despicable_me = Movie("Despicable Me", 4.5)
    netflix_original = Movie("The lies of Thomas: How one kids show deceived millions by covering up a massive money laundering scandal.", 2.1)
    bad_movie = Movie("The Best Movie Ever Made!", 0.7)

    netflix_original.get_ticket_price()

    netflix = NetflixQueue()
    netflix.add_movie(shrek_2)
    netflix.add_movie(twilight)
    netflix.add_movie(despicable_me)
    netflix.add_movie(netflix_original)
    netflix.add_movie(bad_movie)
    netflix.print_movies()
    netflix.sort_movies_by_rating()
    netflix.get_movie(1)
    print("The best movie is ", netflix.get_best_movie().to_string())
    print("The second best movie is ", netflix.get_movie(1).to_string())
