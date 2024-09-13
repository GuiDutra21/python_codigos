#Para converter uma lista em string e depois o contrario
lista = list(input('Digite uma frase : '))

for i in range(0,len(lista)):
    if(lista[i] == 'a'):
        lista[i] = 'b'
a = ''.join(lista)
print(a)