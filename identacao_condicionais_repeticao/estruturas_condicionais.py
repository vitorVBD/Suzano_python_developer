#if
idade = 18

if idade >= 18:
    print("Maior de idade")

#if/else
saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    saldo -= saque
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")

print("Saldo atual: R$ %.2f" % saldo)

#if/elif/else
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 4:
    print("Recuperação")
else:
    print("Reprovado")