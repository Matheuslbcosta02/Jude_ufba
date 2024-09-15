X , Y = map(int,input().split())

if (X>0 and X<100):
    if(Y>0 and Y<100):
        if(X>70 or Y>70):
            print("Coordenada valida e o navio esta longe")
        elif(X<=70 and Y<=70):
            print("Coordenada valida e o navio esta perto")

else:
    print("Coordenada invalida")
