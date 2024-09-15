zagueiro, goleiro = map(str,input().split())
drible,chute = map(str,input().split())

if (zagueiro == drible):
    print("Bloqueado")

else:
    print("Driblado")
    if (goleiro != chute):
        print("Gol")
    else:
        print("...e o goleiro pega")
