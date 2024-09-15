import math

X , Y = map(int, input().split())
controle = Y * 9
falta = (X - controle)/ 9
saida = math.ceil(falta)

if(controle < X):
    print(f"Precisa de mais difusores!")
    print(saida)

else:
    print("Lar doce lar.")
