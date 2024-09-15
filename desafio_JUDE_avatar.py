numero_dobradores = int(input())

# 1 agua - 2 terra - 3 fogo - 4 ar

habilidade_dobradores = list(map(int,input().split()))

identificador_dobradores = list(map(int,input().split()))

elemento_escolhido = int(input())

saida = []

for i in range(len(habilidade_dobradores)):
    if elemento_escolhido == habilidade_dobradores[i]:
        saida.append(identificador_dobradores[i])

if elemento_escolhido not in habilidade_dobradores:
    print("Nenhum")
else:
    print(" ".join(map(str,saida)))
        


