saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    saldo -= saque
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")

print("Saldo atual: R$ %.2f" % saldo)