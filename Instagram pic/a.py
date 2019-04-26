from bs4 import BeautifulSoup
import requests
from termcolor import colored

username=input("Enter the username : ")
try:
    source=requests.get('https://www.instagram.com/{}'.format(username)).text
    soup=BeautifulSoup(source,'lxml')
    p=soup.find('meta',property='og:image').attrs['content']
    # pic=requests.get(p).content

    with open('{}.jpg'.format(username),'wb') as pic:
        pic.write(requests.get(p).content)

    print(colored('done','green'))
except Exception:
    print(colored('Something goes wrong','red'))
