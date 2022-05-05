"""
EM PYTHON É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!?!?)
"""

class PaiDeA:
    nome = 'Teste'

A = type(
    'A',
    (PaiDeA,),
    {
        'attr': 'Olá Mundo!'
    }
)

a = A()
print(type(a))
print(a.nome)
print(a.attr)

# ----------------------------------

# class Meta(type):
#     def __new__(mcs, name, bases, namespace):
#         if name == 'A':
#             return type.__new__(mcs, name, bases, namespace)
#         if 'attr_classe' in namespace:
#             del namespace['attr_classe']

#         return type.__new__(mcs, name, bases, namespace)

# class A(metaclass=Meta):
#     attr_classe = 'Valor A'

# class B(A):
#     attr_classe = 'Valor B'

# b = B()
# print(b.attr_classe)