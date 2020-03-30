from flask import Flask, url_for, render_template, request
from math import ceil
import sqlite3

PAGE_SIZE = 12
PAGE_SIZE_2 = 25
PAGE_SIZE_3 = 12


app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index.html')
@app.route('/genre/index.html')
@app.route('/movies/index.html')

def home():
    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sql = ('SELECT DISTINCT movie_imbd_rating.movie_id,movie_imbd_rating.voters, movies.released, movies.title, '
           'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
           'FROM movies LEFT JOIN movie_imbd_rating '
           'ON movie_imbd_rating.movie_id=movies.id '
           'ORDER BY movie_imbd_rating.voters DESC')

    exec = cur.execute(sql)
    print(exec)
    data = exec.fetchall()





    cur.close()
    return render_template("index.html", data=data)


@app.route('/list')
def list():
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

        # set detault to 1 if page is less than 1
    if page < 1:
        page = 1
    start = (page - 1) * PAGE_SIZE_2
    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    sql = ('SELECT DISTINCT movie_imbd_rating.movie_id, COUNT(*) max_count '
           'FROM movies INNER JOIN movie_imbd_rating '
           'ON movie_imbd_rating.movie_id=movies.id '
           'WHERE movies.genre="Action" OR movies.genre="Drama" OR movies.genre="Comedy"'
           'OR movies.genre="Romance" OR movies.genre="Sci-Fi" OR movies.genre="Adventure" '
           'OR movies.genre="Animation" OR movies.genre= "Biography" OR movies.genre="Crime"'
           'ORDER BY rating_wa')

    cur.execute(sql)
    max_count = cur.fetchone()['max_count']
    print(max_count)

    sql_2 = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.small_pic_url, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.genre="Action" OR movies.genre="Drama" OR movies.genre="Comedy" '
             'OR movies.genre="Romance" OR movies.genre="Sci-Fi" OR movies.genre="Adventure" '
             'OR movies.genre="Animation" OR movies.genre= "Biography" OR movies.genre="Crime" '
             'ORDER BY rating_wa DESC '
             f'LIMIT {PAGE_SIZE_2} OFFSET {start}')

    exec = cur.execute(sql_2)
    print(exec)
    data = exec.fetchall()
    print(data)
    page_count = ceil(max_count / PAGE_SIZE_2)
    print(page_count)


    sql_a = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "a%" AND movies.genre="Action" OR  movies.title LIKE "a%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "a%" AND movies.genre="Drama" OR  movies.title LIKE "a%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "a%" AND movies.genre="Romance" OR  movies.title LIKE "a%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "a%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "a%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "a%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')

    sql_b = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "b%" AND movies.genre="Action" OR  movies.title LIKE "b%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "b%" AND movies.genre="Drama" OR  movies.title LIKE "b%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "b%" AND movies.genre="Romance" OR  movies.title LIKE "b%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "b%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "b%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "b%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')

    sql_c = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "c%" AND movies.genre="Action" OR  movies.title LIKE "c%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "c%" AND movies.genre="Drama" OR  movies.title LIKE "c%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "c%" AND movies.genre="Romance" OR  movies.title LIKE "c%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "c%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "c%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "c%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_d = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "d%" AND movies.genre="Action" OR  movies.title LIKE "d%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "d%" AND movies.genre="Drama" OR  movies.title LIKE "d%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "d%" AND movies.genre="Romance" OR  movies.title LIKE "d%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "d%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "d%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "d%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_e = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "e%" AND movies.genre="Action" OR  movies.title LIKE "e%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "e%" AND movies.genre="Drama" OR  movies.title LIKE "e%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "e%" AND movies.genre="Romance" OR  movies.title LIKE "e%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "e%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "e%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "e%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_f = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "f%" AND movies.genre="Action" OR  movies.title LIKE "f%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "f%" AND movies.genre="Drama" OR  movies.title LIKE "f%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "f%" AND movies.genre="Romance" OR  movies.title LIKE "f%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "f%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "f%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "f%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_g = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "g%" AND movies.genre="Action" OR  movies.title LIKE "g%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "g%" AND movies.genre="Drama" OR  movies.title LIKE "g%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "g%" AND movies.genre="Romance" OR  movies.title LIKE "g%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "g%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "g%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "g%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_h = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "h%" AND movies.genre="Action" OR  movies.title LIKE "h%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "h%" AND movies.genre="Drama" OR  movies.title LIKE "h%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "h%" AND movies.genre="Romance" OR  movies.title LIKE "h%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "h%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "h%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "h%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_i = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "i%" AND movies.genre="Action" OR  movies.title LIKE "i%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "i%" AND movies.genre="Drama" OR  movies.title LIKE "i%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "i%" AND movies.genre="Romance" OR  movies.title LIKE "i%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "i%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "i%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "i%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_j = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "j%" AND movies.genre="Action" OR  movies.title LIKE "j%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "j%" AND movies.genre="Drama" OR  movies.title LIKE "j%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "j%" AND movies.genre="Romance" OR  movies.title LIKE "j%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "j%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "j%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "j%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_k = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "k%" AND movies.genre="Action" OR  movies.title LIKE "k%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "k%" AND movies.genre="Drama" OR  movies.title LIKE "k%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "k%" AND movies.genre="Romance" OR  movies.title LIKE "k%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "k%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "k%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "k%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_l = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "l%" AND movies.genre="Action" OR  movies.title LIKE "l%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "l%" AND movies.genre="Drama" OR  movies.title LIKE "l%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "l%" AND movies.genre="Romance" OR  movies.title LIKE "l%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "l%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "l%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "l%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_m = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "m%" AND movies.genre="Action" OR  movies.title LIKE "m%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "m%" AND movies.genre="Drama" OR  movies.title LIKE "m%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "m%" AND movies.genre="Romance" OR  movies.title LIKE "m%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "m%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "m%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "m%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_n = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "n%" AND movies.genre="Action" OR  movies.title LIKE "n%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "n%" AND movies.genre="Drama" OR  movies.title LIKE "n%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "n%" AND movies.genre="Romance" OR  movies.title LIKE "n%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "n%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "n%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "n%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_o = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "o%" AND movies.genre="Action" OR  movies.title LIKE "o%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "oa%" AND movies.genre="Drama" OR  movies.title LIKE "o%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "o%" AND movies.genre="Romance" OR  movies.title LIKE "o%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "o%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "o%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "o%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_p = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "p%" AND movies.genre="Action" OR  movies.title LIKE "p%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "p%" AND movies.genre="Drama" OR  movies.title LIKE "p%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "p%" AND movies.genre="Romance" OR  movies.title LIKE "p%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "p%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "p%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "p%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_q = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "q%" AND movies.genre="Action" OR  movies.title LIKE "q%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "q%" AND movies.genre="Drama" OR  movies.title LIKE "q%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "q%" AND movies.genre="Romance" OR  movies.title LIKE "q%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "q%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "q%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "q%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_s = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "s%" AND movies.genre="Action" OR  movies.title LIKE "s%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "s%" AND movies.genre="Drama" OR  movies.title LIKE "s%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "s%" AND movies.genre="Romance" OR  movies.title LIKE "s%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "s%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "s%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "s%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_r = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "r%" AND movies.genre="Action" OR  movies.title LIKE "r%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "r%" AND movies.genre="Drama" OR  movies.title LIKE "r%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "r%" AND movies.genre="Romance" OR  movies.title LIKE "r%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "r%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "r%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "r%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_t = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "t%" AND movies.genre="Action" OR  movies.title LIKE "t%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "t%" AND movies.genre="Drama" OR  movies.title LIKE "t%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "t%" AND movies.genre="Romance" OR  movies.title LIKE "t%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "t%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "t%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "t%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_u = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "u%" AND movies.genre="Action" OR  movies.title LIKE "u%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "u%" AND movies.genre="Drama" OR  movies.title LIKE "u%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "u%" AND movies.genre="Romance" OR  movies.title LIKE "u%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "u%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "u%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "u%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_v = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "v%" AND movies.genre="Action" OR  movies.title LIKE "v%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "v%" AND movies.genre="Drama" OR  movies.title LIKE "v%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "v%" AND movies.genre="Romance" OR  movies.title LIKE "v%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "v%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "v%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "v%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_w = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "w%" AND movies.genre="Action" OR  movies.title LIKE "w%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "w%" AND movies.genre="Drama" OR  movies.title LIKE "w%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "w%" AND movies.genre="Romance" OR  movies.title LIKE "w%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "w%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "w%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "w%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_x = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "x%" AND movies.genre="Action" OR  movies.title LIKE "x%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "x%" AND movies.genre="Drama" OR  movies.title LIKE "x%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "x%" AND movies.genre="Romance" OR  movies.title LIKE "x%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "x%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "x%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "x%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_y = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "y%" AND movies.genre="Action" OR  movies.title LIKE "y%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "y%" AND movies.genre="Drama" OR  movies.title LIKE "y%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "y%" AND movies.genre="Romance" OR  movies.title LIKE "y%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "y%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "y%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "y%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')
    sql_z = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
             'movie_imbd_rating.rating_wa, movies.country, movies.id, movies.genre '
             'FROM movies INNER JOIN movie_imbd_rating '
             'ON movie_imbd_rating.movie_id=movies.id '
             'WHERE movies.title LIKE "z%" AND movies.genre="Action" OR  movies.title LIKE "z%" AND movies.genre="Comedy"'
             'OR  movies.title LIKE "z%" AND movies.genre="Drama" OR  movies.title LIKE "z%" AND movies.genre="Animation"'
             'OR  movies.title LIKE "z%" AND movies.genre="Romance" OR  movies.title LIKE "z%" AND movies.genre="Crime"'
             'OR  movies.title LIKE "z%" AND movies.genre="Sci-Fi" OR  movies.title LIKE "z%" AND movies.genre="Biography"'
             'OR  movies.title LIKE "z%" AND movies.genre="Adventure" '
             'ORDER BY rating_wa DESC')


    a = cur.execute(sql_a)
    a_res= a.fetchall()
    b = cur.execute(sql_b)
    b_res= b.fetchall()
    c = cur.execute(sql_c)
    c_res= c.fetchall()
    d = cur.execute(sql_d)
    d_res= d.fetchall()
    e = cur.execute(sql_e)
    e_res= e.fetchall()
    f = cur.execute(sql_f)
    f_res= f.fetchall()
    g = cur.execute(sql_g)
    g_res= g.fetchall()
    h = cur.execute(sql_h)
    h_res= h.fetchall()
    i = cur.execute(sql_i)
    i_res= i.fetchall()
    j = cur.execute(sql_j)
    j_res= j.fetchall()
    k = cur.execute(sql_k)
    k_res= k.fetchall()
    l = cur.execute(sql_l)
    l_res= l.fetchall()
    m = cur.execute(sql_m)
    m_res= m.fetchall()
    n = cur.execute(sql_n)
    n_res= n.fetchall()
    o = cur.execute(sql_o)
    o_res= o.fetchall()
    p = cur.execute(sql_p)
    p_res= p.fetchall()
    q = cur.execute(sql_q)
    q_res= q.fetchall()
    r = cur.execute(sql_r)
    r_res= r.fetchall()
    s = cur.execute(sql_s)
    s_res= s.fetchall()
    t = cur.execute(sql_t)
    t_res= t.fetchall()
    u = cur.execute(sql_u)
    u_res= u.fetchall()
    v = cur.execute(sql_v)
    v_res= v.fetchall()
    w = cur.execute(sql_w)
    w_res= w.fetchall()
    x = cur.execute(sql_x)
    x_res= x.fetchall()
    y = cur.execute(sql_y)
    y_res= y.fetchall()
    z = cur.execute(sql_z)
    z_res= z.fetchall()



    # print(a_res)
    # print(len(a_res))
    cur.close()
    return render_template('list.html', data=data, page=page, page_count=page_count,
                           page_size=PAGE_SIZE_2, max_count=max_count, a_res=a_res, b_res=b_res,  c_res=c_res,
                           d_res=d_res, e_res=e_res, f_res=f_res, g_res=g_res, h_res=h_res,
                           i_res=i_res, j_res=j_res, k_res=k_res, l_res=l_res, m_res=m_res,
                           n_res = n_res, o_res = o_res, p_res = p_res, q_res = q_res, r_res = r_res,
                           s_res=s_res, t_res=t_res, u_res=u_res, v_res=v_res, w_res=w_res,
                           x_res=x_res, y_res=y_res, z_res=z_res)


