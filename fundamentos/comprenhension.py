#! /usr/bin/python3 
#estrutura
#[expressão for intem in (lista de itens) if condicional]
dobro = [i*2 for i in range(10)] #gera tudo de uma vez
print(dobro)


numeros_sobre_demanda_generator = (i*2 for i in range(10))
for numero in numeros_sobre_demanda_generator:
	print(numero)
