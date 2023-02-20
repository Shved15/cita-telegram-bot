from bs4 import BeautifulSoup
import requests

with open("/home/shved15/my_pet_project/pages_requests/pages_Tarragona/index_Tarragona_2.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_country = soup.find("select", class_= "mf-input__m")

l = []
for nation in all_country:
    nation.append(nation.find('//*[@id="txtPaisNac"]'))
print(l)
