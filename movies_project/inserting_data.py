import sqlite3
import csv



con = sqlite3.connect('test_1.db')

cur = con.cursor()

query_1 = 'INSERT INTO movies (movie_id, movie_name, released, duration, genre, budget, winner, open_week_us,' \
          ' gross_us, gross_world) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

query_2 = 'INSERT INTO  people (people_id, name, birthdate, interviews, articles, pictorials, ' \
          ' magazines) VALUES (?, ?, ?, ?, ?, ?, ?)'

query_3 = 'INSERT INTO movie_people (movie_id, people_id, role) VALUES (?, ?, ?)'
query_4 = 'INSERT INTO  movie_languages(movie_id, language_name) VALUES (?, ?)'
query_5 = 'INSERT INTO  movie_critics(movie_id, critic_id, score) VALUES (?, ?, ?)'
query_6 = 'INSERT INTO  critics (critic_id, critic_name) VALUES (?, ?)'
query_7 = 'INSERT INTO  movie_ratings( movie_id, source, rate) VALUES (?, ?, ?)'
query_8 = 'INSERT INTO  movie_country(movie_id, country_name) VALUES (?, ?)'
query_9 = 'INSERT INTO  movie_imbd_rating(movie_id, voters, rating_wa, rating_av, rating_median, rating_male, ' \
          'rating_female) VALUES (?, ?, ?, ?, ?, ?, ?)'
query_10 = 'INSERT INTO  movie_companies(movie_id, company_name, company_role) VALUES (?, ?, ?)'


with open('scrapped_data.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # generate sql insert query and execute it
        if not row:
            print("Empty row")
            continue
        print(row['movie_id'])
        print(row['movie_name'])

        cur.execute(query_1, (row['movie_id'], row['movie_name'], row['released'], row['duration'], row['genre'],
                              row['budget'], row['winner'], row['open_week_us'],  row['gross_us'], row['gross_world']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_2, (row['people_id'], row['name'], row['birthdate'], row['interviews'],
                              row['articles'], row['pictorials'], row['magazines']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_3, (row['movie_id'], row['people_id'], row['role']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_4, (row['movie_id'], row['language_name']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_5, (row['movie_id'], row['critic_id'], row['score']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_6, (row['critic_id'], row['critic_name']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_7, (row['movie_id'], row['source'], row['rate']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_8, (row['movie_id'], row['country_name']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_9, (row['movie_id'], row['voters'], row['rating_wa'], row['rating_av'], row['rating_median'], row['rating_male'], row['rating_female']))
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute(query_10, (row['movie_id'], row['company_name'], row['company_role']))
        cur.execute("PRAGMA foreign_keys = ON")

con.commit()
con.close()
