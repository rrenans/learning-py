from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numeroConta, saldo):
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.saldo = saldo
    
    # @property
    # def agencia(self):
    #     return self._agencia
    # @property
    # def numeroConta(self):
    #     return self._numeroConta
    # @property
    # def saldo(self):
    #     return self._saldo

    # @saldo.setter
    # def saldo(self, saldo):
    #     self._saldo = saldo

    def depositar(self, valorDepositado):
        self.saldo += valorDepositado
        self.info()

    @abstractmethod
    def sacar(self, valorSacado):
        pass

    def info(self):
        print(f'Agência: {self.agencia} ' 
              f'Conta: {self.numeroConta} '
              f'Saldo: {self.saldo}')