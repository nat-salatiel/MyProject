#classificando por ordem numérica
print("Digite 3 números: ")
x = int(input("Número 1: "))
y = int(input("Número 2: "))
z = int(input("Número 3: "))

if x > y and y > z:
    print("Números em ordem decrescente!")
elif x < y and y < z: 
    print("Números em ordem crescente!")
else:
    print("Os números estão misturados!")
