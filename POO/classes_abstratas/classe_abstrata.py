from abc import ABC, abstractmethod

class Controle_Remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class Controle_Tv(Controle_Remoto):
    def ligar(self):
        print('Ligando a TV')

    def desligar(self):
        print('Desligando a TV')

    @property
    def marca(self):
        return 'Samsung'

class Controle_Ar_Condicionado(Controle_Remoto):
    def ligar(self):
        print('Ligando o Ar Condicionado')

    def desligar(self):
        print('Desligando o Ar Condicionado')

    @property
    def marca(self):
        return 'LG'

controle = Controle_Tv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_2 = Controle_Ar_Condicionado()
controle_2.ligar()
controle_2.desligar()
print(controle_2.marca)