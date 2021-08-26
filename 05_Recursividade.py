# Fatorial de um número n 
# é igual ao número n multiplicado por todos os seus antecessores até 1
#
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 4! = 4 * 3 * 2 * 1 = 24
# 3! = 3 * 2 * 1 = 6
# 2! = 2 * 1 = 2
# 1! = 1
# 0! = 1

# 5! = 5 * 4!
# 4! = 4 8 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!

# n! = n * (n-1)! p/ n > 1

# implementação iterativa
def fatorial(n):
    resultado = 1
    if (n>1):
        for i in range(n,1,-1): # range começa no número n e vai descrementenado até 1
            resultado *= i 
            print(f'Resultado: {resultado}, i: {i}') #debug
    return resultado

numero = 10
print(f'{numero}! = {fatorial(numero)}')

print ('--------------------------------------')

# n! = n * (n-1)! p/ n >1
#Recursividade ocorre quando a deginição de uma unção incluir a propria função sendo definida
#Em programação, a recursividade se traduz quando uma função efetua 
# chamadas a si propria

#implementação recursiva
def fatorialRecursivo(n):
    # Em uam função recusiva , a condição de sáida é aquela em que 
    # a funcão é capaz de retornar um resultado sem chamar novamente a si mesma
    print(n)
    if n <= 1:
        return 1
    return n * fatorialRecursivo(n-1)

numero = 20
print(f'{numero}! = {fatorialRecursivo(numero)}')

import sys
print(sys.maxsize)