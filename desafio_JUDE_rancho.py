N, Q = map(int, input().split())

estoque = Q - N
testar_paridade = estoque % 2

if(testar_paridade == 0) and N <= Q:
    print("vendido")

else:
    print("sinto muito")
