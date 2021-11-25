# Usando a estrutura dict nativa do Python
# Para representar o grafo não direcionado
# refletindo sua matriz de adjacencia

# Dentro de cada propriedade da dict usamos
# uma lista para representar as arestas entre
# os vértices
grafo.naodir = {
    'A' : ['A', 'B', 'C'],
    'B' : ['A', 'C'],
    'C' : ['A', 'B' ,'D'],
    'D' : ['D']
}