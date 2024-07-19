#Identificando as posicoes de acordo com a funcao do jogador.

funcao = input("Informe a sua função em campo: ")

if funcao == "goleiro" or funcao == "zagueiro" or funcao == "lateral":
    print("Defesa!")
elif funcao == "volante" or funcao == "meia":
    print("Meio-Campo!")
elif funcao == "ponta" or funcao == "atacante" or funcao == "centroavante":
    print("Ataque!")
else:
    print("Teimoso!")
