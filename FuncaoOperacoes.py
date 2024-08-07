#Demonstração do uso de funções

def adicao(x,y):
    return x+y
def subtracao(x,y):
    return x-y
def multiplicacao(x,y):
    return x*y
def divisao(x,y):
    return x/y

print("Digite dois valores inteiros: ")
n1 = int(input("X: "))
n2 = int(input("Y: "))
op = input("Digite qual operação deseja realizar: (+,-,* ou /) ")

if op == "+":
    z = adicao(n1, n2)
    print(f"Resultado da soma: {z}")
elif op == "-":
    z = subtracao(n1, n2)
    print(f"Resultado da subtração: {z}")
elif op == "*":
    z = multiplicacao(n1, n2)
    print(f"Resultado da multiplicação: {z}")
elif op == "/":
    z = divisao(n1, n2)
    print(f"Resultado da divisão: {z}")
else:
    print("Opção digitada inexistente! ")

 