# issubset() - Retorna True se todos os elementos do conjunto estão presentes no conjunto especificado, caso contrário, ele retorna False.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

resultado = conjunto_a.issubset(conjunto_b)
print(resultado)  # True - todos os elementos de a estão em b

resultado2 = conjunto_b.issubset(conjunto_a)
print(resultado2)  # False - nem todos os elementos de b estão em a