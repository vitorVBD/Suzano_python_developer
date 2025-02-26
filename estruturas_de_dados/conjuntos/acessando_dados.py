# para acessar valores de um set, é preciso converter em lista

set = {1, 2, 3, 4, 5}

#convertendo em lista
numero = list(set)

# acessando o primeiro valor
print(numero[0])

# porém é possível iterar em um set

carros = {"Fusca", "Gol", "Palio", "Uno"}

for carro in carros:
    print(carro)


print()
# enumerate

for indice, carro in enumerate(carros):
    print(indice, carro)
