import requests 
from bs4 import BeautifulSoup as bs 
import pandas as bd
  
T = []
L= [] 
OCC=[]
COMP=[]
S=[]
for page in range(0,3): 
     
    req = requests.get( "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=machine%20learning&start="+str(page)) 
    soup = bs(req.text, "html.parser") 
  
    titles = soup.find_all('h2',{'class':'css-m604qf'})
    titles_lst = [title.text for title in titles]
    T+= titles_lst
    T
    links = [ title.a['href'] for title in titles]
    L+=links
    L
    occupations = soup.find_all("div", {'class': 'css-1lh32fc'})

    occupation_list=[occupation.text for occupation in occupations]
    OCC+=occupation_list
    OCC
    companies = soup.find_all("a", {'class': 'css-17s97q8'})
    companies_list=[company.text for company in companies]

    COMP+=companies_list
    COMP
    specs = soup.find_all("div", {'class': 'css-y4udm8'})
    specs_list=[spec.text for spec in specs]
    S+=specs_list
    S
scraped_data = {}
scraped_data['Title'] = T
scraped_data['Link'] = L
scraped_data['Occupation'] = OCC
scraped_data['Company'] = COMP
scraped_data['Specs'] = S
scraped_data
df = bd.DataFrame.from_dict(scraped_data,orient='index')
df = df.transpose()
df
df.to_csv('mljobs.csv', index=False)


