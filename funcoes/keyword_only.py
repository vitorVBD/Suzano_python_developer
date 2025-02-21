def criar_carro(*, marca, modelo): # * indica que os argumentos seguintes devem ser passados como palavras-chave
    print(f'Marca: {marca}, Modelo: {modelo}')

criar_carro(marca="Mercedes", modelo="A200")

#codigo invalio: criar_carro("Mercedes", "A200")