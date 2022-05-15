# https://docs.python.org/3/library/functions.html#open
# percorrendo arquivos e pastas

import os

caminho_pesquisa = input('Digite um caminho: ')
termo_pesquisa = input('Digite um termo: ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_pesquisa):
    for arquivo in arquivos:
        if termo_pesquisa in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                # print(nome_arquivo, ext_arquivo, sep='//')
                tamanho_arquivo = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho formatado:', formata_tamanho(tamanho_arquivo))
            except PermissionError as error:
                print('Sem permissão')
            except FileNotFoundError as error:
                print('Arquivo não encontrado')
            except Exception as error:
                print('ERRO desconhecido:', error)

print()
print(f'{conta} arquivo(s) encontrado')