@app.route('/celebs')
def celebs():
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

        # set detault to 1 if page is less than 1
    if page < 1:
        page = 1
    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sql_1 = ('SELECT count(people_id) max_count FROM people '
             'WHERE prof LIKE "%Actor%" ')


    f = cur.execute(sql_1)
    # print(f)
    max_count = f.fetchone()['max_count']
    # print(max_count)

    sql_2 = ('SELECT * FROM people '
             'WHERE prof LIKE "%Actor%"  '
             'ORDER BY name '
             'LIMIT {}, {}'.format((page - 1) * PAGE_SIZE_3, PAGE_SIZE_3))

    s = cur.execute(sql_2)
    # print(s)
    resAll = s.fetchall()
    # print(resAll)

    page_count_1 = ceil(max_count / PAGE_SIZE_3)
    # print(page_count)

    sql_3 = ('SELECT count(people_id) max_count FROM people '
             'WHERE prof LIKE "%Producer%" ')


    p = cur.execute(sql_3)
    max_count_2 = p.fetchone()['max_count']
    # print(max_count_2)

    sql_4 = ('SELECT * FROM people '
             'WHERE prof LIKE "%Producer%"  '
             'ORDER BY name '
             'LIMIT {}, {}'.format((page - 1) * PAGE_SIZE_3, PAGE_SIZE_3))

    ps = cur.execute(sql_4)
    # print(s)
    resAll_2 = ps.fetchall()
    # print(resAll)


    sql_5 = ('SELECT count(people_id) max_count FROM people '
             'WHERE prof LIKE "%Writer%" ')


    p_3 = cur.execute(sql_5)
    max_count_3 = p_3.fetchone()['max_count']
    # print(max_count_3)

    sql_6 = ('SELECT * FROM people '
             'WHERE prof LIKE "%Writer%"  '
             'ORDER BY name '
             'LIMIT {}, {}'.format((page - 1) * PAGE_SIZE_3, PAGE_SIZE_3))

    ps_3 = cur.execute(sql_6)
    resAll_3 = ps_3.fetchall()
    # print(resAll_3)

    sql_7 = ('SELECT count(people_id) max_count FROM people '
             'WHERE prof LIKE "%Director%" ')


    p_4 = cur.execute(sql_7)
    max_count_4 = p_4.fetchone()['max_count']

    sql_8 = ('SELECT * FROM people '
             'WHERE prof LIKE "%Director%"  '
             'ORDER BY name '
             'LIMIT {}, {}'.format((page - 1) * PAGE_SIZE_3, PAGE_SIZE_3))

    ps_4 = cur.execute(sql_8)
    resAll_4 = ps_4.fetchall()
    # print(resAll_4)

    return render_template("celebs.html", f=cur, page_count_1=page_count_1, page_size=PAGE_SIZE_3,
                           page=page,  resAll=resAll, resAll_2=resAll_2, resAll_3=resAll_3, max_count_3=max_count_3,
                           max_count_2=max_count_2, max_count_4=max_count_4, resAll_4=resAll_4)


