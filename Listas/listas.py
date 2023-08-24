frutas = ["laranja", "maça", "uva"]
print(frutas)

frutas = []
print(frutas)
letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(f"numeros pares: {pares}")

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [quadrado ** 2 for quadrado in numeros]
print(quadrado)