import requests
from bs4 import BeautifulSoup
import csv

url = "https://everymac.com/systems/apple/ipad/index-ipad-specs.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract iPad models and specs
ipad_data = []
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 1:  # Skip rows without data
        model = columns[0].get_text().strip()
        release_info = columns[1].get_text().strip()
        ipad_data.append({"Model": model, "Release Info": release_info})

# Write to CSV
with open('ipad_models.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=["Model", "Release Info"])
    writer.writeheader()
    writer.writerows(ipad_data)

print("Data written to ipad_models.csv")
