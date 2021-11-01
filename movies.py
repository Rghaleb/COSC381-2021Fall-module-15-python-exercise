
class Movie():

    def __init__(self):
        self._movies = {}

    def add_movie(self, name, casts):
        self._movies[name] = casts

    def print_movies(self):
        print('{:<30}{}'.format('Movie Name','Cast'))
        print('-----------------------------------------------------')
        for name, cast in self._movies.items():
            print('{:<30}{}'.format(name, ', '.join(cast)))
        print('-----------------------------------------------------')

    def popular_letter(self):
        cast_names = ''
        for cast in self._movies.values():
            cast_names += ''.join(cast)
        cast_names = cast_names.lower()
        max_letter, max_count = 'a', 0
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            count = cast_names.count(letter)
            if count > max_count:
                max_letter, max_count = letter, count
        return max_letter, max_count