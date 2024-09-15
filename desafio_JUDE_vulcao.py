limite_pressao = int(input())
controle = 0
pressao_entrada = 1

while(pressao_entrada != 0):
    pressao_entrada = int(input())
    if(pressao_entrada > limite_pressao):
        controle += 1

if(controle != 0):
    print("ALARME")

else:
    print("O Havai pode dormir tranquilo")
