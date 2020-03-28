import bs4
from bs4 import BeautifulSoup
import os
import requests
import boto3

class country:
    name = ''
    totalCases = 0;
    totalDeaths = 0
    firstCase = ''
    
    def __init__(self, name, totalCases, totalDeaths, firstCase):
        self.name = name
        self.totalCases = totalCases
        self.totalDeaths = totalDeaths
        self.firstCase = firstCase

    def __str__(self):
        return (self.name + "\t cases: " + self.totalCases + "\t total deaths: " + self.totalDeaths)

#path of link
path = "https://www.worldometers.info/coronavirus/"
response = requests.get(path)
soup = bs4.BeautifulSoup(response.text, "lxml")

count = soup.find_all('div', class_='maincounter-number')
data = soup.find_all('div', class_='tab-content')

#save total global cases
totalCases = count[0].find('span').text
totalDeaths = count[1].find('span').text

newlist = data[2].find('tbody')

items = newlist.find_all('tr')

totalItems = len(items)

database = []

for item in items:
    list = item.find_all('td')
    name = list[0].text
    cases = list[1].text
    deaths = list[3].text
    firstDate = list[10].text
    count = country(name, cases, deaths, firstDate)
    database.append(count)

#write to file
try:
    os.remove("text.txt")
except:
    pass

f = open("text.txt", "a")

for data in database:
    try:
        f.write(data.__str__() + "\n")
        print(data)
    except:
        pass

f.close()
