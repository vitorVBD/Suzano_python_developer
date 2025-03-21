class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2025 - ano_nascimento
        return Pessoa(nome, idade)
    
    @staticmethod
    def eh_maior_de_idade(idade):
        return idade >= 18

p = Pessoa.por_ano_nascimento('Vitor', 1998)
print(p.nome, p.idade)

print(p.eh_maior_de_idade(p.idade))