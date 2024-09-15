dimensao , teletransportes = map(int, input().split())
matriz = []
for linhas in range(dimensao):
    valores = [int(x) for x in input().split()]
    matriz.append(valores)

naves_destruidas = 0

for coordenadas in range(teletransportes):
    X,Y = map(int,input().split())
    if matriz[X-1][Y] == 1:
        naves_destruidas += 1

print(naves_destruidas)
