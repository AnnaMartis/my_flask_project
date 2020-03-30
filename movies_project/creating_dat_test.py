import sqlite3
con = sqlite3.connect('my_test.db')

cur = con.cursor()

query_1 = ('CREATE TABLE IF NOT EXISTS movies ('
           'ID TEXT PRIMARY KEY, '
           'Title TEXT,'
           'released TEXT, '
           'duration INTEGER, '
           'genre TEXT, '
           'budget REAL, '
           'language TEXT, '
           'country TEXT, '
           'small_pic_url TEXT, '
           'large_pic_url TEXT, '
           'open_week_us REAL, '
           'gross_usa REAL, '
           'gross_world REAL)')

cur.execute(query_1)

query_2 = ('CREATE TABLE IF NOT EXISTS people ('
           'people_id TEXT PRIMARY KEY , '
           'name TEXT, '
           'birthdate TEXT, '
           'interviews TEXT, '
           'articles TEXT, '
           'pictorials TEXT, '
           'pic_url TEXT, '
           'star_meter INTEGER, '
           'prof INTEGER, '
           'magazines TEXT )')
cur.execute(query_2)

query_3 = ('CREATE TABLE IF NOT EXISTS movie_people ('
           'movie_id TEXT, '
           'people_id TEXT, '
           'role TEXT, '
           'FOREIGN KEY(movie_id) REFERENCES movies(movie_id)'
           'FOREIGN KEY(people_id) REFERENCES people(people_id))')

cur.execute(query_3)


query_4 = ('CREATE TABLE IF NOT EXISTS movie_imbd_rating ('
           'movie_id TEXT, '
           'voters INTEGER, '
           'rating_wa REAL, '
           'rating_av REAL, '
           'rating_median REAL, '
           'rating_male REAL, '
           'rating_female REAL,'
           'Metascore REAL,'
           'FOREIGN KEY(movie_id) REFERENCES movies(movie_id))')
cur.execute(query_4)

query_5 = ('CREATE TABLE IF NOT EXISTS movie_companies ('
           'movie_id TEXT, '
           'company_name TEXT, '
           'FOREIGN KEY(movie_id) REFERENCES movie(movie_id))')
cur.execute(query_5)



con.close()
