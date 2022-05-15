# se executado a partir do arquivo main, executar função

def soma(x: float, y: float) -> float:
    return x + y

def main() -> None:
    print(soma(10, 20))
    print(soma(20, 20))

if __name__ == '__main__':
    main()