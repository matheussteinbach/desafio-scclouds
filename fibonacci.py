

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_linear(n):
    if n <= 1:
        return n
    else:
        penultimo = 0 # fibonacci(0)
        ultimo = 1  # fibonacci(1)

        i = 2
        while i <= n:
            atual = ultimo + penultimo 

            penultimo = ultimo
            ultimo = atual
            i += 1

        return atual
