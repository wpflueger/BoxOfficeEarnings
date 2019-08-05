from bs4 import BeautifulSoup
import urllib.request
import datetime
import csv

# Get the current date
x = datetime.datetime.now()

# Scrape Box Office Mojo Web Page
url = "https://www.boxofficemojo.com/alltime/world/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")
bo_table = soup.find_all(
    'table')

A = []
B = []
C = []

# Convert table from webpage to lists of Title, Earnings, & Year
for row in bo_table[1].find_all("tr"):
    cells = row.find_all("td")
    if len(cells) == 9:
        A.append(cells[1].find(text=True))
        oldstr = cells[3].find(text=True)
        newstr = oldstr.replace('$', "")
        B.append(newstr)
        oldstr = cells[8].find(text=True)
        newstr = oldstr.replace('^', "")
        C.append(newstr)

# Convert Lists to single CSV file
Headings = ['Title', 'Earnings', 'Year']

movies = {}

date = str(x.month) + "-"+str(x.day)
csv_file = date+" boxoffice.csv"

rows = zip(A, B, C)

# Populate CSV file
with open(csv_file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(Headings)
    for row in rows:
        writer.writerow(row)
