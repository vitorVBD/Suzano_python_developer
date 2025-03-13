class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print(f'{self.nome} está latindo!')

    def dormir(self):
        self.acordado = False
        print(f'{self.nome} está dormindo!')