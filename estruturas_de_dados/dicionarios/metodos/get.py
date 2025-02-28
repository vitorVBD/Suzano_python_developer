# acessar valores dentro do dicionario

dicionario = {"nome": "Vitor", "email": "teste@teste.com", "telefone": "1234-5678"}

print(dicionario.get("nome"))
print(dicionario.get("email", "Não encontrado")) # se a chave não existir, retorna o valor padrão