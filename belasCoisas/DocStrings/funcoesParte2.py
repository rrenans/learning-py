"""
Descrição rápida e simples.

Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum.
"""


variavel_1 = 'valor1'

def soma(x, y):
    """
    Soma de x e y
    
    :param x: Primeiro número
    :type x: int or float
    :param y: Segundo número
    :type y: int or float

    :return: A sma entre x e y
    :rtype: int or float
    """
    return x + y

def multiplica(x, y, z=None):
    """
        Soma x, y, z

        Multiplica x, y, z. O programador por omitir a variável z caso não tenha
        necessidade de usá-la

        :param x Primeiro número
        :type x: int or float
        :param y: Segundo número
        :type y: int or float
        :param z: Terceiro número (optional)
        :type z: int, float ou None

        :return: A soma entre X, Y e Z
        :rtype: int or float
    """
    if z:
        return x * y
    else:
        return x * y * z

variavel_2 = 'valor 1'
variavel_3 = 'valor 2'
variavel_4 = 'valor 3'
