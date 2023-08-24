#Exemplos de uso de métodos da classe String

curso = "python "

print(curso.upper()) #Todas as letras para maiúsculas
print(curso.lower()) #Todas as letras para minúsculas
print(curso.title()) #Apenas a primeira letra para maiúscula

text = "  Hello World    "

print(text + "!")
print(text.strip() + "!")
print(text.lstrip() + "!")
print(text.rstrip() + "!")

menu = "Python"

print(menu.center(14, "#"))
print("-".join(menu))

