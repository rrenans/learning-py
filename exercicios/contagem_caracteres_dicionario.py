def contar_caracteres(s):

    """
        Função que conta os caracteres de uma string

        :param s: string a ser contada

        Esta função imprime e retorna os dados
    """


    resultado = {}

    for caracter_atual in s:
        resultado[caracter_atual] = resultado.get(caracter_atual, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('renan')) # pode mudar a string para testar
    print()
    print(contar_caracteres('banana'))
