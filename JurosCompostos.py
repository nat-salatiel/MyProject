valorProduto = int(input("Insira o valor do produto: "))
qtdParcelas = int(input("Informe a quantidade de parcelas: "))
taxaJuros = int(input("Informe a taxa de juros: "))
taxaJuros = taxaJuros * 0.01
tempoAnos = int(input("Qual o período em anos do pagamento? "))
montante = 0


#juros = valorProduto * taxaJuros * qtdParcelas
#valorParcela = (valorProduto / qtdParcelas) + juros

#for i in range(0 , qtdParcelas):
montante = valorProduto * (1+(taxaJuros/qtdParcelas))**(qtdParcelas*tempoAnos)
print(montante)