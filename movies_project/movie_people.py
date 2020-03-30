from bs4 import BeautifulSoup  # pip install beautifulsoup4 # pip install lxml
import requests  # pip install requests
import csv
import sqlite3

con = sqlite3.connect('my_project_new.db')
cur = con.cursor()

step = 1
url = ('https://www.imdb.com/search/title/?title_type=feature&'
       'release_date=2000-01-01,2002-12-31&user_rating=1.0,&sort=year,asc&start={}&count=200')


for page in range(0, step * 10, step):
    source = requests.get(url.format(801)).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup)
    movie_p_table = {}
    if page ==1: break

    for film in soup.find_all('div', class_='lister-item-content'):
        title = film.h3.a.text
        movie_id = film.h3.a['href'].split('/')[2][2:]
        movie_p_table["movie_id"]= movie_id

        full_cast_open = f"https://www.imdb.com{film.h3.a['href']}fullcredits"
        print(full_cast_open)
        cast_open_source = requests.get(full_cast_open).text
        c_soup = BeautifulSoup(cast_open_source, 'lxml')
        if c_soup.find("table", class_="simpleTable simpleCreditsTable"):
            tb = c_soup.findAll("table", class_="simpleTable simpleCreditsTable")
            directors = tb[0]
            od_d = directors.findAll('a')
            # print(od_d)
            for ch in od_d:
                people_id = ch["href"].split('/')[2][2:]
                movie_p_table["people_id"] = people_id
                # print(people_id)
                name = ch.text.strip()
                # print(name)
                role = "director"
                movie_p_table["role"] = role
                print(movie_p_table)
                attrib_names = ", ".join(movie_p_table.keys())
                attrib_values = ", ".join("?" * len(movie_p_table.keys()))
                sql = f'INSERT OR REPLACE INTO movie_people ({attrib_names}) VALUES ({attrib_values})'
                cur.execute(sql, list(movie_p_table.values()))

                if len(tb)==2:
                    writers = tb[1]
                    od_w = writers.findAll('a')
                    for ch_1 in od_w:
                        people_id = ch_1["href"].split('/')[2][2:]
                        # print(people_id)
                        movie_p_table["people_id"] = people_id
                        name = ch_1.text.strip()
                        # print(name)
                        role = "writer"
                        movie_p_table["role"] = role

                        print(movie_p_table)
                        attrib_names = ", ".join(movie_p_table.keys())
                        attrib_values = ", ".join("?" * len(movie_p_table.keys()))
                        sql = f'INSERT OR REPLACE INTO movie_people ({attrib_names}) VALUES ({attrib_values})'
                        cur.execute(sql, list(movie_p_table.values()))
                else:
                    continue

        else:
            continue

        if c_soup.find("table", class_="cast_list"):



            ac_soup = c_soup.find("table", class_="cast_list")
            # print(ac_soup)
            count = 0
            od_c = ac_soup.findAll('a')
            # print(len(od_c))
            for l in range(1, len(od_c), 2):
                child = od_c[l]
                count += 1
                if count == 15: break
                people_id = child["href"].split('/')[2][2:]
                movie_p_table["people_id"] = people_id
                # print(people_id)
                name = child.text.strip()
                # print(name)
                role = "actor/actress"
                movie_p_table["role"] = role

                print(movie_p_table)

                attrib_names = ", ".join(movie_p_table.keys())
                print(attrib_names)
                attrib_values = ", ".join("?" * len(movie_p_table.keys()))
                print(attrib_values)
                sql = f'INSERT OR REPLACE INTO movie_people ({attrib_names}) VALUES ({attrib_values})'
                cur.execute(sql, list(movie_p_table.values()))
con.commit()
con.close()














