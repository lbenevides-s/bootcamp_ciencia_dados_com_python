saldo = 0

while True:
    valor = float(input())
    
    if valor > 0:
        saldo += valor
        print(f"Depsito realizado com sucesso!\nSaldo atual: R$ {valor:.2f}")
        break
    elif valor == 0:
        print("Encerrando o programa...")
        break  
    else:
        print("Valor invalido! Digite um valor maior que zero")
        
