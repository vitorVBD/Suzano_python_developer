from datetime import datetime

class Pessoa:
    def __init__(self,nome, ano_nascimento):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        _ano_atual = datetime.now().year
        return _ano_atual - self.__ano_nascimento
    

pessoa = Pessoa("Vitor", 1998)
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade} anos")