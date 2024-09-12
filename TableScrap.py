import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="table table-sm table-hover screenertable")

# Extract headers
headers = table.find_all("th")
titles = [header.text.strip() for header in headers]

# Initialize DataFrame with column headers
df = pd.DataFrame(columns=titles)

# Extract rows
rows = table.find_all("tr")

# Loop through each row (skipping the header row)
for row in rows[1:]:
    # Find all <td> elements in this row
    data = row.find_all("td")

    # Extract the text from each <td> and store it in a list
    row_data = [td.text.strip() for td in data]

    # Append the row data to the DataFrame
    df.loc[len(df)] = row_data

# Print the final DataFrame
print(df)

# Optionally, save the DataFrame to an Excel file
df.to_excel("stock_data.xlsx")
