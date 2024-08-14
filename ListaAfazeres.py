#Criando lista para armazenar tarefas
afazeres = []

#loop para adicionar tarefas à lista
for i in range(0,5):
    afazeres.append(input("Digite uma tarefa: "))

#loop para verificar se cada tarefa foi executada
for x in range(0,len(afazeres)):
    print(f"A {x+1}° tarefa foi executada? (S/N)")
    statusTarefa = input()
    #verificação se resposta do usuário é positiva
    if statusTarefa == "S" or statusTarefa == "s":
        #verificando necessidade de adicionar outra tarefa à lista
        print("Deseja cadastrar nova tarefa? (S/N)")
        statusCadastro = input()
        #verificação se resposta do usuário é positiva
        if statusCadastro == "S" or statusCadastro == "s":
            #deletando a tarefa concluída da lista
            del(afazeres[x])
            novaTarefa = input("Digite a tarefa nova: ")
            #adicionando nova tarefa à lista
            afazeres.append(novaTarefa)
        else:
            #deletando a tarefa concluída da lista
            del(afazeres[x])
            #adiconado valor apenas para manter o índice de elementos
            afazeres.append("Ok")
            continue
    else:
        continue

#ordenando a lista em ordem alfabética
afazeres.sort()

#exibindo lista na tela
print(afazeres)
