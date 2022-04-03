from dados import *

# opção com filter
# nova_lista = filter(lambda x: x > 5, lista_aleatoria)
# print(list(nova_lista))

# opção com list comprehension
# nova_lista = [x for x in lista_aleatoria if x > 5]
# print(list(nova_lista))

# nova_lista = filter(lambda p: p['preco'] > 50, produtos)
def filtra(produto):
    if produto['preco'] > 50:
        return True

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)


