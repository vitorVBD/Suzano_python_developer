# .isdisjoint() - Verifica se dois conjuntos são disjuntos, ou seja, se não possuem elementos em comum.

conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {3, 4, 5}

print(conjunto_a.isdisjoint(conjunto_b))  # True

print(conjunto_a.isdisjoint(conjunto_c))  # False

print(conjunto_b.isdisjoint(conjunto_c))  # False