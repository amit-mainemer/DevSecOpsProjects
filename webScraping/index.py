import requests
from bs4 import BeautifulSoup
import json


BASE_URL = "https://www.sport5.co.il/"

page = requests.get(BASE_URL)

soup = BeautifulSoup(page.content, "html.parser")

dataDict = {
    "מכבי": [],
    "הפועל": [],
    "ביתר": [],
    "בני": [],
    "יורוליג": [],
    "other": []
}

for item in soup.find_all("li"):
    for key in dataDict:
        if key in item.text:
            dataDict[key].append(item.text)
        else:
            dataDict["other"].append(item.text)

file = open("data.json", "w", encoding="utf-8")
file.write(json.dumps(dataDict,  ensure_ascii=False))
file.close()


print("html content was parsed. data.json created")