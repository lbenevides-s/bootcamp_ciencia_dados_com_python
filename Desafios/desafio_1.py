saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())


saldo_atual += valor_deposito
saldo_atual -= valor_retirada


print(f"Saldo atualizado na conta: {saldo_atual:.1f}")
