"""
    Exercício de forca, como desafio consumir uma API para gerar palavras rândomicas automaticamente
"""

palavra_secreta = 'perfume'
letras_digitadas = []
chances = 3

while True:

    if chances == 1:
        print('Digite "S" para receber uma dica ou digite "N" para não receber uma dica')
        dica = input('Você deseja receber uma dica? ')
        if dica == 'S':
            print('A dica é: Aromatizador de corpos')
        elif dica == 'N':
            continue

    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print(f'Ahh isso não vale, digite apenas uma letra.')
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz, a letra "{letra}" não existe na palavra secreta.')
        letras_digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:
        print(f'Que legal, VOCÊ GANHOU! A palavra secreta era {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in palavra_secreta:
        chances -= 1

    print(f'Você tem {chances} chances.')
