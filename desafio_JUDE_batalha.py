defesa_oponente, meu_ataque = map(int, input().split())
ataques_necessarios = 0

while(defesa_oponente > 0):
    defesa_oponente -= meu_ataque
    meu_ataque -= 1
    ataques_necessarios += 1
    if(meu_ataque <= 0):
        break


if (defesa_oponente <= meu_ataque):
    print(f"{ataques_necessarios}")

else:
    print("F")