@app.route('/genre/<genre_type>')
def genre_type(genre_type):
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

        # set detault to 1 if page is less than 1
    if page < 1:
        page = 1

    original_query = request.args.get('query', '')

    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    sql = ('SELECT count(ID) max_count FROM movies '
           'WHERE genre = (?) AND small_pic_url LIKE "%http%" ')

    f = cur.execute(sql, (genre_type,))
    # print(f)
    max_count = f.fetchone()['max_count']
    print(max_count)

    sql_2 = ('SELECT * FROM movies '
             'WHERE genre = (?) AND small_pic_url LIKE "%http%" '
             'LIMIT {}, {}'.format((page - 1) * PAGE_SIZE, PAGE_SIZE))

    s= cur.execute(sql_2,(genre_type,))
    # print(s)
    resAll = s.fetchall()
    print(resAll)

    page_count = ceil(max_count / PAGE_SIZE)
    # print(page_count)

    cur.close()
    return render_template('action.html', data=cur, page_count=page_count, page_size=PAGE_SIZE,
                           page=page, query=original_query, resAll=resAll)

@app.route('/country/<country>')
def country(country):
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

        # set detault to 1 if page is less than 1
    if page < 1:
        page = 1

    original_query = request.args.get('query', '')

    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    sql = ('SELECT count(ID) max_count FROM movies '
           'WHERE country = (?) AND small_pic_url LIKE "%http%" ')

    f = cur.execute(sql, (country,))
    # print(f)
    max_count = f.fetchone()['max_count']
    print(max_count)

    sql_2 = ('SELECT * FROM movies '
             'WHERE country = (?) AND small_pic_url LIKE "%http%" '
             'LIMIT {}, {}'.format((page - 1) * PAGE_SIZE, PAGE_SIZE))

    s= cur.execute(sql_2, (country,))
    print(s)
    resAll = s.fetchall()
    print(resAll)

    page_count = ceil(max_count / PAGE_SIZE)
    print(page_count)

    cur.close()
    return render_template('action.html', data=cur, page_count=page_count, page_size=PAGE_SIZE,
                           page=page, query=original_query, resAll=resAll)

