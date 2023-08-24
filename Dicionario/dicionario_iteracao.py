contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "3333-3333"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "3333-4444"},
    "luana@gmail.com": {"nome": "Luana", "telefone": "3333-9696"}, 
    "mel@gmail.com": {"nome": "Mel", "telefone": "3333-9898"},
}

for chave in contatos:
    print(chave, contatos[chave])
    print()

# Forma mais declarativa e legível
for chave, valor in contatos.items():
    print(chave, valor)
    print()