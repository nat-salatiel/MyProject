#Recebendo avalição de serviço prestado

print("O serviço foi realizado? 0) Não executado, 1) Executado")
statusDoServico = (input("Digite uma das opções acima: "))

if statusDoServico == "0) Não executado":
    input("Descreva aqui o problema com o serviço: ")
    print("Pedimos desculpas pelo transtorno, iremos melhorar isso!")
else:
    print("Como você avalia nosso serviço? 1) péssimo, 2) ruim, 3) razoável, 4) bom, 5) ótimo.")
    nota = int(input("Digite uma das opções acima: "))

