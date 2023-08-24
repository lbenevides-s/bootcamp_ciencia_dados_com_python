contato = {"nome": "João", "telefone": "3333-3333"}
print(contato)

# Não funciona porque já existe "nome" em contato
contato.setdefault("nome", "Giovana")
print(contato)

# Funciona porque ainda não existia "idade" em contato
contato.setdefault("idade", 28)
print(contato)

