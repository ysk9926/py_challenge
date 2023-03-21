from requests import get 
from bs4 import BeautifulSoup

base_url = "https://remoteok.com/"
term = "remote-react-jobs"

response = get(f"{base_url}{term}", headers={"User-Agent": "Kimchi"})
if response.status_code != 200:
    print("can't request")
else:
    result=[]
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('tr', class_="job")
    for jobs_tr in jobs:
        jobs_td = jobs_tr.find_all('td')
        jobs_td.pop(4)
        jobs_td.pop(3)
        jobs_td.pop(0)
       
        for item in jobs_td:
            anchors = item.find_all('a')
            anchor = anchors[0]
            link = anchor['href']
            company = anchors.find('h2', class_="title")
            region = item.find_all('div', class_="location")
            print(region, company)
            
        

