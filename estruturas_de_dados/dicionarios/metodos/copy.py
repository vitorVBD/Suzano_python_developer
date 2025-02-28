# cria uma copia do dicionario

dicionario = {"vitor@teste.com": {"nome": "Vitor", "telefone": "1234-5678", "endereco": "Rua 1"}}

copia = dicionario.copy()

print(dicionario)
print(copia)

copia["vitor@teste.com"] = {"nome": "Vitor"}


print()

print(dicionario)
print(copia)