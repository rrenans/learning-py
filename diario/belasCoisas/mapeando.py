"""
Estudando função map(), com list comprehension e funções lambda
"""
from dados import *

nova_lista = map(lambda x: x * 2, lista_aleatoria)
nova_lista = [x * 2 for x in lista_aleatoria]
print(lista_aleatoria)
print(list(nova_lista))

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

precos = map(lambda p: p['preco'], produtos)
for preco in precos:
    print(preco)


nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)

