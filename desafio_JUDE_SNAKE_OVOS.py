#quantidades de ovos coletados pelo snake em cada caçada -> Q1,Q2,Q3
Q1,Q2,Q3 = map(int,input().split())

#quantidade de ovos envenenados em cada caçada -> E1,E2,E3
E1,E2,E3 = map(int,input().split())

#ovo envenenado -> snake dorme e perde dois ovos, além do envenenado -> ou seja cada evenenado é menos 3
#quantidade de ovos que de fato sobraram pro snake em cada caçada -> OVOS_1, OVOS_2, OVOS_3
OVOS_1 = Q1 - (E1 * 3) 
OVOS_2 = Q2 - (E2 * 3)
OVOS_3 = Q3 - (E3 * 3)

#QUANTIDADE DE OVOS QUE SOBRARAM ao todo para o snake -> OVOS
OVOS = OVOS_1 + OVOS_2 + OVOS_3
print(f'{OVOS}')
