# .add() adiciona um elemento que não existe ao conjunto

conjunto = {1, 2, 3}

conjunto.add(4)
print(conjunto)  # {1, 2, 3, 4}

conjunto.add(4)
print(conjunto)  # {1, 2, 3, 4} - não adiciona o 4 novamente