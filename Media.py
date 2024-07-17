#CALCULANDO MÉDIA DE 4 NOTAS E EXIBINDO MENSAGEM DE ACORDO COM A MÉDIA

print("Informe as notas do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media < 6:
    print(f"Aluno reprovado. Média: {media}")
else:
    print(f"Aluno aprovado! Média: {media}")

print(type(media))
