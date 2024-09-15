C,c,X = map(int, input().split())
cubo_grande = C ** 3
cubo_menor = (c ** 3) * X

if(cubo_menor >= cubo_grande):
    print("Eh possivel")

else:
    print("!Eh possivel")
    