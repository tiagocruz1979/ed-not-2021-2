# algoritmo de ordenação Bubble Sort

# Percorre a lista a ser ordenada em sucessivas passadas
# trocando elementos adjacentes entre si quando o segundo 
# for menor que o primeiro. Efetua tantas passadas quanto necessárias
# até que nenhuma troca seja efetuada, sendo esta a ultima passada.

from time import time

def bubble_sort(lista):
    """
        Função que implementa o algoritmo de ordenação
        bubble sort
    """
    while(True):    #Loop eterno
        trocou = False
        # Loop na lista até o penúltimo elemento: len(lista) - 2
        for i in range(len(lista)-2): # inicia nova passada
            if lista[i + 1] < lista[i]: # é ncessário trocar
                lista[i+1],lista[i]=lista[i],lista[i+1] # faz a troca dos valores
                trocou = True
        # se não houve troca , a lista está ordenada e podemos interromper 
        # o loop while
        if not trocou:  # trocou == False
            break # interrompe o while



lista =[5,3,6,4,8,2,4,1]

print(lista)

t_ini = time()
bubble_sort(lista)
t_fim = time()

print("\n")

print(lista)


