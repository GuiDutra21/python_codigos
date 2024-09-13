
for i in range(0,5,2) :#condição_inicial, condição_final, incremento
    print(i)
print('')
for j in range(0,5) : #se omitirmos o incremento sera considerado como 1
    print(j)

n = int(input('Digite quantos numeros serao somados : '))
soma = 0

for i in range(0,n) :
    soma += int(input('Digite um numero : '))
print(soma)    

print()

for i in range(5,0,-1):
    print(i)
ola = 'amor'
print('testando uma cor \033[32m{}'.format(ola))#cor verde
