nome = "Vitor"
idade = 27
profissao = "Desenvolvedor"
linguagem = "Python"

print("Nome: {0}, Idade: {1}, Profissão: {2}, Linguagem: {3}".format(nome, idade, profissao, linguagem))

print("Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#usando dicionário

pessoa = {
    "nome": "Vitor",
    "idade": 27,
    "profissao": "Desenvolvedor",
    "linguagem": "Python"
    }

print("Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}".format(**pessoa))