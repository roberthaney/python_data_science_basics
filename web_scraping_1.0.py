from bs4 import BeautifulSoup 
import requests

url = "http://www.ibm.com"

data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

# find links
links = []
for link in soup.find_all('a', href=True):
	links.append(link.get('href'))

for link in links:
	print link

print "Number of links found", len(links)

# find image sources
for image in soup.find_all('img'):
	print image.get('src')

# scraping data from html tables
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data = requests.get(url).text

# create soup object
soup = BeautifulSoup(data, "html.parser")

# get all tables
tables = soup.find_all('table')

# isolate first table on page with find (although in this case only one)
table = soup.find('table')

# isolate table rows
for row in table.find_all('tr'):
	# get columns in rows as td elements
	cols = row.find_all('td')
	# find number of columns (all rows should have same number)
	col_no = len(cols)
	# print first column text
	print cols[0].string

print "Number of tables present", len(tables)
print "Number of columns in table", col_no
print tables[0].prettify()





