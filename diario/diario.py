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
    contadores infinitos = count()
        é necessário importar -> from itertools import count
        contador = count()
        este contador pode receber como parâmetro start, step e end
        Exemplo:
            for valor in contador:
                print(round(valor, 2))
                if valor >= 10:
                    break
    combinations, permutations e product - itertools
        combinação - ordem não importa
        permutação - ordem importa
        ambos não repetem valores únicos
        produto - ordem importa e recebe valores únicos
        Exemplo:
            pessoas = ['Luiz', 'André', 'Eduardo']
            for grupo in combinations(pessoas, 3):
                print(grupo)
    groupby - agrupando valores
        Exemplo:
            from itertools import groupby, tee

            alunos = [
                {'nome': 'Luiz', 'nota': 'A'},
                {'nome': 'Letícia', 'nota': 'B'},
                {'nome': 'Fabrício', 'nota': 'A'},
                {'nome': 'Rosemary', 'nota': 'C'},
                {'nome': 'Joana', 'nota': 'D'},
                {'nome': 'João', 'nota': 'A'},
                {'nome': 'Eduardo', 'nota': 'B'},
                {'nome': 'André', 'nota': 'C'},
                {'nome': 'Anderson', 'nota': 'B'},
            ]


            def ordena(item):
            return item['nota']


            alunos.sort(key=ordena)
            alunos_agrupados = groupby(alunos, ordena)

            '''
            # Sem tee (com list)
            for agrupamento, valores_agrupados in alunos_agrupados:
            valores = list(valores_agrupados)
            print(f'Agrupamento: {agrupamento}')
            for aluno in valores:
                print(f'\t{aluno}')
            quantidade = len(valores)
            print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
            '''

            # Com tee
            for agrupamento, valores_agrupados in alunos_agrupados:
            v1, v2 = tee(valores_agrupados)

            print(f'Agrupamento: {agrupamento}')

            for aluno in v1:
                print(f'\t{aluno}')

            quantidade = len(list(v2))
            print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
            
    Map
        



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
        #                           é possível criar uma variável coringa, esta variável é uma lista
                                        (utilizando * na frente)
        # n1, n2, *n4, n5 = lista -> uma variável depois da lista sempre pega o último índice (-1 no caso)
        # *n4, n5, n6, n7 = lista -> n5, n6, n7 pega os últimos valores da lista,
                                        pois está depois da variável com * na frente

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

15. Tuplas
    utiliza-se o ()
    diferença de uma tupla para uma lista é que a tupla não pode ser alterada,
    não pode adicionar, remover ou mudar o valor do elemento dentro de uma tupla
    muito parecido com as listas

16. Dicionário
    Estrutura de dados que contém chave e valor
    Utiliza-se {} como símbolo

    sintaxe abaixo:
    d1 = {'chave': 'valor'}

    Podemos criar também com a função dict, sintaxe abaixo:
    d1 = dict(chave1='valor da chave1', chave2='valor da chave2')

    Dicionários podem receber qualquer tipo de dados dentro deles
    d1 = {
        'str': 'valor1',
        123: 'valor2'
        (1,2,3,4): 'valor3',
        'cliente': {
            'nome' : 'Renan',
            'contrato' : 1932
        }
    }

    Podemos utilizar a função update para atualizar e criar valores dentro de um dicionário
    Mas a melhor forma é utilizando os colchetes []

    Um trecho de código muito importante para fazer a iteração de um dicionário dentro de
    outro dicionário, sintaxe abaixo:

    clientes = {
        'cliente1': {
            'nome': 'Renan',
            'sobrenome': 'Silva',
        }, 
        'cliente2': {
            'nome': 'João',
            'sobrenome': 'Santos',
        }, 
        'cliente3': {
            'nome': 'Luiz',
            'sobrenome': 'Pereira',
        }
    }

    for clientes_key, clientes_value in clientes.items(): # A função items acessa tudo, no caso, chave e valor
        print(f'Exibindo {clientes_key}')
        for dados_key, dados_value in clientes_value.items():
            print(f'\t{dados_key} = {dados_value}')

17. Conjuntos (sets)
    É como se estivesse criando uma lista, porém apenas com as chaves ao invés de colchetes
    Para não confundir com a criação de um dicionário, Sets recebem apenas valores
    Eles não respeitam ordens
    Geralmente são utilizados para eliminar elementos duplicados de uma lista

    s1 = {1, 2, 3, 4}
    s1 = set() # cria um set vazil
    s1.add(1) # adiciona 1 ao set
    s1.update('Renan') # muito parecida com o add, porém recebe um iterável e itera sobre o valor
                    no caso, está recebendo uma string 'Renan', mas quando der um print pode ser
                    ser retornado = {'a', 'n', 'e', 'n', 'R'}
    s1.discard(1) # remove o 1 do set

    Funções para set:
        union -> | :
            s1 = {1, 2, 3}
            s2 = {3, 4, 5}
            s3 = s1 | s3 # Une os dois sets

        intersection -> & :
            s1 = {1, 2, 3}
            s2 = {3, 4, 5}
            s3 = s1 & s3 # Mostra todos os elementos presentes nos dois sets

        difference -> - :
            s1 = {1, 2, 3, 7}
            s2 = {3, 4, 5}
            s3 = s1 - s3 # Elementos apenas no set da esquerda

        symmetric_difference -> ^ :
            s1 = {1, 2, 3}
            s2 = {3, 4, 5}
            s3 = s1 ^ s3 # Elementos que estão nos dois sets, mas não em ambos

