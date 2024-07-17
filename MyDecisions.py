#Demosntração operadores lógicos

print("O que você vai fazer amanhã de manhã? ")
print("Dormir/ estudar/ planejar")
manha = input()
print("O que você vai fazer amanhã de tarde? ")
print("Jogar/ treinar/ trabalhar")
tarde = input()

if not manha or not tarde:
    print("Você precisa dizer o que vai fazer!")
else: 
    if manha == "dormir" or tarde == "jogar":
        print("Você está desperdiçando o seu dia!")
    elif manha == "estudar" or tarde == "treinar":
        print("Que bom! Você irá se aperfeiçoar!")
    elif manha == "planejar" or tarde == "trabalhar":
        print("Para trabalhar melhor, devo planejar!")
    else:
        print("Não combinamos estas ações.")

print("Tenha um bom dia!")