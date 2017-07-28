# import libraries
import csv
import requests
from BeautifulSoup import BeautifulSoup

# these are the unique suffixes 
letters = ["", "m2", "s2"]

# appends the rest of the letters of the alphabet
def letter_list(start, stop):
  for c in range(ord(start),ord(stop)+1):
    letters.append(chr(c))

# calls the function running from b through z    
letter_list('b', 'z')

# this is the url of the site
site = 'http://gov.texas.gov/music/musicians/talent/talent'

# opens the file with a new write command
outfile = open("./music2.csv", "wb")
# loop that appends letter to scrape each page
for letter in letters:
    url = site + letter
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find('div', attrs={'class': 'wrapper'})

    list_of_rows = []

# loop that goes through each row
    for row in table.findAll('tr'):
        list_of_cells = []
# loop that goes through each cell and finds text
        for cell in row.findAll('td'):
            text = cell.text
            list_of_cells.append(text.encode('utf-8'))
        list_of_rows.append(list_of_cells)
# writes the data to music.csv,uses ab not wb
    outfile = open("./music2.csv", "ab")
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)
