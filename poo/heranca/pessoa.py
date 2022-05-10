# Herança Simples

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')