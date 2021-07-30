primos =[2,3,5,7,11,13,17,19,23,29]

# Percurso
for num in primos:
    print(num)

# Acrescentar novo elemento ao fim da lista
primos.append(31)
print(primos)

# inserindo um novo eleemento em uma posição específica
# primeiro informa a posição e depois o valor 
primos.insert(0,1)
print(primos)

# insere o valor 37 na posição 5
primos.insert(5,37)
print(primos)

# retirando o último elemento da lista: pop()
ultimo = primos.pop()
print(f"Último: {ultimo}")
print(primos)

#removendo por valor: remove()
primos.remove(37)
print(primos)

#removendo por posição: del
#removendo o elemento da posição 4
del primos[4]
print(primos)

#fatiando uma lista
#exibindo apenas o elemento da posição 0(inclusive) à posicao 7 (exclusive)
print(primos[0:7])

#da posição de à posição 8
print(primos[2:8])

#fatiando e criando uma sublista
sub_primos = primos[1:5]
print (sub_primos)




