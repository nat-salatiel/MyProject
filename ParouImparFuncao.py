def ParOuImpar():
    soma = numeroAleatorio + numeroUsuario
    if soma % 2 == 0:
        print("Deu par! Você venceu!")
    else:
        print("Deu ímpar! Você perdeu!")

numeroAleatorio = 3
numeroUsuario = int(input("Digite um número inteiro: "))

ParOuImpar()