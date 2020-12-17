from bs4 import BeautifulSoup
import requests

r = requests.get('http://10.10.136.132:8000/static/index.html') 

soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all('a')
for link in links:      
    # prints each link    
    print(link.get('href'))
