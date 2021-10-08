"""
        Classe que representa cada unidade (elemento) da lista encadeada
        É dividida em duas partes:
        1) Onde fica armazenada a informação relevante para o usuário (data)
        2) O ponteiro para o próximo nodo da sequência (next)
"""
class Node:
    
    def __init__(self, val):
        self.data = val     # Armazena a informação do usuário
        self.next = None    # Ponteiro para o próximo nodo (None = nenhum)

    """
        Estrutura de dados LISTA ENCADEADA
        - A lista encadeada é uma estrutura de dados formada por unidade de informação chamada nodos ou nós
        - Cada nodo da lista encadeada tem duas partes: uma , que armazena a informação e outra que guarda o endereço do próximo  nodo da sequencia
        - a qualquer momento , temos um conhecimento apenas limitados de onde se encontram todos os nodos da lista. sabemos  apenas onde está o primeiro e o ultimo nodo da sequencia. Os nodos intermediarios precisam ser encontrados partindo-se do primeiro e percorrendo a sequencia
    """
class LinekdList:

    """
        Construtor da classe
    """

    def __init__(self):
        self.__head = None    # (cabeça) ponteiro para o primeiro nodo da lista
        self.__tail = None  # (cauda) Ponteiro para o último nodo da lista
        self.__count = 0    # contador de nodos

    """
        Método que informa se a lista está ou não vazia
    """
    def is_empty(self):
        return self.__count == 0

    def insert(self,pos,val):

        inserted = Node(val)

        # 1º caso: a lista está vazia. O nodo criada será , ao mesmo tempo , o primeiro e o último

        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted
    
        # 2º caso: inserção no inicio da lista (posicao 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head = inserted


        # 3º caso: inserção no fim da lista
        # vamos considerar qualquer posicação de inserção maior ou igual ao count como inserção no final
        elif pos >= self.__count:
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        else:
            before = self.__head 
            #percorre a lista encadeada da segunda posição (pos.1) até a posição Anterior àquela de inserção
            for i in range(1,pos): before = before.next

            # Nodo que ficará depois do inserido
            after = before.next

            # O next do nodo inserido passa a ser o after
            inserted.next = after

            # o next do nodo before passa a ser  o inserted
            before.next = inserted

        self.__count += 1

    """
        Método para inserir na primeira posição
    """
    def insertFront(self,val):
        self.insert(0,val)    

    """
        Método para inserir na última posição
    """
    def insertBack(self,val):
        self.insert(self.__count,val)


    """
        retorna o data do nodo  da posição desejada
    """
    def peek(self,pos):
        # Quando a lista estiver vazia ou a posiçlão estiver fora dos limites válidos (0.. count -1) , retorna None
        if self.is_empty() or pos < 0 or pos > self.__count -1: return None
        node = self.__head
        for i in range(0,pos):
            node = node.next
        return node.data

    """
        Método para procurar um valor na lista e retornar sua posição.
        REtorna -1 caso não encontre
    """
    def index(self,val):
        node = self.__head
        for pos in range(0,self.__count):
            if node.data == val: return pos
            node = node.next
        return -1 # Não encontrou


    """
        Método que imprime toda a lista . para fins de depuração
    """
    def to_str(self):
            string = ""
            node = self.__head
            for i in range(0,self.__count):
                if string != "": string += ", "
                string += f"(pos:: {i} data: {node.data})"
                node = node.next
            return "[" + string + " ]" +f"count: {self.__count}"



##################################################

lista = LinekdList()

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


