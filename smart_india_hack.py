from bs4 import BeautifulSoup
import requests

urls = ["https://innovate.mygov.in/sih2018/", "https://innovate.mygov.in/sih2018/?filter=state", "https://innovate.mygov.in/sih2018/?filter=sector", "https://innovate.mygov.in/sih2018/?filter=student"]
for url in urls:
#  url = "https://innovate.mygov.in/sih2018/"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "lxml")
    links = soup.find_all('h3')
#  print(links)
    ministries = []
    for ministry_link in soup.find_all('h3'):
        ministries.append(ministry_link.find("a")['href'])

#  ministries = ["https://innovate.mygov.in/ministry_state/aicte/"]
    for page in ministries:
        pageData = requests.get(page)
        pageObj = BeautifulSoup(pageData.text, "lxml")
        for problem in pageObj.find_all('article', class_="category-listing"):
            print(pageObj.find('div', class_="search-by").text )
            print(problem.find('div',class_="problem-id").find('a').text.lstrip())
            print("Problem Statement : " , problem.find('a').text)
            print('\n')
            print("Problem Description : " )
            print(problem.find('div',class_="description").p.text)
            print('\n')
            print("-------------------------------------------------------------------------------------------------------------------")
            print('\n')




