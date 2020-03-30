from bs4 import BeautifulSoup  # pip install beautifulsoup4 # pip install lxml
import requests  # pip install requests
import csv
import sqlite3

con = sqlite3.connect('my_project_new.db')
cur = con.cursor()

step = 1
url = ('https://www.imdb.com/search/title/?title_type=feature&'
       'release_date=2000-01-01,2002-12-31&user_rating=1.0,&sort=year,asc&start={}&count=20')


for page in range(0, step * 10, step):
    print(page)
    source = requests.get(url.format(221)).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup)
    people_table = {}

    if page ==1: break
    r_page = 0

    for film in soup.find_all('div', class_='lister-item-content'):
        r_page += 1
        print(r_page)
        title = film.h3.a.text
        movie_id = film.h3.a['href'].split('/')[2][2:]

        full_cast_open = f"https://www.imdb.com{film.h3.a['href']}fullcredits"
        # print(full_cast_open)
        cast_open_source = requests.get(full_cast_open).text
        c_soup = BeautifulSoup(cast_open_source, 'lxml')
        # print(c_soup)

        result_0 = c_soup.find_all('td', class_="name")
        count = 0
        for child_0 in result_0:
            count += 1
            # print(count)
            if count == 20: break
            lk = child_0.a['href']
            people_id = lk.split('/')[2][2:]
            print(people_id)


            person_open = f"https://www.imdb.com{lk}"
            print(person_open)
            person_open_source = requests.get(person_open).text
            p_soup = BeautifulSoup(person_open_source, 'lxml')
            # print(p_soup)
            # print("--------------")
            people_table["people_id"]=people_id
            if p_soup.find('a', class_="top100"):
                star_meter = p_soup.find('a', class_="top100").text.strip()
            else:
                star_meter = "None"
            people_table["star_meter"] = star_meter

            role_s = p_soup.find('div', class_="infobar").text.strip().split("\n")
            if len(role_s)==1:
                prof = role_s[0]
            else:
                mlist = []
                for item in role_s:
                    if item == ' ':
                        role_s.remove(item)
                # print(role_s)
                for i in role_s:
                    # print(i)
                    pr = i.strip().split(" ")
                    k = pr[0]
                    mlist.append(k)
                prof = " , ".join(mlist)
                # print(prof)
            people_table["prof"] = prof

            title = p_soup.find('title').text.strip().split("-")
            name = title[0]
            print(name)
            people_table["name"]=name
            soup_link = p_soup.find('div', class_="image")
            # print(soup_link)
            if soup_link.find('img'):
                link = soup_link.find('img')
                # print(link)
                link_small = link["src"]
                people_table["pic_url"] = link_small
            else:
                link_small = "https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB470041852_.png"
                people_table["pic_url"] = link_small
            if link_small=="https://m.media-amazon.com/images/M/MV5BNzJmNWQ5N2QtYWI5Yi00ODg0LTg0ODUtNWJjYzg5NWJhM2Y3XkEyXkFqcGdeQXVyODQxODMzNjQ@._CR8,468,660,494_UX614_UY460._SY230_SX307_AL_.jpg":
                link_small= "https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB470041852_.png"
            print(link_small)
            print(people_table)




            cl_0 = p_soup.findAll('div', class_="txt-block")
            # print(cl_0)
            for i in cl_0:
                # print(i)
                if i.find('time'):
                    date = i.find('time').text.strip().split("\n")
                    if len(date)==1:
                        birth_date = date[0]
                    else:

                        birth_date = f"{date[0]}{date[2]}"
                        break
                else:
                    continue
                people_table["birthdate"]= birth_date

            if p_soup.findAll('div', {"id": "details-publicity-listings"}):
                group = p_soup.findAll('div', {"id": "details-publicity-listings"})
                for child in group:
                    txt = child.text.strip().split("\n")
                    if len(txt) == 4:
                        interviews = "None"
                        articles = "None"
                        pictorials = "None"
                        magazines = "None"
                    else:
                        interviews = []
                        pictorials = []
                        articles = []
                        magazines = []
                        txt.pop(0)
                        txt.pop(-1)
                        txt.pop(-1)
                        txt.pop(-1)
                        for i in txt:
                            i = i.strip().split("     ")
                            i.remove("|")
                            for m in i:
                                m = m.strip().split(" ")
                                if m[1] == 'Interview' or m[1] == 'Interviews':
                                    interviews.append(m[0])
                                else:
                                    interviews.append("None")
                                    # print(interviews)
                                if m[1] == 'Article' or m[1] == 'Articles':
                                    articles.append(m[0])
                                else:
                                    articles.append("None")
                                if m[1] == 'Pictorial' or m[1] == 'Pictorials':
                                    pictorials.append(m[0])
                                else:
                                    pictorials.append("None")
                                if m[1] == 'Magazine' or m[1] == 'Magazines':
                                    magazines.append(m[0])
                                else:
                                    magazines.append("None")

                        interviews = list(set(interviews))
                        # print(interviews)
                        # print(len(interviews))
                        if len(interviews) == 1:
                            print("Yes")
                            interviews = interviews[0].strip()
                        else:
                            print("No")
                            if interviews[0] == "None":
                                interviews = interviews[1].strip()
                            else:
                                interviews = interviews[0].strip()

                        magazines = list(set(magazines))
                        if len(magazines) == 1:
                            magazines = magazines[0].strip()
                        else:
                            if magazines[0] == "None":
                                magazines = magazines[1].strip()
                            else:
                                magazines = magazines[0].strip()

                        articles = list(set(articles))
                        if len(articles) == 1:
                            articles = articles[0].strip()
                        else:
                            if articles[0] == "None":
                                articles = articles[1].strip()
                            else:
                                articles = articles[0].strip()

                        pictorials = list(set(pictorials))
                        if len(pictorials) == 1:
                            pictorials = pictorials[0].strip()
                        else:
                            if pictorials[0] == "None":
                                pictorials = pictorials[1].strip()
                            else:
                                pictorials = pictorials[0].strip()



            else:
                interviews = "None"
                articles = "None"
                pictorials = "None"
                magazines = "None"

            people_table["interviews"] = interviews
            people_table["articles"] = articles
            people_table["pictorials"] = pictorials
            people_table["magazines"] = magazines
            print(people_table)


            attrib_names = ", ".join(people_table.keys())
            attrib_values = ", ".join("?" * len(people_table.keys()))
            sql = f'INSERT OR REPLACE INTO people ({attrib_names}) VALUES ({attrib_values})'
            cur.execute(sql, list(people_table.values()))


con.commit()
con.close()


