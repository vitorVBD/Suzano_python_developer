def decorador(funcao):
    def envelope(*args, **kwargs):
        print("Antes da função")
        funcao(*args, **kwargs)
        print("Depois da função")

    return envelope


@decorador
def ola(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}!")

ola("Vitor", "Bittencourt")