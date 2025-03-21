def mensagem(nome):
    print("Executando mensagem")
    return f"Olá {nome}!"

def mensagem_longa(nome):
    print("Executando mensagem_longa")
    return f"Olá {nome}, seja bem-vindo ao mundo Python!"

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)

print(executar(mensagem, "Vitor"))
print(executar(mensagem_longa, "Vitor"))