x = int(input("entre com um numero : "))
soma = 0

while x != 0 :
    soma = soma + x
    x = int(input('Entre com um outro numero : '))
print('Soma = ',soma)

n = soma = 0
while True :
    n = int(input('Digite um numero : '))
    if(n == 999):
        break
    soma  += n
print(f'O valor da soma eh : {soma}')
    