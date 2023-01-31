from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(
            row['artist_name'],
            row['id']
        )
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['artist_name'], result['id'])
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE from artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):

    sql = "UPDATE artists SET (artist_name) = (%s) WHERE id = %s"
    values = [
        artist.artist_name,
        ]
    run_sql(sql, values)

def albums(artist):
    albums = []
    sql = "SELECT * from albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(
            row['title'],
            row['genre'],
            artist,
            row['id']
        )
        albums.append(album)
    return albums
