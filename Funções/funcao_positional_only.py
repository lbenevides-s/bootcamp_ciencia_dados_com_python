def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
		print(modelo, ano, placa, marca, motor, combustivel)

#Exemplo válido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


#Exemplo inválido
#criar_carro(modelo="Palio", ano=1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")