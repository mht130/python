import requests
from bs4 import BeautifulSoup
import os

url="http://m86valthw.l1wr6ke1f86v.w0kriscaz3hcff0sb26887827rxg7ib99m7xk9x9ikr3qil7ax59bjhogl.xyz/Serial/House%20M.D/S02/"

source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')
for i in soup.body.find_all('a',href=True)[25:]:
    os.system(f"uget-gtk --quiet {url+i['href']}")
    # print(i['href'])