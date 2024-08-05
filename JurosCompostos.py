valorProduto = int(input("Insira o valor do produto: "))
qtdParcelas = int(input("Informe a quantidade de parcelas: "))
taxaJuros = int(input("Informe a taxa de juros: "))

juros = valorProduto * taxaJuros * qtdParcelas
valorParcela = (valorProduto / qtdParcelas) + juros

for i in range(0 , qtdParcelas):

##não finalizado