import os
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver = "/home/aditya/python/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.tourtravelworld.com/travel-agents/search.htm?catgcode=10324&srch_kword=jaipur")

for i in range(10):
    driver.find_element_by_xpath('//*[@id="load_more_label"]/a').click()



html = driver.page_source.encode('utf-8')


soup = BeautifulSoup(html, 'lxml')



spans = soup.find_all('span', {'itemprop' : 'Name'})
names = [span.get_text() for span in spans]

print(names)
print(len(names))

#  section = soup.find_all(class = "fo mb25px bsb5px25 bgfff ffos large bsb10px33-hover")


spans = soup.find_all('p', {'class' : "xxlarge dif b mb7px" })
number = [span.get_text() for span in spans]
print(number)


print(len(number))

for i,j in zip(names, number):
    print(i, j)



