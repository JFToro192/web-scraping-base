import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the webpage
url = 'https://webscraper.io/test-sites/e-commerce/allinone'
response = requests.get(url)



# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})

data = []

for item in items:
    img = item.find('img')
    if img is not None:
        src = img.get('src')
    title = item.find(class_='title') 
    price = item.find(class_='price')
    description = item.find(class_='description')

    data.append({
        # 'html': item,
        'name': title.text,
        'img_src': src,
        'price': price.text,
        'description': description.text
    })

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('./outputs/data.csv', index=False)