from bs4 import BeautifulSoup  # pip install beautifulsoup4 # pip install lxml
import requests  # pip install requests
import csv
import sqlite3



class AttributeError(Exception):
    pass

# csv_file = open('movies_2000_2002.csv', 'w', newline='', encoding="utf-8")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["ID", "Title", "Year", "Genre", "Duration","Budget", "Open week us", "Gross us", "Gross world",
#                      "Country", "Language", "Small_pic_url", "Large_pic_url"])

con = sqlite3.connect('my_project_new.db')
cur = con.cursor()

step = 1
url = ('https://www.imdb.com/search/title/?title_type=feature&'
       'release_date=2000-01-01,2002-12-31&user_rating=1.0,&sort=year,asc&start={}&count=200')

url_cast = 'https://www.imdb.com/title/tt{}/fullcredits'

# parsing idx +, name +, released +, duration +, genre +, budget+, open_week_us+, gross_us+, gross_world+,
# description, country, language

print("lets start!!!")

for page in range(0, step * 10, step):
    source = requests.get(url.format(801)).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup)
    movie_table = {}
    if page == 1:
        break

    for film in soup.find_all('div', class_='lister-item-content'):
        title = film.h3.a.text
        idx = film.h3.a['href'].split('/')[2][2:]

        # print(idx)
        # print(title)

        movie_table["ID"]= idx
        movie_table["Title"]=title
        # print(movie_table)

        film_open = f"https://www.imdb.com{film.h3.a['href']}"  # link
        film_open_source = requests.get(film_open).text  # opened, entered in
        # print(film_open_source)
        f_soup = BeautifulSoup(film_open_source, 'lxml')  # search
        # print(f_soup.prettify())
        # print("---------------")
        if f_soup.find('div', class_="poster"):
            soup_link = f_soup.find('div', class_="poster")
            # link = soup_link["loadlate"]
            # print(soup_link)
            link = soup_link.find('img')
            link_small=link["src"]
            movie_table["Small_pic_url"]= link_small
            # movie_table["Large_pic_url"]= link_large
        else:
            link_large ="None"
            link_small = "None"
            movie_table["Small_pic_url"]= link_small
            movie_table["Large_pic_url"]= link_large



        summary_open = f"https://www.imdb.com/{film.h3.a['href']}plotsummary"
        # print(summary_open)
        summary_open_source = requests.get(summary_open).text
        summary_soup = BeautifulSoup(summary_open_source, 'lxml')
        print(summary_soup.prettify())
        zebra_list = summary_soup.find('ul', class_="ipl-zebra-list")

        if zebra_list.text.split()[0:3]== ['It', 'looks', 'like']:
            description = "None"
            # print(description)
        else:
            description= zebra_list.text.strip().split("\n")[0]
            # print(description)
        movie_table["description"] = description

        res = f_soup.find('div', class_="title_wrapper")
        # print(res)
        year = res.h1.a.text
        # print(year)

        res_1 = f_soup.find('div', class_="subtext")
        if res_1.a:
            genre = res_1.a.text
        else:
            genre = "None"
        deep_res_1 = res_1.find('time')
        if not deep_res_1:
            duration = "None"
        else:
            duration = deep_res_1.text.strip()
        movie_table["duration"] = duration
        movie_table["released"] = year
        movie_table["genre"] = genre
        # print(movie_char)

        txt_block = f_soup.findAll('div', class_="txt-block")
        budget = []
        open_week_us = []
        gross_usa = []
        gross_world = []
        country = []
        language = []
        for i in txt_block:
            contain = i.text.strip().split(":")
            # print(contain)

            if contain[0]=="Budget":
                budg = contain[1].split("\n")[0].strip()
                budget.append(budg)
            else:
                budget.append("None")

            if contain[0]=="Opening Weekend USA":
                week_us = contain[1].split("\n")[0].strip()[:-1]
                open_week_us.append(week_us)
            else:
                open_week_us.append("None")

            if contain[0] == "Gross USA":
                 gross_us = contain[1].strip()
                 gross_usa.append(gross_us)
                 # print(gross_us)
            else:
                gross_usa.append("None")

            if contain[0] == "Cumulative Worldwide Gross":
                gross_w = contain[1].strip()
                gross_world.append(gross_w)
            else:
                gross_world.append("None")

            if contain[0] == "Country":
                countr = contain[1].strip()
                if "|" in countr:
                    countr = countr.split("\n")
                    for el in countr:
                        if el == "|":
                            countr.remove(el)
                    countr = " , ".join(countr)
                country.append(countr)
            else:
                country.append("None")

            if contain[0]=="Language":
                lang = (contain[1]).strip()
                if "|" in lang:
                    lang = lang.split("\n")
                    for el in lang:
                        if el == "|":
                            lang.remove(el)
                    lang = " , ".join(lang)
                language.append(lang)
            else:
                language.append("None")


        budget = list(set(budget))
        # print(budget)
        if len(budget)==1:
            budget = budget[0].strip()
            # print(budget)
        else:
            if budget[0]=="None":
                budget = budget[1].strip()
                # print(budget)
            else:
                budget = budget[0].strip()
                # print(budget)

        open_week_us = list(set(open_week_us))
        if len(open_week_us) == 1:
            open_week_us = open_week_us[0]
            # print(open_week_us)
        else:
            if open_week_us[0] == "None":
                open_week_us = open_week_us[1]
                # print(open_week_us)
            else:
                open_week_us = open_week_us[0]
                # print(open_week_us)

        gross_usa = list(set(gross_usa))
        if len(gross_usa) == 1:
            gross_usa = gross_usa[0]
            # print(gross_usa)
        else:
            if gross_usa[0] == "None":
                gross_usa = gross_usa[1]
                # print(gross_usa)
            else:
                gross_usa = gross_usa[0]
                # print(gross_usa)

        gross_world = list(set(gross_world))
        if len(gross_world) == 1:
            gross_world = gross_world[0]
            # print(gross_world)
        else:
            if gross_world[0] == "None":
                gross_world = gross_world[1]
                # print(gross_world)
            else:
                gross_world = gross_world[0]
                # print(gross_world)

        country = list(set(country))
        # print(budget)
        if len(country) == 1:
            country = country[0]
            print(country)
        else:
            if country[0] == "None":
                country = country[1]
                # print(country)
            else:
                country = country[0]
                # print(country)

        language = list(set(language))
        # print(budget)
        if len(language) == 1:
            language = language[0]
        else:
            if language[0] == "None":
                language = language[1]
            else:
                language = language[0]
                # print(language)

        movie_table["budget"] = budget
        movie_table["open_week_us"] = open_week_us
        movie_table["gross_usa"] = gross_usa
        movie_table["gross_world"] = gross_world
        movie_table["country"] = country
        movie_table["language"] = language

        attrib_names = ", ".join(movie_table.keys())
        print(attrib_names)
        attrib_values = ", ".join("?" * len(movie_table.keys()))

        print(attrib_values)
        sql = f'INSERT OR REPLACE INTO movies ({attrib_names}) VALUES ({attrib_values})'
        cur.execute(sql, list(movie_table.values()))

        print(movie_table)
        print("--------------")


        # csv_writer.writerow([idx, title, year, genre, duration, budget, open_week_us, gross_usa, gross_world, country,
        #                      language, link_small, link_large])  # , actor, actor_name_in_film
        #

con.commit()
# csv_file.close()
con.close()
