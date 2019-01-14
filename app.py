# coding=utf-8

import time
import io
import sys
from selenium import webdriver
from bs4 import BeautifulSoup, Comment
import pandas
from tabulate import tabulate


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
driver = webdriver.Chrome()
driver.get("https://tw.buy.yahoo.com/")


element = driver.find_element_by_class_name("billboardbox")
element.location_once_scrolled_into_view
time.sleep(5)
element = driver.find_element_by_class_name("about")
element.location_once_scrolled_into_view


soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

# Get catagory name
catagory = soup.find("h2", text = "排行榜").find_next().findChildren()[0].text
print("排行類別: ", catagory)

l = []
index = 1

elements = soup.find_all("div", {"class":"rank"})
for element in elements:
  d = {}
  d["Ranking"] = index
  d["Price"] = element.find_next().find_next().find("span", {"class":"shpprice"}).text
  d["Description"] = element.find_next().text
  # d["Link"] = element.parent["href"]
  print(index, element.parent)

  index = index + 1
  l.append(d)

df = pandas.DataFrame(l)
print(tabulate(df, headers='keys', tablefmt='psql'))
df.to_csv('output.csv')
