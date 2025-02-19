def sacar(valor: float):
    saldo = 1000
    print('Saldo atual: R$', saldo)

    if saldo >= valor:
        print('Saque realizado com sucesso!')
        saldo -= valor
        print('Saldo restante: R$', saldo)
    else:
        print('Saldo insuficiente!')

    print('Operação finalizada!')


sacar(500)
sacar(1500)