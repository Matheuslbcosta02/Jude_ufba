sapos , pedras = map(int,input().split())

caminho = [0] * pedras
tamanho_pulo = []

for i in range(sapos):
    x = int(input())
    tamanho_pulo.append(x)

for pulo in tamanho_pulo:
    for j in range(0,pedras,pulo):
        caminho[j] = 1

print(" ".join(map(str,caminho)))





