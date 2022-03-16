"""
Exercício para treinar lógica, utilizando iterações entre dicionários, dicionários
laços de repetição entre outros
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '6',
            'b': '5',
            'c': '12',
        },
        'resposta_certa': 'a',
    },
}

print()

respostas_certas = 0
for pergunta_chave, pergunta_valor in perguntas.items():
    print(f'{pergunta_chave}: {pergunta_valor["pergunta"]}')

    print('Respostas: ')
    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items():
        print(f'[{resposta_chave}] : {resposta_valor}')


    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pergunta_valor['resposta_certa']:
        print('EHHH!! Você acertou!!')
        respostas_certas += 1
    else:
        print('AAHH, Você errou !!')
    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou: {respostas_certas}')
print(f'Sua porcentagem de acerto foi: {porcentagem_acerto}%')
