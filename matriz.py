l = int(input('Quantas linhas tera a matriz?'))
c = int(input('Quantas colunas tera a matriz?'))

matriz = [[0 for x in range(c)]for x in range(l)]

print('Insira os elementos da matriz : ')
for i in range(0,l):
    for j in range(0,c):
        matriz[i][j] = input(f'elemento[{i},{j}] : ')
    
print()
print('A matriz digitada foi : ')
for i in range(0,l):
    for j in range(0,c):
        print(f'{matriz[i][j]} ',end='')
    print()    
