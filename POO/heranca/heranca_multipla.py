class Animal:
    def __init__(self, numero_patas, cor_pelo):
        self.numero_patas = numero_patas
        self.cor_pelo = cor_pelo

    def __str__(self):
        return f'Número de patas: {self.numero_patas}, cor do pelo: {self.cor_pelo}'
        

class Mamifero(Animal):
    def __init__(self, **kw):
        super().__init__(**kw)

class Oviparo(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

    def __str__(self):
        return f'Número de patas: {self.numero_patas}, cor do pelo: {self.cor_pelo}, cor do bico: {self.cor_bico}'

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Oviparo):
    pass

cachorro = Cachorro(numero_patas=4, cor_pelo='branco')
print(cachorro)

ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo='marrom', cor_bico='preto')
print(ornitorrinco)