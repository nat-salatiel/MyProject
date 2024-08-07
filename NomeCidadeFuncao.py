def NomeeCidade(nome,cidade):
    if cidade =="Rio de Janeiro":
        print(f"Olá, {nome}! Seja Bem-vindo(a) à Cidade Maravilhosa!")
    else:
        print(f"Olá, {nome}, da cidade de {cidade}.")


nome = input("Digite seu nome: ")
cidade = input("De qual cidade você está digitando? ")

NomeeCidade(nome,cidade)