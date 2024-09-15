#Harry linha \\\\\ Ron coluna
dimensao = int(input())
matriz = []

for l in range(dimensao):
    linhas = [int(x) for x in input().split()]
    matriz.append(linhas)

##print(matriz)

X,Y = map(int,input().split())

harry = 0
ron = 0
harry = sum(matriz[X])

ron = sum(matriz[linhas][Y] for linhas in range(dimensao))

intersseccao = matriz[X][Y]
if X > Y :
    ron -= intersseccao

elif X == Y :
    harry -= intersseccao

else:
    harry -= intersseccao

print(f"Harry {harry}")
print(f"Ron {ron}")
