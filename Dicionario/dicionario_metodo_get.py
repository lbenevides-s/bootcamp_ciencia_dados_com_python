contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "3333-3333"},
}


# contatos["chave"] #KeyError

print(contatos.get("chave")) #None
print(contatos.get("chave", {})) # {}
print(contatos.get("joao@gmail.com", {}))
