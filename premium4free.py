"""
This Script grabs the text from premium Volkskrant articles. Enjoy.
"""
from bs4 import BeautifulSoup
import requests

# Definieer variabelen:
text_list = []

# Vraag de gebruiker om een URL
URL = input("Geef de URL op van het artikel: ")

# Probeer een connectie met de website te maken
try:
	r = requests.get(URL)
except requests.exceptions.ConnectionError:
	print("Connection error!")

# Sla de tekst op in de variabele 'text'
soup = BeautifulSoup(r.text, "html.parser")
text = soup.find_all(class_="artstyle__text")

# Verzamel de tekst in een lijst:
for t in text:
	var = t.get_text()
	text_list.append(var)

# Filter de format van de tekst
for i in range(len(text_list)):
	text_list[i] = text_list[i][7:]

# Print tekst
for text in text_list:
	print(text)
