class Iterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.indice]
            self.indice += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        
for i in Iterador([1, 2, 3, 4, 5]):
    print(i)