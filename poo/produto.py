class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter -> obter um valor (.)
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco # por convenção, utiliza-se o nome da variável, mas, com um underline na frente

    # Setter -> configurando um valor(=)
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


    @preco.setter # o decorador do setter será sempre o nome do atributo com .setter em seguida
    def preco(self, valor):
        if isinstance(valor, str): # checando se o valor é uma string
            valor = float(valor.replace('R$', ''))

        self._preco = valor