18. List Comprehension
    É possível iterar sobre uma lista com uma única linha de código
    l1 = [1, 2, 3]
    ex1 = [var for var in l1] # não estamos fazendo nada aqui, a não ser a própria iteração
    ex2 = [var * 2 for var in l1] # foi feita a iteração com uma multiplicação de cada índice
    ex3 = [(var, var2) for var in l1 for var2 in range(3)] # estou criando duas tuplas, temos dois for
        o primeiro for está iterando na lista
        o segundo for está iterando no valor, ou seja, um pega o índice e outro o valor
    l2 = ['Renan', 'Silva']
    ex4 = [v.replace('a', '@').upper() for v in l2] # para cada valor dentro da l2, mudar o a por @ e deixar tudo maiúsculo
    ex5 = [(y, x) for x, y in tupla]
    l3 = list(range(100))
    ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0] # com if
    ex7 = [v if v % 3 == 0 else 'Não é' for v in l3] # com if e else (todo número divisível por três retorna 'Não é')
    ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for in l3]

19. Dictionary Comprehension
    Assim como funciona com listas, funciona também com dicionários

    lista = [
        ('chave', 'valor')
    ]

    d1 = {x: y.upper() for x, y in lista}

20. Geradores, Iteradores e Iteráveis:
    Iterável -> é um objeto que pode-se iterar sobre ele, mas não necessariamente é um iterador
    Iterador -> ele vai te dar um valor de cada vez sempre que você precisar desse valor

    yield -> define um gerador, gerador retorna um valor de cada vez, sem esperar por todo o resultado
        chamamos esse acontecimento de lazy evaluation(avaliação preguiçosa)

    para ver na prática, podemos testar o código a seguir:
        def gera():
            for n in range(100):
                yield n
                time.sleep(0.1)

        g = gera()
        for v in g:
            print(v)

21. Unindo iteráveis
    Zip - Unindo iteráveis
        une até a menor lista
    Zip_longest - Itertools
        une todos os valores e, preenche com none caso uma chave não tenha seu valor
        o zip_longest tem que importar -> from itertools import zip_longest

    cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
    estados = ['SP', 'MG', 'BA']

    cidades_estados = zip(cidades, estados)
    for valor in cidades_estados:
        print(valor)

22.Exceções
    try:
        a
    except NameError as erro:
        print(erro)
    execpt Exception as erro:
        print(erro)

        É possível utilizar else depois da exception, para caso o código funcione sem ter erro executar
        é possível também utilizar a palavrinha finally, que será executado sempre que a exception chegar ao final
        podemos ter também try dentro de try

        lançando nossa própria exception:
            https://docs.python.org/3/library/exceptions.html

            def divide(n1, n2):
                if n2 == 0:
                    raise ValueError("n2 não pode ser 0.") # lança e relança a excption
                return n1 / n2
            
            try:
                print(divide(n1=2, n2=0))
            exception ValueError as error:
            print(error)

        Podemos usar try e except como condicionais
            def converte_numero(valor):
                try:
                    valor = int(valor)
                    return valor
                except ValueError:
                    try:
                        valor = float(valor)
                        return valor
                    except ValueError:
                        pass

            numero = converte_numero(input('Digite um número: '))
            if numero is not None:
                print(numero * 5)
            else:
                print('isso não é um número')

23. Módulos
    módulos são arquivos .py (que contém código python) e servem para expandir
    as funcionalidades padrão da linguagem
    https://docs.python.org/3/py-modindex.html

    from calculos import multiplica
    import calculos

24. Criando, lendo, escrevendo e apagando arquivos
    https://docs.python.org/pt-br/3/library/functions.html#open

    # file = open('abc.txt', 'w+')
    # file.write('Linha1\n')
    # file.write('Linha2\n')
    # file.write('Linha3\n')

    # file.seek(0, 0)
    # print('Lendo linhas:')
    # print(file.read())
    # print('#############')

    # file.seek(0, 0)
    # for linha in file.readlines():
    #     print(linha, end='')
    
    # file..close()
    # ---------------
    # try:
    #     file = open('abc.txt', 'w+')
    #     file.write('Linha')
    #     file.seek(0)
    #     print(file.read())
    # finally:
    #     file.close()
    # ---------------
    # with open('abc.txt', 'w+') as file:
    #     file.write('Outra linha\n')
    #     file.seek(0)
    #     print(file.read())

25. Funções decoradoras e decoradores
    cd ../exercicios/decor.py
26. Parâmetros mutáveis
    cd ../exercicios/param_mutaveis.py


                PROGRAMAÇÃO ORIENTADA A OBJETOS


27. Classes
    Uma classe é uma forma de definir um tipo de dado em uma linguagem orientada a objeto.
    Ela é formada por dados e comportamentos. Para definir os dados são utilizados os atributos,
    e para definir o comportamento são utilizados métodos.

    Quando uma função está dentro de uma classe, ela é um método.

    O self serve para usar um método de determinada classe
    utiliza-se a instancia da classe
    p2.falar(p2)

28. Encapsulamento
    Encapsulamento é o processo de esconder todos os detalhes de um objeto que não contribuem
    para as suas características essenciais. Na programação orientada a objetos, o encapsulamento
    se refere ao agrupamento de dados com os métodos que operam nesses dados ou à restrição
    do acesso direto a alguns dos componentes de um objeto.

    public -> métodos e atributos que podem ser acessados dentro e fora da classe
    protected -> métodos e atributos que podem ser acessados apenas dentro da classe ou das filhas daquela classe
    private -> métodos e atributos que só estão disponíveis dentro da classe

    no python utilizamos convenções ao invés destas palavras
    _dados -> privado fraco = protected/ é um atributo público, que podemos acessar
    __dados -> privado forte = private/ é um atributo que pode ser acessado a partir do (_NOMECLASSE__nomeatributo)



"""
