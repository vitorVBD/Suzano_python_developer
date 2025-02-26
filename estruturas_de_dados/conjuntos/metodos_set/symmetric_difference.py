# .symmetric_difference() - Retorna um conjunto que contém todos os elementos de dois conjuntos, exceto os elementos que são comuns a ambos.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)  # {1, 2, 3, 6, 7, 8}