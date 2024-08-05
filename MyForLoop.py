#Demonstração do uso for/range

print("Digite o valor máximo desejado: ")
numero = int(input())

print("Segue, os números desejados: ")

for i in range(0, numero):
    print(i)



#Demonstração do for SEM o range

print("Digite o nome desejado: ")
nome = input()

print("Vamos soletrar cada letra? ")

for i in nome:
    print(i)
