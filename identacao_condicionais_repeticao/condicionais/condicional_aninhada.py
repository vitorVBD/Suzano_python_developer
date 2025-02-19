idade = int(input("Digite a idade: "))
sexo = str(input("Digite o sexo (M/F): "))

if idade >= 18:
    if sexo == "F":
        print("Maior de idade do sexo feminino")
    else:
        print("Maior de idade do sexo masculino")
else:
    if sexo == "M":
        print("Menor de idade do sexo masculino")
    else:
        print("Menor de idade do sexo feminio")