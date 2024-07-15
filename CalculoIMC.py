#Calculando o imc do usuário

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso/altura

if imc > 25:
    print("Acima do peso ideal.")
elif imc < 18:
    print("Abaixo do peso ideal.")
else:
    print("Seu peso está OK.")
