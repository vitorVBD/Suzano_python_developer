matriz = (
    (1, "a", 3,),
    ("c", 5, 6,),
    (7, 8, "b",)
)

print(matriz[0][0])  # 1
print(matriz[1][1])  # 5
print(matriz[0]) # (1, 'a', 3)

# Acessando todos os elementos da matriz
for linha in matriz:
    for coluna in linha:
        print(coluna, end=" ")
    print()