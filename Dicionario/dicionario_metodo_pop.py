contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "3333-3333"},
}

# Removendo uma key usando pop
print(contatos.pop("joao@gmail.com"))

# resultado após execução do método pop
print(contatos.pop("joao@gmail.com", {}))