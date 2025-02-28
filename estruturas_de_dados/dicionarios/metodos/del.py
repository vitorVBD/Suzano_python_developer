# tira um valor do dicionario

contatos = {
    "vitor@teste.com": {
        "nome": "Vitor",
        "telefone": "123456789"
    }
}

del contatos["vitor@teste.com"]["telefone"]

print(contatos)

del contatos["vitor@teste.com"]

print(contatos)