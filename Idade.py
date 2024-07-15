#calculando a idade futura do usuário

anoNascimento = int(input("Informe o ano em que você nasceu: "))
anoFuturo = int(input("Informe o ano que deseja analizar: "))

anoAtual = 2024
idadeAtual = anoAtual -anoNascimento
idadeFutura = idadeAtual + (anoFuturo - anoAtual)

print(f"Sua idade no ano de {anoFuturo} será {idadeFutura} anos")