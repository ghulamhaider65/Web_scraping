# Deaths in 2024 - Wikipedia Scraper

## 📚 About the Project

This project scrapes publicly available death records for the year 2024 from Wikipedia, month by month, and organizes the data into a structured CSV file.  
**Main Goal:**  
- Build a real-world dataset to practice **data cleaning**, **data wrangling**, and **NLP tasks**.

Wikipedia pages scraped:  
- `https://en.wikipedia.org/wiki/Deaths_in_January_2024`
- `https://en.wikipedia.org/wiki/Deaths_in_February_2024`
- ...
- `https://en.wikipedia.org/wiki/Deaths_in_December_2024`

**⚡ Why?**  
Most tutorial datasets are too "perfect". Real-world data is messy. This project gives you actual messy, imperfect data — just like you'll deal with in real projects.

---

## 🛠️ How It Works

- Loops through all 12 months of 2024.
- Sends a request to each Wikipedia page.
- Parses the page with `BeautifulSoup`.
- Extracts important information from list items:
  - **Name** (of the deceased)
  - **Age**
  - **Location/Profession**
  - **Cause of Death** (if available)
  - **Month** (for time-based analysis)
- Saves everything to a clean CSV file:  
  `deaths_2024_full_year.csv`

---

## 🧰 Tech Stack

- Python 3.x
- Libraries:
  - `requests`
  - `BeautifulSoup` (`bs4`)
  - `pandas`

---

## 📂 Output Example

| Name         | Age | Location/Profession         | Cause of Death          | Month    |
|--------------|-----|------------------------------|--------------------------|----------|
| John Doe     | 78  | American actor and producer  | Heart attack             | January  |
| Jane Smith   | 85  | British politician           | Natural causes           | March    |
| ...          | ... | ...                          | ...                      | ...      |

*Note: Some records may not have a clear "cause of death". That's real life — messy data.*

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Install required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
