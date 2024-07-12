#Inserção de dados
print("Digite o nome da empresa:")
NomeDaEmpresa = input()

print("Digite o nome do Gestor:")
NomeGestor = input()

print("Digite o seu nome:")
NomeFuncionario = input()

print("Informe o seu cargo:")
CargoAtual = input()

print("Informe a data de início do aviso prévio:")
InicioAvisoPrevio = input()

print("Informe a data de término do aviso prévio:")
TerminoAvisoPrevio = input()

print("Informe o local:")
Local = input()

print("Informe a data:")
Data = input()

#Exibição do texto na tela, com os dados coletados
print(f"À {NomeDaEmpresa}, \n Prezado {NomeGestor}, \n venho, por meio desta carta, comunicar formalmente o meu pedido de demissão, do cargo de {CargoAtual}.")
print(f"Estarei à disposição da empresa durante o aviso prévio, no período de {InicioAvisoPrevio} à {TerminoAvisoPrevio}.") 
print(f"{Local} \n{Data} \n{NomeFuncionario}")
