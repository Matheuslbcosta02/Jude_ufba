quantidade_secoes= int(input())

comprimento_secoes = list(map(int,input().split()))

meio = 0    

for i in comprimento_secoes:
    meio += i

meio //= 2
##print(meio)

soma = 0

for i in range(quantidade_secoes):
    if soma != meio :
        soma += comprimento_secoes[i]
    else:
        print(i)
        break


