pessoa = {"nome": "Vitor", "idade": 27, "cidade": "Três Rios"}

print(pessoa)  # {'nome': 'Vitor', 'idade': 27, 'cidade': 'Três Rios'}

pessoa2 = dict(nome="Vitor", idade=27, cidade="Três Rios")

print(pessoa["nome"])  # Vitor

print(pessoa2["idade"])  # 27

pessoa["email"] = "exemplo@exemplo.com"

print(pessoa)