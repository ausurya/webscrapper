import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.gstguide.com/gst-circular/IGST/10?classification_id=0&year=#"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

table1 = soup.find("table", class_ = "table table-bordered")
headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
mydata = pd.DataFrame(columns=headers)
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

mydata.to_csv("gst_circular.csv")
