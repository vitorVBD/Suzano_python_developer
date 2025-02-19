#operadores lógicos

#and
print("Operador and")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or
print("Operador or")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not
print("Operador not")
print(not True)
print(not False)
print(not "") #string vazia é considerada False, então o not inverte para True
print(not "hello") #string com conteúdo é considerada True, então o not inverte para False
lista_vazia = []
print(not lista_vazia) #lista vazia é considerada False, então o not inverte para True