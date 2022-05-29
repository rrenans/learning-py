"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
FIla (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitoscolaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados.
"""

from time import sleep
from collections import deque
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')

livro_removido = livros.pop()
# print(livros, livro_removido ─)


# fila = deque()
# fila.append('João')
# fila.append('Gabriel')
# fila.append('Maria')
# fila.append('Fernanda')

# print(f'Saiu: {fila.popleft()}')

# for nome in fila:
#     print(nome)

# fila = deque(maxlen=5)
# fila.extend([1, 2, 3, 4])
# fila.append(5)
# fila.append(6)

# print(fila)
fila = deque(maxlen=10)
for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)
