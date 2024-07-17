

print("Informe a nota do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2 )/2

if media >= 6:
    print(f"Aluno aprovado direto!. Média: {media}")
elif media > 4 and media < 6:
    print(f"Aluno em recuperação! Média: {media}")
    recuperacao = float(input("Informe a nota da recuperação: "))
    if recuperacao >= 5:
        print(f"Aluno aprovado na recuperação! Nota: {recuperacao}")
    else:
        print(f"Aluno reprovado na recuperação. Nota: {recuperacao}")