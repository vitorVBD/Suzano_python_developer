lista = ["Python", "Java", "C#", "Ruby", "PHP", "JavaScript", "C++", "Swift", "Kotlin", "Go"]

print(lista[2:]) # ['C#', 'Ruby', 'PHP', 'JavaScript', 'C++', 'Swift', 'Kotlin', 'Go'] do índice 2 até o final

print(lista[:5]) # ['Python', 'Java', 'C#', 'Ruby', 'PHP'] do início até o índice 5

print(lista[2:5]) # ['C#', 'Ruby', 'PHP'] do índice 2 até o índice 5

print(lista[2:8:2]) # ['C#', 'PHP', 'C++', 'Kotlin'] do índice 2 até o índice 8 pulando de 2 em 2

print(lista[::2]) # ['Python', 'C#', 'PHP', 'C++', 'Kotlin'] do início até o final pulando de 2 em 2

print(lista[::-1]) # ['Go', 'Kotlin', 'Swift', 'C++', 'JavaScript', 'PHP', 'Ruby', 'C#', 'Java', 'Python'] invertendo a lista