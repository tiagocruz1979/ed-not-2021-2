# Algoritmo de Ordenaão Merge Sort
#
# No processo de ordenação, esse algotimo "desmonta" o vetor original
# contentno n elementos até obter N vetores de apenas um elemento cada um 
# Em seguida, usando a técnica de mesclagem (merge) , "remonta" o vetor, dessa vez com os elementos já em ordem 
from time import time
from data.nomes_desord import nomes
import tracemalloc
comps = 0
divisoes = 0
juncoes = 0

def merge_sort(lista):
    """
    Função que implementa o algoritmo merge sort usando o método Recursivo
    """

    # não podemos zerar as variaveis globais de estatistica dentro da função porque ela é recursiva e resetaria a contagem a cada chamada
    global comps, divisoes, juncoes

    # print(f'Lista Recebida: {lista}')
    # Só continua se a lista tiver mais de um elemento
    if len(lista) <= 1:
        return lista
        
    meio = len(lista) // 2 ## operador // divide o número e resorna somente a parte inteira

    # Gera cópia da primeira metade da lista
    lista_esq = lista[:meio] # lista do inicio ao meio -1
    # gera cópia da segunda metade da lista
    lista_dir = lista[meio:] # do meio ao fim

    divisoes += 1

    # chamada recursiva da função para continuar repartindo a lista ao meio
    # print('direita:')
    lista_esq = merge_sort(lista_esq)
    # print('esquerda')
    lista_dir = merge_sort(lista_dir)


    # juntar duas metades em uma única lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = [] # lista vazia

    #Compara os elementos de cada lista entre si e insere na lista ordenada o que for menor
    while(pos_esq < len(lista_esq) and pos_dir <len(lista_dir)):
        # o elemento que se encontra na lista da esquerda
        # é menor que o que se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq+=1
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1
        comps+=1
    
    sobra = None    # A sobra da lista que ficou para trás

    if(pos_esq < pos_dir): # houve sobra à esquerda
        sobra = lista_esq[pos_esq:] # sobra do pos_esq até o final
    else: # houve sobra à direita
        sobra = lista_dir[pos_dir:] # sobra do pos_dir até o final

    # print(f'>>>> final ordenada: {ordenada +sobra}')

    juncoes += 1

    #Retornamos a lista final ordenada , composta da ordenada + sobra
    return ordenada + sobra # "Soma" de duas listas


comps = 0
divisoes = 0
juncoes = 0
print('----------------------------------------')
nums=[7,5,3,1,0,2,4,6,8]
print (nums)
print(merge_sort(nums))


comps = 0
divisoes = 0
juncoes = 0
print('----------------------------------------')
t_ini = time()
tracemalloc.start() # Inicia a medição de consumo de memória
lista_ordenada = merge_sort(nomes)
t_fim = time()
mem_atual,mem_pico = tracemalloc.get_traced_memory()


print(lista_ordenada)
print("\n")
tracemalloc.stop() # finaliza a medição de consumo de memória
memoria = tracemalloc.get_traced_memory()

print(f"Tempo de processamento: {(t_fim-t_ini)} s")
print(f'Pico de memória: {mem_pico / 1024 / 1024 }MB')

print(f"Número de juncoes: {juncoes}")
print(f"Número de Comparações: {comps}")
print(f"Número de divisoes: {divisoes}")



    

