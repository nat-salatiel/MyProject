#Realizar tabuada do número que o usuário digitar

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{numero} X {i}  = ", numero * i)