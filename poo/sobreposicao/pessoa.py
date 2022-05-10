# Sobreposição de membros
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f' {self.nomeclasse} falando')

class Cliente(Pessoa):
    def comprar(self):
        print(f' {self.nomeclasse} comprando')

    # def falar(self):
    #     print(f'Estou em Cliente')

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        # Pessoa.falar(self)
        # Cliente.falar(self)
        super().falar() # primeiro está chamando o método falar da superclasse(pessoa)
        print(f' {self.nomeclasse} falando outra coisa com o {self.sobrenome}') # depois chamando o método dele mesmo