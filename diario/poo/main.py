from pessoa import Pessoa
from produto import Produto
from baseDados import BaseDeDados

pessoa1 = Pessoa('Luiz', 29)
pessoa2 = Pessoa.por_ano_nascimento('João', 1987)

print(pessoa2.nome, pessoa2.idade)
print(pessoa1.gera_id(), pessoa1.get_ano_nascimento())
print()

produto1 = Produto('CANecA', 25)
produto1.desconto(10)
print(produto1.nome, produto1.preco)
produto2 = Produto('CAmiSETA', 'R$ 50')
produto2.desconto(10)
print(produto2.nome, produto2.preco)
print()

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Jorge')
bd.apagar_cliente(2)
bd.listar_clientes()
print(bd._BaseDeDados__dados)
print()
