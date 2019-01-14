# coding=utf-8

import time
import io
import sys
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup, Comment
import pandas
from tabulate import tabulate


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
base_url = "https://tw.buy.yahoo.com"

# Access the site and scraping elements
driver = webdriver.Chrome()
driver.get(base_url)


element = driver.find_element_by_class_name("billboardbox")
element.location_once_scrolled_into_view
time.sleep(5)
element = driver.find_element_by_class_name("about")
element.location_once_scrolled_into_view


# Parsing elements
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

# Get category name
try:
    category = soup.find("h2", text="排行榜").find_next().findChildren()[0].text
except AttributeError:
    category = None

# Get access datettime
timestr = datetime.now().strftime("%Y%m%d-%H%M")

# Create list of products
l = []
index = 1

# Iterate through the products
elements = soup.find_all("div", {"class": "rank"})
for element in elements:
    d = {}
    d["Ranking"] = index
    d["Price"] = element.find_next().find_next().find(
        "span", {"class": "shpprice"}).text
    d["Description"] = element.find_next().text
    if (index == 1):
        d["Link"] = base_url + element.parent["href"]
    else:
        d["Link"] = base_url + element.parent.parent["href"]

    index = index + 1
    l.append(d)

# Load to PANDAS DataFrame object
df = pandas.DataFrame(l)

# Output results for console
print("Current best selling products for", category + ":")
print(tabulate(df, headers="keys", tablefmt="psql"))

# Prompt user input and create files accordingly
inputstr = input(
    "Enter 1 to save as csv. \nEnter 2 to save as excel. \nEnter any other key to quit without saving.\n")
if inputstr == "1":
    print("Saving csv to output/output_" + category + "_" + timestr + ".csv")
    df.to_csv("output/output_" + category + "_" + timestr + ".csv")
elif inputstr == "2":
    print("Saving csv to output/output_" + category + "_" + timestr + ".xlsx")
    writer = pandas.ExcelWriter(
        "output/output_" + category.replace("/", "").replace("\\", "") + "_" + timestr + ".xlsx")
    df.to_excel(writer, "Sheet1")
    writer.save()
