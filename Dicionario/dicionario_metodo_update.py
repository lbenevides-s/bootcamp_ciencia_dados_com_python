contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "3333-3333"},
}

contatos.update({"joao@gmail.com": {"nome": "Jão"}})
print(contatos)

contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "3333-9898"}})
print(contatos)