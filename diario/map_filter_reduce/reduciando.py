
from dados import *
from functools import reduce


# soma_lista = reduce(lambda acumulador, item: item + acumulador, lista_aleatoria, 0)
# print(soma_lista)

# soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
# print(soma_precos / len(produtos))

soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idade / len(pessoas))