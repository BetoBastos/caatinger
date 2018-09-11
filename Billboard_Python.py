import requests
from bs4 import BeautifulSoup
import csv
url="http://www.billboard.com/charts/hot-100"
r=requests.get(url)
page_cont=r.content
print(page_cont)
page_cont_par=BeautifulSoup(r.content,"html.parser")
containers=page_cont_par.findAll("div",{"class":"chart-row__main-display"})
filename="musics.csv"
f=open(filename,"w")
headers="posicao;musica;artista\n"
f.write(headers)
container=containers[0]
for container in containers:
	posicao=container.div.span.text.strip()
	musica=container.h2.text.strip()
	artista=container.a.text.strip()
	
	print("posicao: " + posicao)
	print("musica: " + musica)
	print("artista: " + artista)
	f.write(posicao + ";" + musica.replace(";","|") + ";" + artista.replace(";","|") + "\n")
		
f.close()