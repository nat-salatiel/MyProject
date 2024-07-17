#Programa para converter temperaturas
print("Qual temperatura deseja converter? ")
print("1. De Celsius para Kelvin e Fahrenheit.")
print("2. De Kelvin para Fahrenheit e Celsius ")
print("3. De Fahrenheit para Kelvin e Celsius")
conversao = int(input())

temperatura = int(input("Digite a temperatura: "))

match conversao:
    case 1:
        kelvin = temperatura + 273
        Fahrenheit = (9/5 * temperatura) - 32
        print(f"Temperatura de Celsius para Kelvin será: {kelvin}.")
        print(f"Temperatura de Celsius para Fahrenheit será: {Fahrenheit}.")
    case 2:
        celsius = temperatura - 273
        Fahrenheit = 1.8 *( celsius) + 32
        print(f"Temperatura de Kelvin para Celsius será: {celsius}.")
        print(f"Temperatura de Kelvin para Fahrenheit será: {Fahrenheit}.")
    case 3:
        celsius = 5/9 * (temperatura - 32) 
        kelvin = (temperatura - 32) / 1.8 + 273
        print(f"Temperatura de Fahrenheit para Celsius será: {celsius}.")
        print(f"Temperatura de Fahrenheit para Kelvin será: {kelvin}.")


