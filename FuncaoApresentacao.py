#Demonstração do uso de funções

def apresentar():
    print(f"Meu nome é {meuNome}. ")
    print(f"Minha altura é de {minhaAltura} metros. ")
    print(f"Minha idade é {minhaIdade} anos. ")
    return
def conferir(x):
    if x >= 18:
        print("Você é maior de idade! ")
    else:
        print("Ops, menor de idade não pode!")
    return

meuNome = str(input("Digite o seu nome: "))
minhaAltura = float(input("Digite a sua altura: "))
minhaIdade = int(input("Digite a sua idade: "))

apresentar()
conferir(minhaIdade)