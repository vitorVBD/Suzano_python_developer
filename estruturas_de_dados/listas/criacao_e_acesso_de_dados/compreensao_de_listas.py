numeros = [1, 6, 44, 23, 35, 67, 48, 26]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # [6, 44, 48, 26]

quadrados = [numero**2 for numero in numeros]
print(quadrados)  # [1, 36, 1936, 529, 1225, 4489, 2304, 676]