

def primos_recursivo(n):
    pass


def primos_linear(n):
    primos = [2]
    if n == 2:
        return primos
    else:
        for i in range(3, n + 1):
            divisores = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    divisores += 1

            # Divisivel por 1 e por ele mesmo
            if divisores == 2:
                primos.append(i)
        return primos

while True:
    n = input("Insira o valor de N: ")
    try:
        n = int(n)
        if n > 1:
            break
    except ValueError:
        pass
    print("O valor de N deve ser um número inteiro maior que um!")

print('Primos recursivo = ', primos_recursivo(n))
print('Primos linear = ', primos_linear(n))