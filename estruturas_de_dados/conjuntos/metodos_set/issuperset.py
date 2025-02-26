# .issuperset() -> Verifica se um conjunto é um superconjunto de outro.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5}

resultado = conjunto_a.issuperset(conjunto_b)
print(resultado)  # True - todos os elementos de b estão em a

resultado2 = conjunto_b.issuperset(conjunto_a)
print(resultado2)  # False - nem todos os elementos de a estão em b