# .difference() - Retorna um conjunto que contém todos os elementos do conjunto de chamada que não estão presentes em nenhum dos outros conjuntos passados como argumento.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
conjunto_c = {3, 10, 14}

diferenca = conjunto_a.difference(conjunto_b, conjunto_c)
print(diferenca)  # {1, 2}