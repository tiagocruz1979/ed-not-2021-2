# Algoritmo de Ordenação Selection Sort
#
# Isola (seleciona) o primeiro elemento da lista e em seguida
# encontra o menor valor no restante da lista.
# Se o valor encontrado for menor qe o valor selecionado , efetua a troca.
#Em seguida, isola o segundo número da lista, vuscando pelo menor
# valor das posições subsequentes. Faz a troca entre os dois valores, 
# se necessário. Continua o processo , até isolar o penúltimo elemento da lista.

from time import time
from data.nomes_desord import nomes
import tracemalloc

comps = 0 # número de comparações
passadas = 0 # número de passadas
trocas = 0 # número de trocas

def selection_sort(lista):
    """
        Função que complemnenta o algortimo de ordenação selection sort
    """
    global comps, passadas , trocas

    #percurso da lista até a penúltima posição

    for pos_sel in range(len(lista)-1):
        passadas+=1
        pos_menor = pos_sel+1
        #rotina para encontrar o menor número no resto da lista
       # percurso da lista da posição[i + 2]
        for j in range(pos_sel+2,len(lista)):
           # se o elemento da posição atual (j) for menor que o elemento da posição do menor (pos_menor), atualizamos pos_menor
           comps+=1
           if lista[j] < lista[pos_menor]:
               pos_menor = j
    
        # comparamos lista[sel] com lista[pos_menor] e , se o segundo for menor que o primeiro , trocamos.
        comps +=1 
        if lista[pos_menor] < lista[pos_sel]:
           trocas+=1
           lista[pos_menor],lista[pos_sel] = lista[pos_sel],lista[pos_menor]

################################################################

#nums=[88,44,33,0,99,55,77,22,11,66]
#nums=[99,88,77,66,55,44,33,22,11,0]
#nums=[0,11,22,33,44,55,66,77,88,99]
nums=[99,0,11,22,33,44,55,66,77,88]
print (nums)

lista_parc = nomes[:30000]

t_ini = time()
tracemalloc.start()

selection_sort(nomes)

mem_atual,mem_pico = tracemalloc.get_traced_memory()

t_fim = time()

print(nums)
print("\n")
print(f"Tempo de processamento: {(t_fim-t_ini)} s")
print(f"Número de Trocas: {trocas}")
print(f"Número de Comparações: {comps}")
print(f"Número de passadas: {passadas}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")    
tracemalloc.stop() # finaliza medição do consumo de memória