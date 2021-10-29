from lib.doubly_linked_list import DoublyLinkedList


lista = DoublyLinkedList()
print(lista.to_str())

# inserção na lista vaziz
lista.insert(0,'Fusca')
print(lista.to_str())

# inserção no início da lista
lista.insert(0,'Chevette')
print(lista.to_str())

# inserção no final da lista
lista.insert(3,'Maverick')
print(lista.to_str())

# inserção no final da lista
lista.insert(4,'Opala')
print(lista.to_str())

# inserção no final da lista
lista.insert(5,'Del Rey')
print(lista.to_str())


# inserção em posição intermediária
lista.insert(1,'Gol')
print(lista.to_str())

# inserção em posição intermediária
lista.insert(4,'Corcel')
print(lista.to_str())

#remoção do primeiro nodo
removido = lista.remove(0)
print(f"Removido da primeira posição: {removido}" )
print(lista.to_str())

#remoção do último nodo
removido = lista.remove(lista.count() -1)
print(f"Removido última posição: {removido}")
print(lista.to_str())

#remoção de posição intermediária
removido = lista.remove(2)
print(f"Remoção da posição 2: {removido}")
print(lista.to_str())

#Consultando o ultimo elemento da lista
consulta = lista.peek_tail()
print(f"Mostrar o último elemento: {consulta}")
print(lista.to_str())

# mostrar a posiçãogit add .
#  de um determinado valor

valor = "Opala"
print(f"Mostra a posição de {valor} , posicao {lista.index(valor)}")

valor = "Gol"
print(f"Mostra a posição de {valor} , posicao {lista.index(valor)}")

valor = "Fusca"
print(f"Mostra a posição de {valor} , posicao {lista.index(valor)}")

valor = "Corcel"
print(f"Mostra a posição de {valor} , posicao {lista.index(valor)}")

valor = "Maverick"
print(f"Mostra a posição de {valor} , posicao {lista.index(valor)}")