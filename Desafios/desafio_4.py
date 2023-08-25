valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# Itera, baseado no período em anos, para o cálculo do valorFinal com os juros.
for _ in range(periodo):
    valor_final *= 1 + taxa_juros

print(f"Valor final do investimento: R$ {valor_final:.2f}")
