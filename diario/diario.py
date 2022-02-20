"""
    0. Obs:

        << import this >>
        doc funções built-in = https://docs.python.org/3/library/stdtypes.html e
                                https://docs.python.org/3/library/functions.html
        type() = mostra o tipo do dado. Ex: print(type(1))
        # (cerquilha) = para comentários
        \n = quebra de linha
        bool() = retorna True ou False
        int() = pode converter um dado primitivo para inteiro
        float() = pode converter um dado primitivo para flutuante
        format() = para formatar alguma string
        input() = recebe uma string, o usuário que digita
        print() = imprime qualquer coisa
        len() = retorna a quantidade de elementos de qualquer lista, retorna um int
        pass = placeholder
        continue = não vai ler as linhas de código posteriores
        break = ela finaliza o laço
        (x += 1) == (x = x + 1)
        iteração = passar por cada um dos elementos de uma string, passar pelos índices

    1. Formatando valores com modificadores:
        :s = Texto (str)
        :d = Inteiros (int)
        :f = Números de ponto flutuante (float)
        :.(Número de casas decimais)f = Quantidade de casas decimais (float)
            :.2f = está dizendo que vai ter apenas duas casas decimais
        :(Caractere) (> ou < ou ^) (Quantidade) (Tipo = s, d, f)
            > = Esquerda
            < = Direita
            ^ = Centro

    2. Fatiamento de string:
        [início:fim:passo]
            Ex: texto = 'Morango e Banana'
                 print(texto[1:15:2]) = Ele inicia no índice 1, termina no indíce 15 e pula de 2 em 2

    3. Operadores Aritméticos:
        + = Adição ou Concatenação (caso de duas strings)
        - = Subtração
        * = Multiplicação
        / = Divisão (resultado com ponto flutuante)
        // = Divisão (resultado é arredondado (número inteiro))
        ** = Exponenciação
        % = Resto da divisão entre um número e outro
        () = Altera a precedência dos operadores

    4. Operadores Relacionais:
        == = Igual.
            Ex: Um único igual significa "recebe", enquanto dois sinais de iguais significam "igual"
        > = Maior
        >= = Maior ou igual
        < = Menor
        <= = Menor ou igual
        != = Diferente

    5. Operadores Lógicos:
        and = E
        or = Ou
        not = Não
        in = Está em
        not in = Não está em

    6. Tipos básicos:
        str (string) = "textos que estão dentro de aspas, sejam elas simples ou duplas"
            Ex: print("Esse é 'meu' texto") = Nesse exemplo mostra que as aspas simples podem aparecer dentro de
                                                aspas duplas. Complementando, aspas duplas também podem aparecer
                                                dentro de aspas simples.
                print("Esse é meu \"texto\"") = Nesse exemplo, a barra invertida serve como um caractere de escape,
                                                assim é possível ver uma aspa dupla dentro de outra. Mas não é uma
                                                prática legal nas últimas versões do python. Assim, é preferível que
                                                utilize a forma do exemplo acima.
                print(f'Esse é meu {variável}') = Nesse exemplo vemos a f-string, acredito que esta seja a melhor
                                                  para a formatação de uma string.
        int (inteiro) = 1, 2, 3...
        float (ponto flutuante) = 1.1, 2.0, 5.3...
        bool (booleado) = True, False

    7. Variáveis:
        Iniciar com letra, pode conter números, separar com _ ou letras Maiúsculas, são escritas com letras minúsculas
        Ex: nome = 'renan'
            idade = 17
            altura = 1.80
            e_maior = idade >= 18
            data_1 = True
            data_atual = 2022

    8. Condições:
        If = se
        Elif = ou se
        Else = se não
            Ex: if 1 == 0:
                    print("False")
                elif 1 == 2:
                    print("False")
                elif 1 == 1:
                    print("True")
                else:
                    print("Nada a ser impresso")

    9. Laços:
        While = Enquanto
            Ex: No código abaixo percebe-se duas variáveis em que seus nomes já são auto-explicativos
                contador = 1
                    conta de forma linear
                acumulador = 1
                    acumula valores ao longo do laço

                while contador <= 10:
                    print(contador, acumulador)

                    acumulador = acumulador + contador
                    contador += 1
                else:
                    print('Final do laço')
            Ex: No laço while podemos utilizar o contador para ele iterar uma string
                frase = 'O rato roeu a roupa do rei de roma' # Iterável
                tamanho_frase = len(frase)
                contador = 0

                while contador < 10: # Iteração / Iterar
                    # na linha abaixo o contador passa a ser o índice da frase e,
                    vai iterando a cada vez que o índice é mudado (contador é somado mais um número)
                    print(frase[contador], contador)
                    contador += 1

        For


    contadores
    acumuladores
    list
    tupla
    dicionário
    funções
    parâmetros
    docstring
    módulo
    import
    pacote
    empacotamento
    desempacotamento

"""

# print()
