class Cachorro():
    def __init__(self, nome, cor, raça):
        print('Inicializando um objeto')
        self.nome = nome
        self.cor = cor
        self.raça = raça

    def __del__(self):
        print(f'O cachorro {self.nome} foi deletado')

    def latir(self):
        print('Au au')


cachorro = Cachorro('Koe', 'Branco', "Husky")

cachorro.latir()