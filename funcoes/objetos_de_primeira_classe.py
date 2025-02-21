def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(funcao, a, b):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(somar, 10, 20)

exibir_resultado(subtrair, 10, 5)

# Atribuindo uma função a uma variável
operacao = somar

print(operacao(2, 2))