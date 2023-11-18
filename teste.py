from random import randint

matrix = []

for i in range(12):
    linha = []
    for a in range(12):
        linha.append(randint(0,99))
    matrix.append(linha)

print(matrix)
count_inicial = 1
count_final = 11
soma = 0

for i in range(1,2):
    for a in range(count_inicial , count_final):
        soma += matrix[i][a]
    count_inicial += 1
    count_final -= 1

print(f"Soma: {soma}")