"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo.
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clients e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupança e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrição acima)
"""

from Cliente import Cliente
from Banco import Banco
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

banco = Banco()

cliente1 = Cliente('Renan', 18)
cliente2 = Cliente('Maria', 25)
cliente3 = Cliente('João', 27)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 521463, 0)
conta3 = ContaPoupanca(3331, 364125, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_contas(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_contas(conta2)

banco.inserir_clientes(cliente3)
banco.inserir_contas(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(10)
else:
    print('Cliente não autenticado')

print()

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20) # aqui deveria constar saldo insuficiente, creio que por conta do polimorfismo, isto não acontece
else:
    print('Cliente não autenticado')