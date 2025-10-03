import threading
from bs4 import BeautifulSoup
import requests

urls=[
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/versions/v0_2/',
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} chracter from {url}')

threads=[]

for url in urls:
    thread