#As listas podem ser alteradas
lista = [1,2,3,4]
lista[0] = 5 
print(lista)

valores = list(range(4,11))#lista com [4,5,6,7,8,9,10]
print(valores)

#se igualarmos uma lista a outra tudo que fizermos em uma sera feito na outra
a = [1,2,3,4]
b = []

b = a
b[0] = 'a'
print(f'lsita a : {a} e lista b : {b}')

# para que isso nao ocorra podemso fazer o seguinte

b = a[:]
b[0] = 'ameba'
print(f'lsita a : {a} e lista b : {b}')

#para adicionar elementos
adicionar = [1,2,3]
adicionar.append(4)
print(adicionar)
