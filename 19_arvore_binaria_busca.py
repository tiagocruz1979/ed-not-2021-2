
from lib.binary_search_tree import BinarySearchTree

arvore = BinarySearchTree()

lista=[48,15,71,1,29,5,88,13,19,37,51,64,23,21,25]
for i in range(len(lista)):
    arvore.insert(lista[i])


print(arvore.to_str())

em_ordem = []

def insere_em_ordem(val):
    em_ordem.append(val)

arvore.in_order_traversal(insere_em_ordem)

print('Percurso em ordem:', em_ordem)


sumario = BinarySearchTree()
lista2=['2','1','3','1.1','3.1','2.1','2.1.1']
for i in range(len(lista2)):
    sumario.insert(lista2[i])

em_ordem=[]
sumario.in_order_traversal(lambda val: em_ordem.append(val))

print(em_ordem)

pre_ordem=[]
sumario.pre_order_traversal(lambda val: pre_ordem.append(val))

print(pre_ordem)

pos_ordem=[]
arvore.post_order_traversal(lambda val: pos_ordem.append(val))
print('Árvore pós-ordem:', pos_ordem)

existe36 = arvore.exists(36)
existe51 = arvore.exists(51)
existe64 = arvore.exists(64)
print(f'36: {existe36}, 51: {existe51}, 64: {existe64}')


print(lista)

# teste de exclusão
print('---------------- Teste de exclusão''''''''''''''')

arvoreex = BinarySearchTree()

listaexclusao=[48,15,71,1,29,5,88,13,19,37,51,64,23,21,25]
for i in range(len(listaexclusao)):
    arvoreex.insert(listaexclusao[i])

em_ordem =[]
arvoreex.in_order_traversal((lambda val: em_ordem.append(val)))
print('Antes da exclusão do 29', em_ordem)

noremovido = arvoreex.remove(29)
em_ordem =[]
arvoreex.in_order_traversal((lambda val: em_ordem.append(val)))
print('Após a exclusão do 29', em_ordem)

# observando qual valor se tornou a nova raiz
# fazendo um percurso pre-ordem e verificando o primeiro valor retornado 
pre_ordem = []
arvoreex.pre_order_traversal(lambda val: pre_ordem.append(val))
print('Novo novo raiz sem o valor ', pre_ordem[0])