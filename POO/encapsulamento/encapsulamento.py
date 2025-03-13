class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo # Atributo protegido por convenção

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    @property
    def saldo(self):
        return self._saldo

conta = Conta(100)
print(conta.saldo) # forma correta de exibir um atributo protegido