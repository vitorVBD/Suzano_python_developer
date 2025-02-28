# se o atributo não estiver no dicionarion, ele será adicionado com o valor passado

dicionario = {'nome': 'Vitor', 'idade': 27}

dicionario.setdefault('sexo', 'masculino')

print(dicionario)  # {'nome': 'Vitor', 'idade': 27, 'sexo': 'masculino'}