controle = 1
geleia = 0
tradicional = 0

N = int(input())

while(controle <= N):
    pedido = input()
    controle += 1
    if(pedido == '10'):
        tradicional += 1
    
    elif(pedido == '11'):
        geleia += 1

if(tradicional > geleia):
    print("Tradicional")

else:
    print("Geleia")

