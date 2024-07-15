#Exibir uma mensagem de acordo com o dia da semana

print("Escolha um dia da semana: ")
print("1. Sexta")
print("2. Sábado")
print("3. Domingo")

dia = int(input())

match dia: 
    case 1: 
        print("Barzinho tomar um gelo XD")
    case 2: 
        print("Cinema e pipoca!")
    case 3: 
        print("Almoço na beira da praia <3")
    case _:
        print("Opção inválida.")