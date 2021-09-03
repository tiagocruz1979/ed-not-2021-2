# QUICK SORT
# Escolhe um dos elemntos do vetor para ser o pivô ( na nossa implementação o ultimo elemento) e , na primrira passaa divide o vetor , a partir da posição final do vetor , em um subvetor à esquerda contendo apenas os elementos menores que o pivô e à direita contendo apenas os elementos maiores que o pivô.

#Em seguida , recursivamente , repete o processo em cada um dos subvetores até que todo o vetor esteja ordenado
from time import time
from data.nomes_desord import nomes
import tracemalloc
import psutil
comps = 0 # número de comparações
passadas = 0 # número de passadas
trocas = 0 # número de trocas

def quick_sort(lista, ini=0, fim=None):
    """
        Função que implementa o algoritmo de ordenação quick sort de forma recursiva
    """
    #se fim for none então consideramos a última posicao do vetor
    if fim is None:
        fim = len(lista) - 1

    # para continuarmos , precisamos que a lista tenha pelo menos dois elementos para ordenar

    if fim <= ini:
        return      # sai da função sem fazer nada
    
    global passadas, comps, trocas
    passadas += 1

    pivot = fim #pivo é o último elemento
    div = ini - 1 # divisor inciia antes do primeiro elemento

    # percorre a lista até o penultimo elemento
    for i in range(ini,fim):
        comps += 1
        if lista[i] < lista[pivot]:
            div += 1    #incremento o divisor
            if div != i:
                trocas += 1
                lista[div],lista[i]=lista[i],lista[div] # lista[div] e lista[i] trocam de lugar entre si caso não sejam o mesmo elemento

    #depois que o percurso de i acaba, div ainda é incrementado mais uma vez 
    div += 1

    # colocamos o pivo em seu lugar definitivo. a toca acontece se o valor da posicao pivot for menor que o valor da posicao div
    comps += 1
    if lista[pivot] < lista[div] and pivot != div:
        lista[pivot],lista[div] = lista[div], lista[pivot]
        trocas += 1

    #chamamos recursivamente a função para a sublista à esquerda da posicao div
    quick_sort(lista,ini,div-1)
    #chamamos recursivamente a função para a sublista à direita da posição div
    quick_sort(lista,div+1,fim)
        

#testando com vetor de numeros
numeros=[11,00,55,44,33,22,88,77,44,66,99]

quick_sort(numeros)

print(numeros)

#testando com vetor de nomes
comps = 0
passadas = 0
trocas = 0

tracemalloc.start() # Inicia a medição de consumo de memória
print('----------------------------------------')
t_ini = time()
quick_sort(nomes)
t_fim = time()
mem_atual,mem_pico = tracemalloc.get_traced_memory()
print(nomes)
print("\n")
memoria = tracemalloc.get_traced_memory()

print(f"Tempo de processamento: {(t_fim-t_ini)} s")
print(f'Pico de memória: {mem_pico / 1024 / 1024 }MB')

print(f"Número de comps: {comps}")
print(f"Número de passadas: {passadas}")
print(f"Número de trocas: {trocas}")
tracemalloc.stop() # finaliza a medição de consumo de memória

print ('RAM memory % used:' , psutil.virtual_memory()[2])
print ('CPU usage is: ', psutil.cpu_percent(4))

