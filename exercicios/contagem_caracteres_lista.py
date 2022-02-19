def contar_caracteres(s):

    """
        Função que conta os caracteres de uma string

        :param s: string a ser contada

        Esta função apenas imprime os dados
    """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter_atual in caracteres_ordenados[1:]:
        if caracter_atual == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter_atual
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('renan') # pode mudar a string para testar
    print()
    contar_caracteres('banana')
