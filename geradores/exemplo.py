def gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in gerador([1, 2, 3, 4, 5]):
    print(i)