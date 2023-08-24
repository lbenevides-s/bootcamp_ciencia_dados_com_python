contatos = {
    "joao@gmail.com": {"nome": "João", "telefone": "3333-3333"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "3333-4444"},
    "luana@gmail.com": {"nome": "Luana", "telefone": "3333-9696"}, 
    "mel@gmail.com": {"nome": "Mel", "telefone": "3333-9898"},
}
resultado = print("joao@gmail.com" in contatos)# True

resultado = print("rafaelzinho@gmail.com" in contatos) # False

resultado = print("idade" in contatos["joao@gmail.com"]) # False

resultado = print("telefone" in contatos["giovana@gmail.com"])  # True