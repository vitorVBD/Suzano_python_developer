frutas = ('banana', 'maçã', 'uva', 'morango',)

# Acessando valores
print(frutas[0]) # banana
print(frutas[-2]) # uva

# Slicing / Fatiamento
print(frutas[1:3]) # ('maçã', 'uva')
print(frutas[:2]) # ('banana', 'maçã')
print(frutas[2:]) # ('uva', 'morango')

# Concatenação
frutas += ('laranja', 'abacaxi',)
print(frutas) # ('banana', 'maçã', 'uva', 'morango', 'laranja', 'abacaxi')