meses_contrato , valor_carro = map(float, input().split())
meses_contrato = int(meses_contrato)
saldo = 0.0
meses_ate_valor = 0


for i in range(1, meses_contrato + 1):
    entrada_valores = float(input())
    saldo += entrada_valores
    
    if(saldo >= valor_carro and meses_ate_valor == 0):
        meses_ate_valor = i
##garantir que meses_ate_valor só sera atualizado uma vez pelo i, quando atingir valor 

        
        
if(meses_ate_valor > 0):
    saldo -= valor_carro
    print(f"{meses_ate_valor} {saldo:.2f}")

else:
    
    print(f"0 {saldo:.2f}")
    



