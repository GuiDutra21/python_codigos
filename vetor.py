n = int(input('Quantos numeros voce ira digitar ? '))
vetor = [0 for x in range(n)]

for i in range (0,n):
    vetor[i] = float(input('Digite um numero : '))

print('')
print('Os numeros digitados foram : ')
for i in range(0,n):
    print(f"numero {i + 1} : {vetor[i]:.1f}")
