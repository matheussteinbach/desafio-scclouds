

def primo(n):
    divisores = 0
    for j in range(1, n + 1):
        if n % j == 0:
            divisores += 1

    # Divisivel por 1 e por ele mesmo
    return divisores == 2


def primos_recursivo(n):
    if n == 2:
        return 
    else:
        if primo(n):
            primos_rec.append(n)
    primos_recursivo(n - 1)
    return sorted(primos_rec)

def primos_linear(n):
    primos_lin = [2]
    if n == 2:
        return primos_lin
    else:
        for i in range(3, n + 1):
            if primo(i):
                primos_lin.append(i)
        return primos_lin

while True:
    n = input("Insira o valor de N: ")
    try:
        n = int(n)
        if n > 1:
            break
    except ValueError:
        pass
    print("O valor de N deve ser um número inteiro maior que um!")

primos_rec = [2]
print('Primos recursivo = ', primos_recursivo(n))
print('Primos linear = ', primos_linear(n))