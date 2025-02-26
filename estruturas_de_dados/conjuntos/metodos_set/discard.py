# .discard() - Remove um elemento de um conjunto se ele estiver presente.
# Se o elemento não estiver presente, ele não faz nada.

conjunto = {1, 2, 3, 4, 5}

conjunto.discard(3)
print(conjunto)  # {1, 2, 4, 5}

carros = {"Fusca", "Gol", "Palio", "Uno"}
carros.discard("Fusca")
print(carros)  # {'Gol', 'Palio', 'Uno'}