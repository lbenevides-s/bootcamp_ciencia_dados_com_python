ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for quantidade in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Ordena a lista de ativos
ativos.sort()

# Imprime os ativos ordenados
for ativo in ativos:
    print(ativo)