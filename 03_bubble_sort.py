# algoritmo de ordenação Bubble Sort

# Percorre a lista a ser ordenada em sucessivas passadas
# trocando elementos adjacentes entre si quando o segundo 
# for menor que o primeiro. Efetua tantas passadas quanto necessárias
# até que nenhuma troca seja efetuada, sendo esta a ultima passada.

from time import time
from data.nomes_desord import nomes
comps = 0 # número de comparações
passadas = 0 # número de passadas
trocas = 0 # número de trocas

def bubble_sort(lista):
    """
        Função que implementa o algoritmo de ordenação
        bubble sort
    """
    global comps,passadas,trocas
    comps = 0
    passadas = 0
    trocas = 0
    while(True):    #Loop eterno
        trocou = False
        passadas+=1
        # Loop na lista até o penúltimo elemento: len(lista) - 2
        # Ex. em uma lista de 10 elementos, len(lista) ==10
        # a última posição estará em len(lista) -2 , ou seja , 8 -> range(len(lista)-1)
        for i in range(len(lista)-1): # inicia nova passada
            comps+=1
            if lista[i + 1] < lista[i]: # é ncessário trocar
                lista[i+1],lista[i]=lista[i],lista[i+1] # faz a troca dos valores
                trocas+=1
                trocou = True
        # se não houve troca , a lista está ordenada e podemos interromper 
        # o loop while
        if not trocou:  # trocou == False
            break # interrompe o while



t_ini = time()
bubble_sort(nomes)
t_fim = time()

print("\n")
print(f"Tempo de processamento: {(t_fim-t_ini)} s")
print(f"Número de Trocas: {trocas}")
print(f"Número de Comparações: {comps}")
print(f"Número de passadas: {passadas}")





