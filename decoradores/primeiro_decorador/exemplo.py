def meu_decorador(funcao):
    def envelope():
        print('antes')
        funcao()
        print('depois')
    return envelope

@meu_decorador
def ola_mundo():
    print('Olá, mundo!')


ola_mundo()