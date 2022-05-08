from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, numeroConta, saldo, limite=100):
        super().__init__(agencia, numeroConta, saldo)
        self.limite = limite
    
    # @property
    # def limite(self):
    #     return self._limite

    def sacar(self, valorSacado):
        if (self.saldo + self.limite) < valorSacado:
            print('Saldo insuficiente')
            return

        self.saldo -= valorSacado
        self.info()