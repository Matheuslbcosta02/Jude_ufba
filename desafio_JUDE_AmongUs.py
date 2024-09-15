numero_jogadores = int(input())

assassinatos_jogadores = list(map(int,input().split()))

for i in range(numero_jogadores):
    for j in range(0, numero_jogadores - i - 1):
        if assassinatos_jogadores[j] > assassinatos_jogadores [j + 1]:
            assassinatos_jogadores[j],assassinatos_jogadores[j + 1] = assassinatos_jogadores[j + 1],assassinatos_jogadores[j]


print(" ".join(map(str,assassinatos_jogadores)))

