#CALCULANDO MÉDIA DE 4 NOTAS E EXIBINDO MENSAGEM DE ACORDO COM A MÉDIA

print("Informe as notas do aluno: ")
nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
nota4 = int(input("Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media < 6:
    print("Aluno reprovado.")
else:
    print("Aluno aprovado!")

print(type(media))
