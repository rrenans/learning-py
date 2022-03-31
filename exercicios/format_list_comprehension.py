
"""
O objetivo desse arquivo é entender na prática como funciona as
list comprehension, temos uma grande string e o intuito é cortar 
em pequeno blocos e separá-los com um '.'


"""
string = '01234567890123456789012345678901234567890123456789'

cont_indice = 10

lista = [ string[i:i+cont_indice] for i in range(0, len(string), cont_indice)]

result = '.'.join(lista)

print(result)
