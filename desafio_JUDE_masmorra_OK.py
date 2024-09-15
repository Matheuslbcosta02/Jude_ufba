portas_abertas = int(input())
nivel_personagem = 1

for i in range(1, portas_abertas + 1):
    
    entrada, numero = input().split()
    numero = int(numero)
    
    if entrada == 't':
        nivel_personagem += numero
        if nivel_personagem >= 5:
            print("Aventura concluida")
            break

    elif entrada == 'm':
        nivel_monstro = numero
        
        print("Combate iniciado")
        if nivel_personagem >= nivel_monstro:
            print("VITORIA")
            nivel_personagem += 1
            if nivel_personagem >= 5:
                print("Aventura concluida")
                break
        else:
            print("Derrota! Fim da aventura")
            break

    elif entrada == 'b':
        nivel_personagem -= numero
        if nivel_personagem < 0:
            nivel_personagem = 0
