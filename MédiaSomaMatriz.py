matriz = [[0, 0], [0, 0]]
soma = 0
media = 0

for x in range(0,2):
    for y in range(0,2):
        matriz[x][y] = int(input(f"Digite o valor da linha {x+1} e coluna {y+1}: "))

for x in range(0,2):
    for y in range(0,2):
      soma += matriz[x][y]
     
print(soma)     
media = soma/4
print(media)