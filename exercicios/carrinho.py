
"""
Objetivo pegar o total de valores de cada produto
"""

carrinho = []
carrinho.append(('Produto 1', 30.50))
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))


total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)