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
    company_table = {}
    if page == 1:
        break

    for film in soup.find_all('div', class_='lister-item-content'):
        title = film.h3.a.text
        movie_id = film.h3.a['href'].split('/')[2][2:]
        company_table["movie_id"] = movie_id

        company_open = f"https://www.imdb.com{film.h3.a['href']}companycredits"
        company_open_source = requests.get(company_open).text
        c_soup =  BeautifulSoup(company_open_source, 'lxml')
        # print(c_soup)
        if c_soup.find('ul', class_="simpleList"):
            l_0= c_soup.find('ul', class_="simpleList")
            l_1 = l_0.findAll('a')
            print(l_1)
            for child in l_1:
                company_name = child.text
                company_table["company_name"] = company_name
                print(company_table)



                attrib_names = ", ".join(company_table.keys())
                attrib_values = ", ".join("?" * len(company_table.keys()))
                sql = f'INSERT OR REPLACE INTO movie_companies ({attrib_names}) VALUES ({attrib_values})'
                cur.execute(sql, list(company_table.values()))

        else:
            company_name = "None"
            company_table["company_name"] = company_name
            attrib_names = ", ".join(company_table.keys())
            attrib_values = ", ".join("?" * len(company_table.keys()))
            sql = f'INSERT OR REPLACE INTO movie_companies ({attrib_names}) VALUES ({attrib_values})'
            cur.execute(sql, list(company_table.values()))



con.commit()
con.close()
