#Classificação de times.

time = input("Informe o seu time: ")
print("Posições: ")
print("1° ao 16° lugar")
posicao = int(input("Qual é a posição do seu time? Digite o número correspondente: "))

if posicao == 1:
    print(f"Campeão! {time} em 1° lugar!")
elif posicao >= 2 and posicao <= 6:
    print(f"Libertadores! {time} em {posicao}° lugar!")
elif posicao >= 7 and posicao <= 12:
    print(f"Sul-Americana! {time} em {posicao}° lugar!")
elif posicao >= 13 and posicao <= 16:
    print(f"Rebaixado! {time} em {posicao}° lugar!")
else:
    print("Opção inválida.")