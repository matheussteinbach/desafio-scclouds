

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

while True:
    n = input("Insira o valor de N: ")
    try:
        n = int(n)
        if n >= 0:
            break
    except ValueError:
        pass
    print("O valor de N deve ser um número inteiro maior ou igual a zero!")

print('Fibonacci recursivo = ', fibonacci_recursivo(n))
print('Fibonacci linear = ', fibonacci_linear(n))
# Verificações de n <= 1 poderiam ser feitas apenas uma vez previamente
# Foram feitas nas funções para funcionarem independentemente do main
