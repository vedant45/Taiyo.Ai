import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self, url, table_columns):
        self.url = url
        self.table_columns = table_columns

    def scrape_data(self):
        tender_data = []
        df = pd.DataFrame(tender_data, columns=self.table_columns)
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        tenders = soup.find_all('table',{'id': 'activeTenders'})
        index = 0
        for row in tenders[0].find_all('tr'):
            col = 0
            column = row.find_all('td')
            for c in column:
                df.loc[index, self.table_columns[col]] = c.get_text()
                col = col + 1
            index = index + 1
        df.to_csv('output.csv', index=False)

if __name__ == '__main__':
    url = 'https://etenders.gov.in/eprocure/app'
    table_columns = ['Tender Title', 'Reference No', 'Closing Date', 'Bid Opening Date']
    scraper = Scraper(url, table_columns)
    scraper.scrape_data()

 