@app.route('/movies/<id>')
def movie_single(id):
    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sql_movie = ('SELECT DISTINCT movie_imbd_rating.movie_id, movies.released, movies.title, '
                 'movie_imbd_rating.rating_wa, movie_imbd_rating.voters, movies.country, movies.id, movies.genre,'
                 'movies.small_pic_url,  movie_imbd_rating.rating_median,'
                 'movie_imbd_rating.rating_male, movies.language, movie_imbd_rating.rating_female,'
                 'movies.budget, movies.description, movies.duration, movies.open_week_us, '
                 'movies.gross_usa, movies.gross_world '
                 'FROM movies INNER JOIN movie_imbd_rating '
                 'ON movie_imbd_rating.movie_id=movies.id '
                 'WHERE movies.id =(?)')

    sql_people = ('SELECT DISTINCT movie_people.movie_id, people.people_id, people.name, '
                  'people.pic_url, movie_people.role '
                  'FROM movie_people '
                  'INNER JOIN people ON movie_people.people_id = people.people_id '
                  'WHERE movie_people.movie_id = (?)')

    sql_company = ('SELECT DISTINCT company_name FROM movie_companies '
                   'WHERE movie_id =(?)')

    cur.execute(sql_movie, (id,))
    data = cur.fetchone()
    # print(data)
    cur.execute(sql_people, (id,))
    people = cur.fetchall()
    print(id)
    print(people)
    cur.execute(sql_company, (id,))
    companies = cur.fetchall()
    cur.close()
    return render_template('movie_single.html', data=data, people=people, companies=companies)


