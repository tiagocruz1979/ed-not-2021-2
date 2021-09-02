# QUICK SORT
# Escolhe um dos elemntos do vetor para ser o pivô ( na nossa implementação o ultimo elemento) e , na primrira passaa divide o vetor , a partir da posição final do vetor , em um subvetor à esquerda contendo apenas os elementos menores que o pivô e à direita contendo apenas os elementos maiores que o pivô.

#Em seguida , recursivamente , repete o processo em cada um dos subvetores até que todo o vetor esteja ordenado

def quick_sort(lista, ini=0, fim=None):
    """
        Função que implementa o algoritmo de ordenação quick sort de forma recursiva
    """
