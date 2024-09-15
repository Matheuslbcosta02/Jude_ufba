entrada = int(input())
horas = entrada//3600
minutos = (entrada%3600)//60
segundos = (entrada%3600)%60
print(f"{horas}h {minutos}m {segundos}s")
