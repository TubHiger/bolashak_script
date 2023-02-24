import requests
from bs4 import BeautifulSoup
import pandas as pd


# Get the HTML page
url = "https://bolashak.gov.kz/en/pretendentu/vuzy"
response = requests.get(url)
html = response.content


# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")


# Find all divs with class "vuzblock"
vuzblocks = soup.find_all("div", {"class": "vuzblock"})


# Create a list of dictionaries containing the data
data = []
for vuzblock in vuzblocks:
   item = {}
   for span in vuzblock.find_all("span"):
       item[vuzblock.find("p").text.strip()] = span.text.strip()
   data.append(item)

# Create a DataFrame from the data and save it to an Excel file
df = pd.DataFrame(data)
df.to_excel("vuzblocks.xlsx", index=False)