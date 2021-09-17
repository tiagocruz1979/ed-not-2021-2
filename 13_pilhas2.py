from lib.stack import Stack

#Criando uma pilha
pilha = Stack()
print(pilha.to_str())

#Empilhando valores
pilha.push(10)
pilha.push(13)
pilha.push(19)
pilha.push(23)
pilha.push(27)
pilha.push(33)
print(pilha.to_str())

# Retirar um elemento da pilha
removido = pilha.pop()
print(f"Removido: {removido}, pilha: {pilha.to_str()}")

# Consultar o último elemento
print(f"Último elemento da pilha: {pilha.peek()}")


# Esvaziar a pilha, elemento por elemento
while not pilha.is_empty():
    print(pilha.pop())

#Conferindo a pilha atual
print(f"Exibição da pilha atual: {pilha.to_str()}")

# Retirar elemento de uma pilha Vazia
removido = pilha.pop()
print(removido)

# Consultar ultimo elemento de uma pilha vazia
removido = pilha.peek()
print(removido)