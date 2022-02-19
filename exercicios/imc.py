def calcular_imc(peso, altura):
    int(peso)
    float(altura)

    imc = peso / (altura ** 2)
    return imc

if __name__ == '__main__':
    print(f'O seu IMC é: {calcular_imc(80, 1.80)}')
