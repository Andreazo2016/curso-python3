while (Condicao):
	o que vai ser feito


#caso de uso: quando vc não tem uma quantidade determinada de repeticao
while True:
   print("")


#Quando vc tem uma quantidade definidade de repetição
for item in lista.items():

#percorrer uma string
string = "meu nome"
for letra in string:
   print(letra)

#percorrer uma lista
lista = ["Andreazo","Lurdinha"]
#acessa index e item
for indx, item in enumerate(lista): 
   print(item)


#pecorrer tupla
semana = ("Segunda","terça","quarta")
for dia in semana:
  print(dia) 


#percorrer dicionarios
pessoa = {"nome":"Andreazo", "idade":30}

#percorre as chaves
for chave in pessoa:
    print(f'chave eh: {chave}')

#percorre os valores
for valor in pessoa.values():
   print(f'values: {valor}')

#pecorrer chave e valor
for chave, valor in pessoa.items():
   print(f'chave : {chave} e valor: {valor}')




