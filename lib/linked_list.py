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
class LinkedList:

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
        Método para remover elemento da lista
    """
    def remove(self,pos):

        # 1º caso: lista vazia ou posição fora dos limites
        # (menor que 0 ou mairo que count -1) 
        if self.__count == 0 or pos < 0 or pos > self.__count - 1:
            return None
        
        #2º case: remoção inicio da lista
        if pos == 0:
            removed = self.__head   # Nodo removido
            self.__head = self.__head.next   #Passa a apontar o nodo seguinte
        
        # 3º caso: remoçoes intermediárias ou final
        else:
            # Percorre a lista até encontrar o item anterior da posição a ser removida (before)
            before = self.__head
            for i in range(1, pos): before = before.next
            # o Removido será o sucessor do before
            removed = before.next
        
            # Nodo da posição seguinte à de remoção
            after = removed.next

            # O nodo anterior (before) passa apontar para o nodo seguinte (after)
            before.next = after

            # Atualizando o tail caso a remoção seja o último nodo
            if removed == self.__tail:
                self.tail = before

        self.__count -= 1
        # Retorna o valor armazenado no nodo removido
        return removed.data     
        
    
    """
        Método de atalho para remoção do primeiro item da lista
    """
    def removeHead(self):
        return self.remove(0)
    
    """
        Método de atalho para remoão do último item da lista
    """
    def removeTail(self):
        return self.remove(self.__count-1)
    
    """
        Método que retorna a quantidade de itens da lista
    """
    def count(self):
        return self.__count
    
    
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





