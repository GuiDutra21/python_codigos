def lin():
    print('-'*30)

#descompactador
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')

def soma(a,b):
    return a + b

def fatorial(num = 1):
    c = 1
    for f in range( num, 0, -1):
        c *= f
    return c

lin()
print('teste')
lin()

contador(1,2,3,4)
contador(3,5,7,9,11,13)
contador(5)

resposta = soma(10,5)
print(f"O valor da soma eh : {resposta}")
n = int(input('DIGITE UM NUMERO '))
print(f"O fatoria de {n} eh igual a {fatorial(n)}")