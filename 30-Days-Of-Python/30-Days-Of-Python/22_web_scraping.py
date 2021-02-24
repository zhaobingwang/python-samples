# document: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/'
response = requests.get(url)
status = response.status_code
print(status)

content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)

submit_button = soup.findAll('input', {'type': 'submit'})
print(submit_button[0].get('value'))
