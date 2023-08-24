MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe a sua idade: "))

# Exemplo 1
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH!")

# Exemplo 2
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")
else:
    print("Ainda não pode tirar CNH!")

# Exemplo 3
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")
elif idade == IDADE_ESPECIAL:
    print("Você pode somente realizar as aulas teóricas!")
else:
    print("Ainda não pode tirar CNH!")


