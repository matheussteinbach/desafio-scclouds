

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
            p.append(n)
    primos_recursivo(n - 1)
    return sorted(p)

def primos_linear(n):
    p = [2] # Garante que o resultado recursivo nao interfira
    if n == 2:
        return p
    else:
        for i in range(3, n + 1):
            if primo(i):
                p.append(i)
        return p

while True:
    n = input("Insira o valor de N: ")
    try:
        n = int(n)
        if n > 1:
            break
    except ValueError:
        pass
    print("O valor de N deve ser um número inteiro maior que um!")

p = [2]
print('Primos recursivo = ', primos_recursivo(n))
print('Primos linear = ', primos_linear(n))