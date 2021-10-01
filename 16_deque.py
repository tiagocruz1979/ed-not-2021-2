from lib.deque import Deque

#######################################################

deque = Deque()     # Cria um deque vazio
print (deque.to_str())

# Inserções "normais"
deque.insert_back("Tertuliano")
deque.insert_back("Castorina")
deque.insert_back("Astolfo")
deque.insert_back("Wesclerson")
deque.insert_back("Gilvanete")
    
print(deque.to_str())

#inserções prioritárias
deque.insert_front("Hermógenes")
deque.insert_front("Querência")

print(deque.to_str())

# Remoções "normais"
atendido = deque.remove_front()
print(f"Atendido: {atendido}")
atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

# Desistência
desistencia = deque.remove_back()
print(f"Desistiu: {desistencia}")
desistencia = deque.remove_back()
print(f"Desistiu: {desistencia}")

print(deque.to_str())

# consultando  as extremidades do deque
primeiro = deque.peek_front()
ultima = deque.peek_back()
print(f"Prineiro: {primeiro}, útimo: {ultima}")
print(deque.to_str())






