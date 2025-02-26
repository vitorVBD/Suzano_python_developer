linguagens = ['Python', 'Java', 'C', 'JavaScript', 'Ruby']

# Ordena a lista em ordem crescente
print(sorted(linguagens, key=len))  # ['C', 'Java', 'Ruby', 'Python', 'JavaScript']

# Ordena a lista em ordem alfabética reversa
print(sorted(linguagens, key=len, reverse=True))  # ['JavaScript', 'Python', 'Ruby', 'Java', 'C']