class Estudante:
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} estudante da escola {self.escola} com matrícula {self.matricula}"
    
aluno = Estudante("Vitor", 1234)

print(aluno) # Vitor estudante da escola Dio com matrícula 1234