def criar_carro(modelo, ano, placa, /, motor, *, marca): 
    # modelo, ano e placa sao positional_only, motor é positional ou keyword e marca é keyword_only
    print(f'Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Motor: {motor}')

criar_carro("A200", 2020, "ABC-1234", 1.6, marca="Mercedes")
criar_carro("XC60", 2018, "XYZ,890", motor=2.0, marca="Volvo")

#criar_carro("Mercedes", "A200", 2020, "ABC-1234") # Erro: TypeError: criar_carro() takes 3 positional arguments but 4 were given
#criar_carro(modelo="A200", ano=2020, placa="ABC-1234", "Mercedes") # Erro: SyntaxError: positional argument follows keyword argument