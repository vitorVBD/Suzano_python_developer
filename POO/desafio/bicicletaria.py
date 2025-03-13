class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print('Bi Bi')
    
    def parar(self):
        print('Parando')
        print('Bicicleta parada')

    def correr(self):
        print('Correndo')
        print('Bicicleta em movimento')

    def __str__(self):
        # return f'Bicicleta {self.cor} {self.modelo} {self.ano} {self.valor}'
        return f'{self.__class__.__name__} {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'


bicicleta = Bicicleta('vermelha', 'Caloi', 2025, 1000, 18)

bicicleta.buzinar()
bicicleta.correr()
bicicleta.parar()
print(bicicleta)