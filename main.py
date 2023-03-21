from requests import get 
from bs4 import BeautifulSoup

base_url = "https://remoteok.com/"
term = "remote-react-jobs"

response = get(f"{base_url}{term}", headers={"User-Agent": "Kimchi"})
if response.status_code != 200:
    print("can't request")
else:
    results=[]
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('tr', class_="job")
    for job in jobs:
        anchors = job.find_all('a', itemprop_="url")
        print(anchors)
        print("0-----------------------")
        title = job.find('h2')
        company = job.find('h3')
        locations = job.find_all('div',class_="location")
        company_info=[]
        for location in locations:
            company_info.append(location.string)
        job_data ={
            'title' : title.string.strip(),
            'company' : company.string.strip(),
            'location' : company_info
        }
        results.append(job_data)
    for result in results:
        """print(result)"""
        
            
            
        

