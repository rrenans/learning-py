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
    continue = não vai ler as linhas de código posteriores. pula para o próximo laço
    break = ela finaliza o laço
    (x += 1) == (x = x + 1)
    iteração = passar por cada um dos elementos de uma string, passar pelos índices
    count() = conta valores
    range() = ela recebe três parâmetros, start(início), stop(fim), step(pulo).
        por padrão ela inicia em 1, é esperado um fim e pula de 1 em 1.
    split() = divide uma string em uma lista
        var = 'O Brasil é o país do futebol. O Brasil é penta'
        # cada vez que encontrar o parâmetro,
        # irá criar um novo índice em uma lista
        l1 = var.split(' ')
    join() = junta uma lista dentro de uma string / transformar uma lista em uma string
        # uma string passa a ser uma lista separada por ''
        # depois esta mesma lista passa a se tornar uma string separada por ','
        var = 'O Brasil é penta'
        lista = var.split('')
        string2 = ','.join(lista)
    enumerate() = enumerar elementos da lista, função de lista, para objetos iteráveis
        var = 'O Brasil é penta'
        lista = var.split('') # ['O', 'Brasil', 'é', 'penta']
        for índice, valor in enumerate(lista):
            print(índice, valor, lista[índice])
    replace('e', '3') = sempre que achar o primeiro parâmetro, muda pelo segundo
    *args = Quando não se sabe quantos argumentos/parâmetros passar na função.
        Caso eu queira acessar um valor de args, passar o índice ( [] )
        def func(*args)
        func(1, 2, 3)
    **kwags = São argumentos com palavras chaves.
        def func(**kwargs)
        func(nome='Renan', sobrenome='Silva')
        # idade = kwargs.get('idade')
        # print(idade)
    global = a palavra global antes de uma variável, define que a variável,
        mesmo que declarada localmente, ela se torna global
    expresões lambda = funções anônimas, sem nome. sao bastante utilizadas para ordenações
        a = lambda x, y: x * y
        print(a(2,2))
        sorted(lista, key=lambda i: i[0]) -> está ordenando pelo índice 0 de uma lista
    
        



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

    For = Para
        texto = 'banana'
        for letra in texto:
            # a variável local (letra) passa a receber todos os índices da variável texto,
            # assim lê-se = para cada letra em texto, imprima a letra
            print(letra)

        for n in range(10):
            # laço simples em que conta de 0 a 9, acrescentando na variável local
            print(n)

        variável = ['Luiz', 'Renan', 'Bruno']
        for valor in variável:
            # for com else
            if valor.lower().startswith('r'): # essa função olha se o elemento começa com o parâmetro
                break
        else:
            print('Não começa com R', valor)



10. List:
        Utiliza-se colchetes = [], pode receber qualquer tipo de dado
        Listas também possuem índices, assim como as strings
        É possível utilizar o fatiamento = [start=0:end=10:step=1]
        Listas podem estar dentro de outras listas
            Ex: list =[
                    [1,2],
                    [3,4],
                    [5,6]
                ]
                for v in lista:
                    print(v[0]) # pega todos os índices 0

        Algumas funções para listas:
            extend = estende o valor de uma segunda lista ou variável na primeira
                l1.extend(l2) = l1 passa a ter o valor de l2 também
            append = insere um novo valor no final da lista
                l1.apprend('novo valor')
            insert = insere um novo valor em um índice pré-definido
                l1.insert(1, 'x') = insere o valor 'x' no índice 1
            pop = remove o último índice da lista
                l1.pop() = em uma lista de [1, 2, 3], ela passa a ter apenas [1, 2]
            del = remove índices, é possível utilizar fatiamento
                del(l1[3:5]) = está apagando os índices 3 e 4
            max = pega o maior valor da lista
                max(l1)
            min = pega o menor valor da lista
                min(l1)
            list = possível criar uma lista a partir de qualquer iterável,
                    junto com a função range é possível criar uma lista sem muito esforço
                l1 = list(range(1, 5)) # [1, 2, 3, 4]

        Ex:
            l2 = ['String', True, 10, -20.5]
            #para cada elemento (elem) em/na lista (l2)
            for elem in l2:
            # imprima
            print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

        Ex2:
            Em caso de lista dentro de outra lista:
            lista = [
                ['Renan', 'João', 'Maria'],
                ['Joana', 'Alice', 'Fernando']
            ]
            print(lista[1][0]) -> primeiro pai depois filho

11. Desempacotamento
        lista = ['Luiz', 'João', 'Maria']
        # n1, n2, n3 = lista -> cada valor/índice da lista irá para uma variável de acordo com sua posição
        # n1, n2, *n4 = lista -> percebe-se que em casos de não ter variáveis para cada índice,
        #                           é possível criar uma variável coringa, esta variável é uma lista (utilizando * na frente)
        # n1, n2, *n4, n5 = lista -> uma variável depois da lista sempre pega o último índice (-1 no caso)
        # *n4, n5, n6, n7 = lista -> n5, n6, n7 pega os últimos valores da lista, pois está depois da variável com * na frente

12. Invertendo valores
        x = 10
        y = 'Luiz'
        x, y = y, x -> x recebe y e y recebe x (1º com 1º e 2º com 2º)

13. Operação ternária
        logged_user = False
        msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
            a variável msg já possui uma operação ternária, isso simplifica muito
        print(msg)

14. Funções
        def funcion():
            print('Olá mundo!'):

        funções servem para que eu possa fazer com que o programa realize qualquer atividade
        funções só são executadas com ()

        elas podem receber variáveis, como abaixo:
        def funcion(msg):
            print(msg)

        funcion('Aqui vai a minha mensagem')
        return

        variáveis podem receber função, porém para serem chamadas, precisam do return no fim da função
        ex: var1 = funcion()

            

"""
