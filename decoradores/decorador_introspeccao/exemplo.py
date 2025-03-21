import functools

def decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado


    return envelope


@decorador
def ola(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}!")
    return nome.upper()

print(ola.__name__)
