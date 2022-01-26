class Artist:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__(self, name=None, birth_year=0, death_year=0):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    # TODO: Define print_info() method. If death_year is -1, only print birth_year
    def print_info(self):
        if self.death_year == -1:
            return 'Artist: {}, born {}'.format(self.name, self.birth_year)
        else:
            return 'Artist: {} ({}-{})'.format(self.name, self.birth_year, self.death_year)


class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    def __init__(self, title=None, year_created=0, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    # TODO: Define print_info() method
    def print_info(self):
        return 'Title: {}, {}'.format(self.title, self.year_created)


if __name__ == "__main__":
    user_artist_name = 'Brice Marden'
    user_birth_year = 1938
    user_death_year = -1
    user_title = 'Distant Muses'
    user_year_created = 2000

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    print(user_artist.print_info())
    print(new_artwork.print_info())
