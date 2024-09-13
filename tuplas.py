#As tupleas sao imutaveis, e possível acrescentar um valor, mas não alterar os valores já existente 
# e também não é possível apagar um elemento apenas a tupla toda
#As tuplas podem ser formadas por qualquer tipo de dado
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))

a = (4,6,2,3,3,4)
b = (4,5,6,9,8,0,2,3)
c = a + b
print(c)
print(c.count(3))
print(c.index(3))#pega a primeira posicao