# update permite que você atualize um dicionário com outro dicionário, adicionando pares chave-valor de um dicionário a outro.

contatos = {
    "vitor@teste.com": {
        "nome": "Vitor",
        "telefone": "123456789",
        "endereco": "Rua 1"
    }
}

contatos.update({"vitor@teste.com": {"nome": "Vitor Bittencourt", "telefone": "987654321", "endereco": "Rua 2"}})

print(contatos)

print()

contatos.update({"teste@teste": {"nome": "Teste", "telefone": "123456789", "endereco": "Rua 1"}})

print(contatos)