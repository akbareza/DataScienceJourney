import requests
from bs4 import BeautifulSoup

# Replace 'URL' with the actual URL of the page containing reviews
url = 'https://www.tokopedia.com/tagettocoffee/kopi-arabika-aceh-gayo-250gr-biji-bubuk-specialty-arabica-coffee-medium-roast-biji-kopi?extParam=ivf%3Dfalse%26src%3Dsearch'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')