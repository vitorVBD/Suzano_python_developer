class Passaro:
    def voar(self):
        print("Voando")


class Pardal(Passaro):
    def voar(self):
        return super().voar()
    

class Avestruz(Passaro):
    def voar(self):
        print("Não pode voar")

    
def plano_voo(objeto):
    objeto.voar()


pardal = Pardal()
avestruz = Avestruz()

plano_voo(pardal)
plano_voo(avestruz)