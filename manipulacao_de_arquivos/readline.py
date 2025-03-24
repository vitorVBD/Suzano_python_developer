arquivo = open("C:\Aulas\Python\manipulacao_de_arquivos\lorem.txt", "r")
linha = arquivo.readline()
print(linha) # Imprime a primeira linha do arquivo

while linha != "":
    linha = arquivo.readline()
    print(linha) # Imprime as linhas restantes do arquivo

arquivo.close()