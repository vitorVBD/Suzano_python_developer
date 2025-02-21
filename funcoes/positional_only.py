def criar_carro(marca, modelo, ano, / , placa, cor): # / = indica que os argumentos anteriores são apenas posicionais
    print(marca, modelo, ano, placa, cor)

criar_carro("Mercedes", "A200", 2016, placa="ABC-1234", cor="cinza")

#codigo invalido: criar_carro(marca="Mercedes", modelo="A200", ano=2016, placa="ABC-1234", cor="cinza")