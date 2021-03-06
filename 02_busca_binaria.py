# Algoritmo de Busca Binária

# Dada um lista, que deve estar previamente ordenada , e um valor de busca
# divide a lista em 2 metadas e procura pelo valor de busca 
# apenas na metade onde o valor poderia estar . Novas subdivisões são # # # feitas até que se encontre o valor de busca ou até que 
# existe uma sublista vazia, quando se conclui que o valor de busca não # # existe na lista

from time import time
from data.lista_nomes import nomes
comparacoes =0
def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritmo de busca binaria

        Retorna a posição onde valor_busca foi encontrado ou 
        o valor convencional -1 se o valor_busca não existir na lista
    """
    global comparacoes # indica que estamos usando a varia global
    comparacoes = 0
    ini = 0                 # Primeira posição
    fim = len(lista) -1     # última posição
    # comparacoes = 0
    while ini <=  fim:
        meio = (ini+fim) // 2   # Operador // divide e descarta a parte decimal , se houver. 
        # 1º caso: lista(meio) é igual a valor busca
        if lista[meio]== valor_busca: # caso verdadeiro , encontrou o valor
            comparacoes +=1
            return meio     # meio é a posição onde o valor_busca está na lista
        # 2º caso: valor_busca é menor que a lista(meio)
        elif valor_busca < lista[meio]:
            comparacoes+=2
            fim = meio -1
        # 3º caso: valor de busca é maior que lista[meio]
        else:
            comparacoes+=2
            ini = meio +1   # descarta a 1º metade da lista
    
    # 4º caso: valor_busca não encontrado na lista
    return -1
comparacoes = 0
busca = "TIAGO"

hora_ini = time()
posicao = busca_binaria(nomes,busca)
hora_fim = time()
print(f"\nPosição do nome {busca} na posição: {posicao}")
print(f"Tempo Gasto procurando {busca}: {(hora_fim-hora_ini)*1000000} nanosegundos")
print(f"Número de operações necessárias: {comparacoes}\n")
