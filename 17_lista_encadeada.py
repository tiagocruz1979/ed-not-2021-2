
from lib.linked_list import LinkedList

lista = LinkedList()

lista.insert((0), "1 kg de batata")
lista.insert((1), "café")
lista.insert((2), "miojo")
lista.insert((3), "óleo")
lista.insert((4), "sabonete")
lista.insert((5), "shampoo")

lista.insert((4), "tomate")

lista.insert(7, "sabão em pó")

lista.insert(30,"detergente")

lista.insertFront("5 kg arroz")

lista.insertBack("Água Sanitária")

print(lista.to_str())

print(f"Info do nodo na posicao 7: {lista.peek(7)}")
print(f"Info do nodo na posicao 13: {lista.peek(13)}")
print(lista.peek(5))
print(lista.peek(0))

print(f"Item procurado na posição: {lista.index('5 kg arroz')}")
print(f"Item procurado na posição: {lista.index('shampoo')}")
print(f"Item procurado na posição: {lista.index('café')}")
print(f"Item procurado na posição: {lista.index('Água Sanitária')}")
print(f"Item procurado na posição: {lista.index('cebola')}")


print ('----------------------------------')
print(lista.to_str())

#rmeoção no início da lista
removido = lista.remove(0);
print(f"\nValor removido: {removido}\n");
print(lista.to_str())


print ('-------------Removendo item na posicao 5------------')
removido = lista.remove(5);
print(lista.to_str())

print ('----------Remvovendo item da ultima posicao------------')
removido = lista.remove(lista.count() -1);
print(f"Valor Removido: {removido}")
print(lista.to_str())

removido = lista.removeTail();
print(f"Valor Removido: {removido}")
print(lista.to_str())