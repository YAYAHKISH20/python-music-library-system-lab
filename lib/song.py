from typing import ClassVar


class Song:
    """A song in the MusicTech Innovations library.

    Instance attributes describe a single song, while the class attributes
    below track aggregate information about every Song ever created.
    """

    # Class attributes (shared by all instances)
    count: ClassVar[int] = 0
    genres: ClassVar[list[str]] = []
    artists: ClassVar[list[str]] = []
    genre_count: ClassVar[dict[str, int]] = {}
    artist_count: ClassVar[dict[str, int]] = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every new song updates the global stats
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list, keeping it unique."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list, keeping it unique."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Track how many songs belong to each genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Track how many songs each artist is responsible for."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


if __name__ == "__main__":
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Formation", "Beyonce", "Pop")

    print(Song.count)          # 3
    print(Song.genres)         # ['Rap', 'Pop']
    print(Song.artists)        # ['Jay-Z', 'Beyonce']
    print(Song.genre_count)    # {'Rap': 1, 'Pop': 2}
    print(Song.artist_count)   # {'Jay-Z': 1, 'Beyonce': 2}
