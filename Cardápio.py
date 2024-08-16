cafeManha = []
almoco = []
janta = []
cliente = input("Seja bem-vindo(a)! Qual o seu nome? ")

print("Qual a sua opção de café da manhã? ")
for i in range(0,3):
    cafeManha.append(input(f"Escolha a {i+1}° opção: "))
    if cafeManha[i] == "leite" or cafeManha[i] == "queijo":
        print("Esse alimento não é indicado para pessoas com intolerância à lactose!")


print("Qual a sua opção de almoço? ")
for i in range(0,4):
    almoco.append(input(f"Escolha a {i+1}° opção: "))
    if almoco[i] == "peixe" or almoco[i] == "camarão":
        print("Esse alimento não é indicado para pessoas alérgicas à frutos do mar!")


print("Qual a sua opção de janta? ")
for i in range(0,4):
    janta.append(input(f"Escolha a {i+1}° opção: "))
    if janta[i] == "peixe" or janta[i] == "lasanha":
        print("Esse alimento não é indicado para pessoas alérgicas à frutos do mar ou com intolerância à lactose!")


print(f"Cardápio de {cliente}: \n Café da manhã: {cafeManha} \n Almoço: {almoco} \n Janta: {janta}")
