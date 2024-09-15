SC_TOTAL = 30
MM_TOTAL = 6
CK_TOTAL = 3

SC, MM, CK = map(int, input().split())

if(SC < 30):
    SC_faltando = SC_TOTAL - SC
    MM_faltando = MM_TOTAL - MM
    CK_faltando = CK_TOTAL - CK
    print(f'{SC_faltando} {MM_faltando} {CK_faltando}')

else:
    print("PROXIMO MUNDO")

