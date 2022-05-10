# Composição
# a classe endereço está sendo composta pela classe cliente

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Enderecos(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Enderecos:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado