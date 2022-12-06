# Import the necessary libraries
from bs4 import BeautifulSoup
import requests

# Define the URL of the webpage you want to scrape
url = "http://www.gstguide.com/gst-faq"

# Make a request to the webpage to retrieve the HTML
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all text elements on the webpage
text_elements = soup.find_all(text=True)

# Print the text of each element
for text_element in text_elements:
    print(text_element.strip())

# tables = soup.find_all("table")

# for table in tables:
#     print(table.prettify())
