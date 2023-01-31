import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("ACDC")
artist_repository.save(artist_1)

album_1 = Album("Thunderstruck", "Rock", artist_1)
album_repository.save(album_1)
album_2 = Album("Highway to Hell", "Rock", artist_1)
album_repository.save(album_2)


results = artist_repository.albums(artist_1)

pdb.set_trace()

