#versao 1
esta_chovando = True
'Hoje estou com as roupas' + ('opcao falsa', 'opcao verdadeira')[esta_chovendo]

#versao 2
esta_chovendo = True
'Hoje estou com as roupas' + ('opcao verdadeira' if esta_chovendo else 'opcao falsa')
