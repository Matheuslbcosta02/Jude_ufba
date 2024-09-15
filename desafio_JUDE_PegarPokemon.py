linhas , colunas = map(int,input().split())
matriz = []
quantidade = 0

for linha in range(linhas):
        valores = [int(x) for x in input().split()]
        matriz.append(valores)


tipo_pokemon = int(input())


for l in range(linhas):
        for c in range(colunas):
                if matriz[l][c] == tipo_pokemon:
                        quantidade += 1

print(f"Ash pegou {quantidade} pokemon")




