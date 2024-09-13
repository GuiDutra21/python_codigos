#A função input recebe todos os dados como string, consequentemente precisamos fazer a conversão se queremos um dado de outro tipo

nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input('Salario da primeira pessoa: '))

nome2 = input("Nome da segunda pessoa: ")
salario2 = float(input('Salario da segunda pessoa: '))

print("")#ja sai uma quebra de linha
print(f"O nome da primeira pessoas eh : {nome1} e o salario dela eh : {salario1}")
print(f"O noem da segunda pessoa eh : {nome2} e o salario dela eh : {salario2}")

a,b = input("Informe o valor de a e b :").split()
a1=float(a)
b1=float(b)
print(f"{a1} e {b1}")

