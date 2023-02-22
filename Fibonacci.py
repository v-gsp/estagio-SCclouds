# -*- coding: utf-8 -*-

# duas solucoes possiveis para fibonacci
# a solucao linear é obviamente muito mais eficiente

# Fibonacci Recursiva
def fib_r(N):
    if N < 0:           # se negativo, retorna falso
        return False
    elif N <= 1:        # se 0 ou 1, solucao trivial
        return N
    else:               # se > 1: recursao, faz fib das anteriores
        return fib_r(N - 1) + fib_r(N - 2)


# Fibonacci Linear
def fib_l(N):
    if N < 0:           # se negativo, retorna falso
        return False
    elif N <= 1:        # se 0 ou 1, solucao trivial
        return N
    else:               # se > 1: busca linearmente
        a, b = 0,1      # valores iniciais
        for i in range(2,N+1):
            fib = a + b     # somando anteriores
            a, b = b, fib
        return fib


