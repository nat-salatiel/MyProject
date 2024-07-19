#Identificando se o usuário pode se aposentar

sexo = input("Qual é o seu sexo? Digite Masculino ou Feminino: ")
idade = int(input("Qual a sua idade? "))
tempoContribuicao = int(input("Quantos anos de contribuição você possui? "))


if sexo == "Feminino" and idade >= 62 and tempoContribuicao >=15 :
    print("Você possui a idade necessária para se aposentar!")
elif sexo == "Feminino" and tempoContribuicao >= 30:
    print("Você possui o tempo de contribuição necessário para se aposentar!")
elif sexo == "Masculino" and idade >= 65 and tempoContribuicao >=20 :
    print("Você possui a idade necessária para se aposentar!")
elif sexo == "Masculino" and tempoContribuicao >= 35:
    print("Você possui o tempo de contribuição necessário para se aposentar!")
else:
    print("Infelizmente, você ainda não pode se aposentar.")
