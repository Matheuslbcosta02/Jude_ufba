linhas_matriz , colunas_matriz = map(int,input().split())
matriz = []
for l in range(linhas_matriz):
    valores = [int(x) for x in input().split()]
    matriz.append(valores)

#print(matriz)

ovos_snake = 0

for ll in range(linhas_matriz):
    if ll % 2 == 0 :
       for cc in range(colunas_matriz):
           ovos_snake += matriz[ll][cc]
    else:
        for cc in range(colunas_matriz - 1 , -1 , -1):
            ovos_snake += matriz[ll][cc]

print(ovos_snake)
