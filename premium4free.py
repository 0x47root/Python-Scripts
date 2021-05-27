"""
This Script grabs the text from premium Volkskrant articles. Enjoy.
"""
from bs4 import BeautifulSoup
import requests

# Define variables:
text_list = []

# Ask the user for the URL:
URL = input("Geef de URL op van het artikel: ")

# Try to connect to the server:
try:
	r = requests.get(URL)
except requests.exceptions.ConnectionError:
	print("Connection error!")

# Put the text in a list
soup = BeautifulSoup(r.text, "html.parser")
text = soup.find_all(class_="artstyle__text")
for t in text:
	var = t.get_text()
	text_list.append(var)

# Filter the text format
for i in range(len(text_list)):
	text_list[i] = text_list[i][7:]

# Print tekst
for text in text_list:
	print(text)
