import requests
from bs4 import BeautifulSoup
import csv
url="http://futura.org.br/programacao-completa/"
r=requests.get(url)
page_cont=r.content
page_cont_par=BeautifulSoup(r.content,"html.parser")
containers=page_cont_par.findAll("section",{"class":"item-programa col-xs-12"})
filename="programa_futura.csv"
f=open(filename,"w")
headers="inicio;final;programa;descricao\n"
f.write(headers)
container=containers[0]
for container in containers:
	inicio=container.div.findAll("span",{"class":"inicio"})[0].text
	final=container.div.findAll("span",{"class":"fim"})[0].text
	programa=container.findAll("h2")[0].text
	descricao=container.findAll("p")[0].text
	print("inicio: " + inicio)
	print("final: " + final)
	print("programa: " + programa)
	print("descricao: " + descricao)
	f.write(inicio + ";" + final.replace(",","|") + ";" + programa.replace(";","|") + ";" + descricao.replace("\n"," ") + "\n")	

f.close()