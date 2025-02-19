opcao = -1

while opcao != 0:
    opcao = int(input("Digite [1] para sacar \nDigite [2] para depositar \nDigite [0] para sair\n: "))

    if opcao == 1:
        print("Sacar")
    elif opcao == 2:
        print("Depositar")
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida")
        break
