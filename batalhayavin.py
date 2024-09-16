dimensao , teletransportes = map(int, input().split())
inimigosabatidos = 0
matriz = []

for i in range(dimensao):
    numeros = list(map(int,input().split()))
    matriz.append(numeros)

coordenadas = []

for j in range(teletransportes):
    linhacoluna = list(map(int,input().split()))
    coordenadas.append(linhacoluna)



for teste in range(teletransportes):
    linha , coluna = coordenadas[teste]
    for verificarlinha in range(linha,-1,-1):
        if matriz[verificarlinha][coluna] == 1 :
            inimigosabatidos += 1
            break

print(inimigosabatidos)




