#Calculando o imc do usuário

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso/altura**2

if imc > 25:
    print(f"Acima do peso ideal. {imc}")
elif imc < 18:
    print(f"Abaixo do peso ideal. {imc}")
else:
    print(f"Seu peso está OK. {imc}")
