import requests
from bs4 import BeautifulSoup as bs
import time

start_time = time.time()


pages = ()

for page_num in range(1, 96):
    url_start = 'https://www.centralcharts.com/en/price-list-ranking/'
    url_end = 'ALL/asc/ts_29-us-nyse-stocks--qc_1-alphabetical-order?p='
    url = url_start + url_end + str(page_num)
    pages = pages + (url,)

valueslist = []
for page in pages:
    response = requests.get(page)
    soup = bs(response.text, 'html.parser')

    table = soup.find('table',class_='tabMini tabQuotes')
    rows = table.find_all('tr')

    for row in rows[1:]:
        cells = row.find_all('td')
        
        row_values = []
        for cell in cells[0:7]:
            new_value = cell.text.strip()
            row_values.append(new_value)
        valueslist.append(row_values)

print(valueslist)
print("--- %s seconds ---" % (time.time() - start_time))


