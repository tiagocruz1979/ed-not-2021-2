from lib.queue import Queue

#############################################

fila = Queue()  # cria uma nova fila
print (fila.to_str())

# Adicionando pessoas à Fila
fila.enqueue("Marciovaldo")
fila.enqueue("Fildanete")
fila.enqueue("Terencionildo")
fila.enqueue("Junislerton")
fila.enqueue("Ritielaine")

print (fila.to_str())

# desenfileirando

proximo = fila.dequeue();
print(f"Atendido: {proximo}")
print (fila.to_str())
proximo = fila.dequeue();
print(f"Atendido: {proximo}")
print (fila.to_str())

fila.enqueue("Adenoirton")
print(fila.to_str())

proximo = fila.peek()
print(f"Próximo da fila: {proximo}")

while fila.is_empty() == False:
    print(fila.dequeue())
    print(fila.to_str())













