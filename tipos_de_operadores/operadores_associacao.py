#operadores utilizados para verificar se um objeto está presente em uma sequência

#in
#Retorna True se um valor especificado estiver presente em um objeto, caso contrário, False.
#Exemplo:
print("in:")
x = 5
y = 8
lista = [1, 2, 3, 4, 5]
print(x in lista)
print(y in lista)

cursos = ["python", "java", "c++", "c#"]
print("python" in cursos)
print("javascript" in cursos)

#not in
#Retorna True se um valor especificado não estiver presente em um objeto, caso contrário, False.
#Exemplo:
print("not in:")
print(x not in lista)
print(y not in lista)

print("python" not in cursos)
print("javascript" not in cursos)

#case sensitive
print("Python" in cursos) #False