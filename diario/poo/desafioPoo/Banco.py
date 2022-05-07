class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    # @property
    # def agencias(self):
    #     return self._agencias
    # @property
    # def clientes(self):
    #     return self._clientes
    # @property
    # def contas(self):
    #     return self._contas

    # @agencias.setter
    # def agencias(self, agencias):
    #     self._agencias = agencias
    # @clientes.setter
    # def clientes(self, clientes):
    #     self._clientes = clientes
    # @contas.setter
    # def contas(self, contas):
    #     self._contas = contas

    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)

    def inserir_contas(self, contas):
        self.contas.append(contas)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
