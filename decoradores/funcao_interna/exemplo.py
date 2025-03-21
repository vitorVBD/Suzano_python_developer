def principal():
    print('Função principal')

    def interna():
        print('Função interna')
    
    def funcao_2():
        print('Função 2')

    interna()
    funcao_2()

principal()