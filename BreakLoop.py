#Demonstração do uso de break

contador = 0; senha = " "
while senha != "S3nh4":
    print("Digite a senha: ")
    senha = input()

    if senha == "S3nh4":
        print("Senha correta! ")
        break
    else:
        print("Senha errada... ")

    contador = contador + 1
    if contador == 3:
        print("Tentativas excedidas! ")
        break