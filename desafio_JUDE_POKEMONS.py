#K (Kanto) J (Johto) H (Hoenn)

#convertendo as variáveis de string para inteiros 
K1,J1,H1 = map(int,input().split())
K2,J2,H2 = map(int,input().split())

K = K1 + K2
J = J1 + J2
H = H1 + H2

if (0 <= K,J,H <= 100):
    print(f"{K} {J} {H}\n")