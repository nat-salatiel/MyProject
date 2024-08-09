class cadastro:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def maiorIdade(self,idade):
        if cliente.idade >= 18:
            print("Maior de idade")
        else:
            print("Menor de idade.")

nome = input("Informe seu nome completo: ")
idade = int(input("Informe a sua idade: "))
altura = input("Informe a sua altura: ")
cliente = cadastro(nome, idade, altura)
cliente.maiorIdade(idade)