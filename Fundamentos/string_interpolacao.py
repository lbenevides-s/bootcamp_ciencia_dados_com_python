nome = "Joãozinho"
idade = 24
profissao = "Programador"
linguaguem = "Python"
saldo = 45.435
dados = {"nome": "Guilherme", "idade": "28"}


print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")

print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}")

