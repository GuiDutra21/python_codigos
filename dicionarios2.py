brasil = list()
estado = dict()

for k in range(0,3):
    estado['uf'] = input('Digite o uf ')
    estado['sigla'] = input('Digite a sigla ')
    brasil.append(estado.copy())

print(brasil)