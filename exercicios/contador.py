"""
    O objetivo desse exercício é criar um contador que mostre 
    ordem crescente e ordem decrescente
    ex: 0 10
        1 9
        2 8
        3 7
        4 6
        5 5
        6 4
        7 3
        8 2
"""

# Minha solução
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
for v1, v2 in enumerate(lista):
    print(v1, v2)

print('\n --------------- \n' )

# Solução do professor
for v1, v2 in enumerate(range(10, 1, -1)):
    print(v1, v2)
