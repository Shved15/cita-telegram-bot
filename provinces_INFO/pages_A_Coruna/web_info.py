import requests
from bs4 import BeautifulSoup
import lxml

with open("/home/shved15/my_pet_project/provinces_INFO/pages_A_Coruna/index_A Coruña.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")

a = soup.find_all('option')
arr = []
for b in a:
    arr.append(str(b.text))
arr

with open('A_Coruna_test.py', 'w') as file:
    for x in arr:
        file.write("'"+x+"'"+',')
        file.write('\n')
