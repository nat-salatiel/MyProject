nomeJogadores = []
camisaJogadores = []

for i in range(0,11):
    nomeJogadores.append(input("Digite o nome do jogador: "))
    camisaJogadores.append(input("Informe o número de sua camisa: "))

listaJogadores = list(zip(nomeJogadores, camisaJogadores))
print(listaJogadores)