from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
webpage = requests.get("https://en.wikipedia.org/wiki/Deaths_in_January_2024")
soup = BeautifulSoup(webpage.text, 'html.parser')
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Months and URLs
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

base_url = 'https://en.wikipedia.org/wiki/Deaths_in_{}_2024'

# Prepare list
all_data = []

for month in months:
    url = base_url.format(month)
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all list items
    uls = soup.find_all('ul')

    for ul in uls:
        lis = ul.find_all('li')
        for li in lis:
            text = li.get_text(separator=" ", strip=True)
            if ',' in text and any(char.isdigit() for char in text):
                parts = text.split(',')

                if len(parts) >= 3:
                    name = parts[0].strip()
                    age = parts[1].strip()
                    rest = ",".join(parts[2:]).strip()

                    if ',' in rest:
                        location_profession, cause_of_death = rest.rsplit(',', 1)
                        cause_of_death = cause_of_death.strip()
                    else:
                        location_profession = rest
                        cause_of_death = None

                    all_data.append({
                        'Name': name,
                        'Age': age,
                        'Location/Profession': location_profession.strip(),
                        'Cause of Death': cause_of_death,
                        'Month': month
                    })

# Convert to DataFrame
full_year_df = pd.DataFrame(all_data)

# Save to CSV
full_year_df.to_csv('deaths_2024_full_year.csv', index=False)

print("Scraping Completed!")
