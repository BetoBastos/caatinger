#WaitForHost
def wait_for_host():
    from random import randint
    segundos=0
    while (segundos==0):
        segundos=randint(1,10)
        print(segundos)
        return segundos
if __name__ == '__main__':
    print('Funcao wait_for_host(): me executou pelo terminal')
else:
    print('Funcao wait_for_host(): me executou como um módulo')
segundos=wait_for_host()
print("O tempo de espera serah {}".format(segundos)+" segundos")
#Para usar funcao em outro modulo usar:
#import host_wait
