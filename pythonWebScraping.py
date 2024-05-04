import pandas 
from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
table_titles = soup.find_all('th')
table_titles_headers = [title.text.strip() for title in table_titles ]

df = pandas.DataFrame(columns = table_titles_headers)
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data ]

    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'C:\Users\dtrin\PythonOutput\python.csv', index = False)


#<table class="table">
                    
                  