@app.route('/person/<person_id>')
def person(person_id):
    con = sqlite3.connect('my_project_new.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sql_people = ('SELECT DISTINCT people.people_id, people.name, people.birthdate, people.interviews, '
                  'people.articles, people.pictorials, people.pic_url, people.magazines, '
                  'people.prof, movie_people.movie_id  '
                  'FROM people '
                  'INNER JOIN movie_people ON people.people_id = movie_people.people_id '
                  'WHERE people.people_id = ?')

    sql_movie = ('SELECT DISTINCT movie_people.movie_id,  movies.title, '
                 'movies.small_pic_url, movies.released, movie_imbd_rating.rating_wa '
                 'From movie_people '
                 'LEFT JOIN movies ON movie_people.movie_id = movies.id '
                 'LEFT JOIN movie_imbd_rating ON movie_people.movie_id = movie_imbd_rating.movie_id '
                 'WHERE movie_people.people_id =(?) ORDER BY movies.released DESC ')

    cur.execute(sql_people, (person_id,))
    person = cur.fetchone()
    print(person)

    cur.execute(sql_movie, (person_id,))
    movies = cur.fetchall()




    cur.close()
    return render_template('celeb_single.html', person=person, movies=movies)



if __name__=="__main__":
    app.run(debug=True)


