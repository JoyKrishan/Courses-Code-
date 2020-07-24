import sqlite3
import xml.etree.ElementTree as ET

conn=sqlite3.connect('My_Music.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER);
CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    len INTEGER, rating INTEGER, count INTEGER,
    album_id INTEGER,
    genre_id INTEGER)''')

Fname=input('Enter the File name-\n')
words=Fname.split('.')
extension=words[1]
if extension == 'xml':
    file=open(Fname)
else:
    print('Enter the Correct File')

#def the lookup function to find the names and keys
#<key>Track ID</key><integer>369</integer>
#<key>Name</key><string>Another One Bites The Dust</string>
#<key>Artist</key><string>Queen</string>
def lookup(entry, d):
    found= False
    for child in entry:
        if found:
            return child.text
        elif child.tag=='key' and child.text==d:
            found=True
    return None

tree=ET.parse(Fname)
all=tree.findall('dict/dict/dict')
print('Dict Count:', len(all))

for entry in all:
    if lookup(entry, 'Track ID') is None: continue
    Track=lookup(entry, 'Name')
    Artist=lookup(entry, 'Artist')
    Album=lookup(entry, 'Album')
    Genre=lookup(entry, 'Genre')
    Length=lookup(entry, 'Total Time')
    Count=lookup(entry, 'Track Count')
    Rating=lookup(entry, 'Rating')
    if Track is None  or Artist is None or Album is None or Genre is None:
        continue
    print('TRACK:- ',Track, Artist, Album, Genre, Length, Count, Rating)

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(Artist,))
    cur.execute('SELECT id FROM Artist WHERE name= ?',(Artist,))
    artist_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (Genre,))
    cur.execute('SELECT id FROM Genre WHERE name= ?',(Genre, ))
    genre_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (Album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title=?',(Album,))
    album_id=cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Track (title, len, rating, count, album_id, genre_id) VALUES (?, ?, ?, ?, ?, ?)',(Track, Length, Rating,Count,album_id,genre_id))
    conn.commit()
