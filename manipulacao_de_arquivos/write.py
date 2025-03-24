arquivo = open("C:\Aulas\Python\manipulacao_de_arquivos/teste.txt", "w") #criando um arquivo teste.txt
arquivo.write("Esse eh o meu arquivo teste.") #escrevendo no arquivo
arquivo.writelines(["\n" "Escrevendo ", "um ", "novo ", "texto"]) #writelines escreve uma lista de strings
arquivo.close()