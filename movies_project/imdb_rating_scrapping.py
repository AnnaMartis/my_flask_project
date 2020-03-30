from bs4 import BeautifulSoup  # pip install beautifulsoup4 # pip install lxml
import requests  # pip install requests
import csv
import sqlite3


con = sqlite3.connect('my_project_new.db')
cur = con.cursor()

step = 1
url = ('https://www.imdb.com/search/title/?title_type=feature&'
       'release_date=2000-01-01,2002-12-31&user_rating=1.0,&sort=year,asc&start={}&count=200')

url_cast = 'https://www.imdb.com/title/tt{}/fullcredits'



for page in range(0, step * 10, step):
    source = requests.get(url.format(801)).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup)
    imdb_table = {}
    if page == 1:
        break

    for film in soup.find_all('div', class_='lister-item-content'):
        title = film.h3.a.text
        idx = film.h3.a['href'].split('/')[2][2:]
        imdb_table["movie_id"]= idx

        film_open = f"https://www.imdb.com{film.h3.a['href']}"  # link
        print(film_open)
        film_open_source = requests.get(film_open).text  # opened, entered in
        # print(film_open_source)
        f_soup = BeautifulSoup(film_open_source, 'lxml')  # search
        if f_soup.find('div', class_="titleReviewBarItem"):
            met = f_soup.find('div', class_="titleReviewBarItem").text.strip().split("\n")
            meta_score = met[0]
            if meta_score.strip()=="Reviews":
                meta_score = "None"
        else:
            meta_score = "None"
        print(meta_score)
        # imdb_table[meta_score] = meta_score

        rate_open = f"https://www.imdb.com/{film.h3.a['href']}ratings"
        print(rate_open)
        rate_open_source = requests.get(rate_open).text  # opened, entered in
        r_soup = BeautifulSoup(rate_open_source, 'lxml')  # search
        # print(r_soup)
        test = r_soup.find('div', class_="allText").text.strip().split("\n")
        # print(test)
        voters = test[0]
        print(voters)
        imdb_table["voters"]=voters
        weighted_av = test[1].strip().split("             ")
        wa = weighted_av[1].strip().split("/")
        rating_wa = wa[0]
        imdb_table["rating_wa"]=rating_wa
        print(rating_wa)
        if r_soup.find('div', {"align": "center"}).text.strip().split("\n"):
            med_whole = r_soup.find('div', {"align": "center"}).text.strip().split("\n")
            med_sep = med_whole[-1].strip()
            med = med_sep.split("=")
            median = med[1].strip()
            print(median)
        else:
            median = "None"
        imdb_table["rating_median"]= median
        male_whole = r_soup.findAll('div', class_="bigcell")
        rating_male = male_whole[5].text
        rating_woman = male_whole[10].text
        imdb_table["rating_female"] = rating_woman
        imdb_table["rating_male"] = rating_male
        print(rating_male)
        print(rating_woman)

        attrib_names = ", ".join(imdb_table.keys())
        print(attrib_names)
        attrib_values = ", ".join("?" * len(imdb_table.keys()))
        print(attrib_values)
        sql = f'INSERT OR REPLACE INTO movie_imbd_rating ({attrib_names}) VALUES ({attrib_values})'
        cur.execute(sql, list(imdb_table.values()))

        print(imdb_table)
        print("--------------")
con.commit()
con.close()











