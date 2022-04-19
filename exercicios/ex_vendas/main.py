
# import vendas.calc_preco
from vendas import calc_preco
from vendas.formata import preco_formata

preco = 49.90
preco_aumento = calc_preco.aumento(valor=preco, porcentagem=15, formata=True)
print(preco_aumento)

preco_reducao = calc_preco.reducao(valor=preco, porcentagem=15, formata=True)
print(preco_reducao)

print(preco_formata.real(69.90))