numero_obstaculos = int(input())

alturas = list(map(int,input().split()))

altura_maxima_saltador = int(input())

obstaculos_saltados = 0

for i in range(len(alturas)):
    if alturas[i] <= altura_maxima_saltador :
        obstaculos_saltados += 1
    else:
        break

if obstaculos_saltados == len(alturas):
    print(obstaculos_saltados)
    print(1)

else:
    print(obstaculos_saltados)
    print(0)
    

