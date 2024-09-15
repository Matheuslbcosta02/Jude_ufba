# A -> Luther // B -> Diego // C -> Alisson // D -> Klaus // E -> Ben // F -> Victor
# #entrada são os anos para cada qual um deles viajou
    
A,B,C,D,E,F = map(int,input().split())
ano_vigente = 2023
int(ano_vigente)

tempo_A = (A - ano_vigente) * 2 
tempo_B = (B - ano_vigente) * 2
tempo_C = (C - ano_vigente) * 2
tempo_D = (D - ano_vigente) * 2
tempo_E = (E - ano_vigente) * 2
tempo_F = (F - ano_vigente) * 2



if (tempo_A < 0):
    tempo_A = tempo_A * (-1)

if (tempo_B < 0):
    tempo_B = tempo_B * (-1)

if (tempo_C < 0):
    tempo_C = tempo_C * (-1)

if (tempo_D < 0):
    tempo_D = tempo_D * (-1)

if (tempo_E < 0):
    tempo_E = tempo_E * (-1)

if (tempo_F < 0):
    tempo_F = tempo_F * (-1)


tempo_five = tempo_A + tempo_B + tempo_C + tempo_D + tempo_E + tempo_F

if (tempo_five < 0):
    tempo_five = tempo_five * (-1)
    
print(f"Luther {tempo_A}\nDiego {tempo_B}\nAlisson {tempo_C}\nKlaus {tempo_D}\nFive {tempo_five}\nBen {tempo_E}\nViktor {tempo_F}")

