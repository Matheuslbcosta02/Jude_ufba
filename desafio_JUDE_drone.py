dimensao = int(input())
linhas = dimensao

matriz = []

for l in range(linhas):
        numero_especies = list(map(int,input().split()))
        matriz.append(numero_especies)

dimensao_coordenadas = int(input())
matriz_coordenadas = []
valor = 0

for lc in range(dimensao_coordenadas):
        X,Y = list(map(int,input().split()))
        valor += matriz[X][Y]

print(valor)