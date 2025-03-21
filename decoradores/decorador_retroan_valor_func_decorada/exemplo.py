def decorador(funcao):
    def envelope(*args, **kwargs):
        print("Antes da função")
        resultado = funcao(*args, **kwargs)
        print("Depois da função")
        return resultado


    return envelope


@decorador
def ola(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}!")
    return nome.upper()

resultado_ola = ola("Vitor", "Bittencourt")
print(resultado_ola)
