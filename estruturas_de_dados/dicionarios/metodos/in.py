# saber se uma chave existe no dicionario

contatos = {
    "vitor@teste.com": {
        "nome": "Vitor",
        "telefone": "123456789"
    },
    "teste@teste.com": {
        "nome": "Teste",
        "telefone": "987654321"
    }
}

resultado = "vitor@teste.com" in contatos
print(resultado)  # True

resultado = "idade" in contatos["vitor@teste.com"]
print(resultado)  # False

resultado = "nome" in contatos["vitor@teste.com"]
print(resultado)  # True