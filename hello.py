from movies import Movie


def main():
    fav_movies = Movie()
    fav_movies.add_movie('Mountain Climber', ['Tom', 'Mary', 'Tim'])
    fav_movies.add_movie('Sea Diver', ['Tiffany', 'John', 'Eleanor'])

    fav_movies.print_movies()

    letter, count = fav_movies.popular_letter()

    print(f'The most popular letter is {letter} and occurs {count} times.')
    print(f'------------------------------------------------------------.')
    
main()

