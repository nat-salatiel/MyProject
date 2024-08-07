def menorIdade():
    print("Que tal um desenho? Sugestões: Peppa Pig, Dora, a Aventureira, Patrulha Canina e Vila Sésamo")
def maiorIdade():
    print("Vamos comprar um carro? Sugestões: Toyota Corolla R$ 190.000,  Honda Civic R$ 180.000, Chevrolet Tracker  R$ 180.000, Volkswagen Polo R$ 120.000. ")

idade = int(input("Digite a sua idade: "))

if idade >=18:
    maiorIdade()
else:
    menorIdade()