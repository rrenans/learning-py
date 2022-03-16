"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.

2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo é um percentual
    (ex: 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.

4 - Fizz Buzz. Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da
    função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.

5 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.

6 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
    Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""

print('1ª Questão: ')
def saudacao(msg, nome):
    print(f'{msg} {nome}')

saudacao('Olá', 'Renan')

print('\n')

print('2ª Questão: ')
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(3, 2, 1)

print('\n')

print('3ª Questão: ')
def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(50, 10)

print('\n')

print('4ª Questão: ')
def fizzbuzz(n):
    if n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    elif n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    else:
        return n

print(fizzbuzz(15))

print('\n')

print('5ª Questão: ')
def ola_mundo1():
    return 'Olá mundo!'

def ola_mundo2(fnc1):
    return fnc1()

executar_ola_mundo = ola_mundo2(ola_mundo1)
print(executar_ola_mundo)

print('\n')

print('6ª Questão: ')
def fala_oi1(fnc2, *args, **kwargs):
    return fnc2(*args, **kwargs)

def fala_oi2(nome):
    return f'Oi {nome}'

def fala_oi3(nome, saudacao):
    return f'{saudacao} {nome}'

executar_fala_oi1 = fala_oi1(fala_oi2, 'Renan', saudacao0='Bom dia!')
executar_fala_oi2 = fala_oi1(fala_oi3, 'Renan', saudacao0='Bom dia!')
