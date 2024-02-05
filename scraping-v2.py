import requests
from bs4 import BeautifulSoup
import re
import csv

csv_file = open('newsro_scrape.csv' , 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Titlu','Tip de articol','Data publicari'])

categorii = ["politic-intern", "justitie","externe","economic","eveniment","entertainment","sport",
"cultura-media","social"]
#Se face selectia pentru numarul de pagini
#Sunt categorii cu mult mai putine pagini de pe care se pot extrage articole, cand se ajunge
#la un dead-end programul va sari la urmatoarea categorie
pages = 200
loading = 1
for categorie in categorii:
	print(f"Task is at:{loading*10}%")
	for page in range(1, pages + 1):
		url = f"https://www.news.ro/{categorie}/?p={page}"
		page = requests.get(url).text
		soup = BeautifulSoup(page, "html5lib")
		for articole in soup.find_all('div', class_='col-sm-9')[:-4]:
			titlu = articole.h2.a.text
			tip = articole.h3.a.text
			data = articole.find('time', class_='a-date')
			data_val = str(data).split("\"")[3]

			csv_writer.writerow([titlu.encode('utf-8'), tip.encode('utf-8'), data_val])
			#csv_writer.writerow([titlu, tip, data_val])

	loading = loading + 1

csv_file.close()

		
