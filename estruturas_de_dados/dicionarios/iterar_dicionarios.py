contatos = {
    "vitor@teste.com": {
        "nome": "Vitor",
        "telefone": "1234-5678",
        "endereco": "Rua 1"
    },
    "teste@teste.com": {
        "nome": "Teste",
        "telefone": "9876-5432",
        "endereco": "Rua 2"
    }
}

for chave in contatos:
    print(chave, contatos[chave])

print()

for chave, valor in contatos.items():
    print(chave, valor)