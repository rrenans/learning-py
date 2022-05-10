from Conta import Conta


class ContaPoupanca(Conta):
    # def __init__(self, agencia, numero, saldo):
    #     super().__init__(agencia, numero, saldo)

    def sacar(self, valorSacado):
        if self.saldo < valorSacado:
            print('Saldo insuficiente')
            return

        self.saldo -= valorSacado
        self.info()