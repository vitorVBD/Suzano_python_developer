#remove uma chave e retorna o valor

dicionario = {'nome': 'Vitor', 'idade': 27, 'cidade': 'São Paulo'}

valor = dicionario.pop('idade')

print(valor) # 25
print(dicionario) # {'nome': 'Vitor', 'cidade': 'São Paulo'}

valor_2 = dicionario.pop('telefone', 'Chave não encontrada')
print(valor_2) # Chave não encontrada