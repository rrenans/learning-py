""" Documentação deste módulo

Ele não faz nada, mas é só um exemplo pra você.
Typing - https://docs.python.org/3/library/typing.html
"""

x: int = 10
y: float = 10.5
z: bool = False

def funcao(p1: float, p2: str, p3: dict) -> float: # esse float, faz referência ao tipo de retorno da função
    # return p1, p2, p3
    return 10.10

print(funcao(10.1, 'str', {}))

# from typing import Union
# def funcao2() -> Union[list, dict]: Caso queira retornar mais de um valor em uma função
#     return []