# -*- coding: utf-8 -*-

# duas solucoes possiveis para achar os primos
# a solucao linear é obviamente muito mais eficiente

# Primos Recursiva
def primos_r(N):
    if N <= 1:          # se 0 ou 1, retorna lista vazia
        return []
    if N == 2:          # se 2, solução trivial
        return [2]
    if N == 3:          # se 3, solução trivial
        return [2, 3]
    else:               # senão, função recursiva
        primos_lista = primos_r(N-1)    # lista os primos do valor anterior
        for i in range(2, N):           # testa todos os divisores possiveis
            if N % i == 0:              # ve se é divisivel
                return primos_lista     # retorna, recursão
        primos_lista.append(N)          # se for primo. adiciona à lista
        return primos_lista             # retorna a lista dos primos

# Primos Linear
def primos_l(N):
    if N <= 1:          # se 0 ou 1, retorna lista vazia
        return []
    if N == 2:          # se 2, solução trivial
        return [2]
    if N == 3:          # se 3, solução trivial
        return [2, 3]
    else:               # se maior, busca os primos
        primos_lista = [2, 3]   # 2 e 3 sempre na lista
        for i in range(4, N + 1):   # analisar todos os valores até N
            for j in range(2, i):   # testa todos os divisores possiveis
                if i % j == 0:      # se divisivel, break
                    break
            else:
                primos_lista.append(i)  # se não, adiciona a lista
    return primos_lista                 # no fim, retorna a lista

