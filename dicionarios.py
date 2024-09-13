pessoa = {'nome' : 'Guilherme', 'sexo' : 'M', 'idade' : 22}
print(f"{pessoa['nome']} tem     {pessoa['idade']} anos")
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for k,v in pessoa.items():
    print(f"{k} = {v}")

humano1 = {'Nome' : 'Josefina', 'Idade' : 30, 'Sexo' : 'feminino'}
humano2 = {'Nome' : 'Camila', 'Idade' : 32, 'Sexo' : 'feminino'}
populacao = []
populacao.append(humano1)
populacao.append(humano2)

print(populacao)
print(populacao[0])
print(populacao[1])
print(populacao[0]['Nome'])
