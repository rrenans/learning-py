from abc import ABC, abstractmethod


"""
Sempre que ter uma classe pai sendo ela abstrata e com métodos abstratos
que force que esse método seja sobescrito em classes filhas, isso será polimorfismo
"""



class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.fala('Um assunto')
c.fala('Um outro assunto')