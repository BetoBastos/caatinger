#WaitForHost
def wait_for_host():
    from random import randint
    lista=list()
    cont=0
    while True:
        num=randint(1,10)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=10:
            break
    lista.sort()
    return lista
if __name__ == '__main__':
    print('Funcao wait_for_host(): me executou pelo terminal')
else:
    print('Funcao wait_for_host(): me executou como um módulo')
lista=wait_for_host()
print("Os numeros sorteados foram {}".format(lista))
#Para usar funcao em outro modulo usar:
#import host_wait
