
from vendas.formata import preco_formata

def aumento(valor, porcentagem, formata=False):
    resultado = valor + (valor * (porcentagem / 100))

    if formata:
        return preco_formata.real(resultado)
    else:
        return resultado

def reducao(valor, porcentagem, formata=False):
    resultado = valor - (valor * porcentagem / 100)
    
    if formata:
        return preco_formata.real(resultado)
    else:
        return resultado