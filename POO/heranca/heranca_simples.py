class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print('Ligando motor do')

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas) # chama o construtor da superclasse
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} está carregado')

moto = Motocicleta("preta","ABC-1234",2)
moto.ligar_motor()

carro = Carro("vermelho","XYZ-5678",4)
carro.ligar_motor()

caminhao = Caminhao("branco","DEF-9012",8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()