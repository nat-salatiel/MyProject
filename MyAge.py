#Demonstração do uso if/else/elif
print("Digite a sua idade: ")
idade = int(input())

if idade < 18:
    print("Você não é maior de idade!")
    print("Não poderá realizar a operação!")
elif idade >= 65:
    print("Você já está pronto para se aposentar?")
    print("Poderemos oferecer suporte técnico")
else:
    print("Você possui a idade mínima obrigatória! Operação autorizada.")

print("Obrigado por optar pelos nossos serviços!")