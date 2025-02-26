linguagens = ['Python', 'Java', 'C#', 'JavaScript', 'PHP', 'Ruby', 'C++', 'C', 'Swift', 'Kotlin']

linguagens.sort() # Ordena a lista em ordem alfabética
print(linguagens) # ['C', 'C#', 'C++', 'Java', 'JavaScript', 'Kotlin', 'PHP', 'Python', 'Ruby', 'Swift']

linguagens.sort(reverse=True) # Ordena a lista em ordem alfabética reversa
print(linguagens) # ['Swift', 'Ruby', 'Python', 'PHP', 'Kotlin', 'JavaScript', 'Java', 'C++', 'C#', 'C']

linguagens.sort(key=lambda x: len(x)) # Ordena a lista pela quantidade de caracteres de cada elemento
print(linguagens) # ['C', 'C#', 'C++', 'PHP', 'Ruby', 'Java', 'Swift', 'Python', 'Kotlin', 'JavaScript']

linguagens.sort(key=lambda x: len(x), reverse=True) # Ordena a lista pela quantidade de caracteres de cada elemento em ordem reversa
print(linguagens) # ['JavaScript', 'Python', 'Kotlin', 'Swift', 'Ruby', 'PHP', 'Java', 'C#', 'C++', 'C']