from bs4 import BeautifulSoup
import requests

URL = input("Please enter the website URL: ")

r = requests.get('URL') 

soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all('a')
for link in links:      
    # prints each link    
    print(link.get('href'))
