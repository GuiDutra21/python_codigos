idade : int

idade = 12
salario = 7885.558
altura = 1.85
genero = "M"
nome = "Guilherme Silva"

print(f"idade = {idade}")
print(f"salario = {salario:.2f}")#arredonda para duas casas decimais
print(f"altura = {altura}")
print(f"genero = {genero}")
print("nome = {}".format(nome))#outra opção
print("O pequeno garfanho " + nome + " tinha {} anos e {} metros" .format(idade,altura))