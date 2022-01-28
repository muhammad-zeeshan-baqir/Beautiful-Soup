import requests
from bs4 import BeautifulSoup
url = 'https://themoviesflix.co'

z = requests.get(url)
html_content = z.content
print(html_content)
print('test')
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())
