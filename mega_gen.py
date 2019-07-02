#https://www.youtube.com/watch?v=Hd7Ycaj61xE
#MegaSena
def gera_mega():
    from random import randint
    lista=list()
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    return lista
if __name__ == '__main__':
    print('Funcao gera_mega(): me executou pelo terminal')
else:
    print('Funcao gera_mega(): me executou como um módulo')
lista=gera_mega()
print("Os numeros sorteados foram {}".format(lista))
