#break, interrompe a execução do laço de repetição

numero = 10

for i in range(0, 100):
    print(i, end=' ')
    if i == numero:
        break

print("\n")

#continue, similar ao break, porém, ele interrompe a execução do laço de repetição atual e passa para o próximo

for i in range(0, 100):
    if i % 2 == 0:
        continue
    print(i, end=' ')