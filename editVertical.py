import re
import os
os.getcwd()
f=open("TRT2_Conteudo","r")
content = f.read()
print(content)
travado = re.sub("(\.)(\n)", r"kkkkkkk\2", content, flags = re.M)
joinQuebra = re.sub("(\n)", r" ", travado, flags = re.M)
destravado = re.sub("kkkkkkk", r".\n", joinQuebra, flags = re.M)
inicial = re.sub("(\n)(\s)", r"\1", destravado, flags = re.M)
lei_uno=re.sub("(\d)(\.|\. | \. )(\d)", r"\1lllllll\3", inicial, flags = re.M)
lei_due=re.sub("\. \d", r"lllllll", inicial, flags = re.M)
ponto_qb=re.sub("\.", r"\n", inicial, flags = re.M)
texto=re.sub("lllllll", r".", lei_due, flags = re.M)
quebras=re.sub("(\.|\:|\;)(\s)", r"\n", texto, flags = re.M)
c = re.sub("(^\s)", r"", quebras, flags = re.M)
print(c)
g=open("TRT2_Conteudo_mod","w")
g.write(c)
g.close()
f.close()
