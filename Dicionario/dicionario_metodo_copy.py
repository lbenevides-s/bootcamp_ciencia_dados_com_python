contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "3333-3333"},
}

copia = contatos.copy()
copia["joao@gmail.com"] = {"nome": "Jão"}

contatos["joao@gmail.com"]
print(contatos)

copia["joao@gmail.com"]
print(copia)