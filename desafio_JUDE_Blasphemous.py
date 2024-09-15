n = int(input())
fase = list(map(int,input().split()))
vida = int(input())
vidaAtual = vida

for caminho in fase:
    if caminho == 0:
        continue
    elif caminho == 1:
        vidaAtual = vida
    else:
        vidaAtual -= caminho
        if vidaAtual < 1:
            break

if vidaAtual < 1:
    print("You Died")

else:
    print("Yes, you can")

