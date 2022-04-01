"""
Funções recursivas com Python (ou qualquer linguagem de programação)
são funções que chamam a si mesmas de maneira direta ou indireta.

"""


def fatorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    fat5 = fatorial(5)
    print(fat5)

# resultado seria 120
# 5 * 4 * 3 * 2 * 1 = 120
