
"""
        Classe que representa cada unidade (elemento) da lista encadeada
        É dividida em três partes:
        1) O ponteiro para o nodo anterior da sequência (prev)
        2) Onde fica armazenada a informação relevante para o usuário (data)
        3) O ponteiro para o próximo nodo da sequência (next)
"""
import math

class Node:
    def __init__(self,val):
        self.prev = None    # Ponteiro para o nodo anterior (None = Nenhum)
        self.data = val     # Armazena a informação do usuário
        self.next = None    # Ponteiro para o próximo nodo (None - nenhum)

""" 
   ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA    - A lista encadeada é uma estrutura de dados formada por unidades      de informação chamadas nodos ou nós.    - Cada nodo da lista encadeada tem três partes: uma, que armazena a      informação; a segunda, que guarda o endereço do nodo anterior; e a      terceira, que guarda o endereço para o nodo seguinte da sequência    - A qualquer momento, temos um conhecimento apenas limitado de onde      se encontram todos os nodos da lista. Sabemos apenas onde está o      primeiro e o último nodo da sequência. Os nodos intermediários precisam      ser encontrados partindo-se do primeiro OU do último nodo e percorrendo      a sequência
"""

class DoublyLinkedList:
    """
        Construtor da classe 
    """
    def __init__(self):
        self.__head = None  # (cabeça) A ponta para o início da lista
        self.__tail = None  # (cauda) Aponta para o fim da lista
        self.__count = 0    # Contador de nodos
    

    """
        Método que informa se a lista está ou não vazia
    """
    def is_empty(self):
        return self.__count == 0


    """
        Método para retornar o número de nodos da lista
    """
    def count(self):
        return self.__count

    """
        Método privado que encontra um nodo data a sua posição
    """
    def __find_node(self, pos):
        #   Encontra o nodo fazendo o percurso a partir de __ head se ele estier na primeira metade da lista
        if pos < self.__count // 2:
            node = self.__head
            for i in range(1,pos+1): node = node.next
        #   se, ao contrário, o nodo estiver na segunda metada da lista compensa fazer o percurso reverso desde o __tail
        else:
            node = self.__tail
            for i in range(self.__count-2,pos-1, -1): node = node.prev
        
        return node


    """
        Método que encontra a posição dado o seu valor
    """
    def index(self, val):
        # Encontra a posição do meio d lista. Se o resultado for fracionário, considera o próximo número inteiro
        meio = math.ceil(self.__count / 2 )
        
        # Inicializa dois nodos, um com a cabeça e outro com a cauda da lista
        node1 = self.__head
        node2 = self.__tail
        
         # Contador que vai até a metade da lista
        for pos in range(0,meio):
            if(node1.data == val): return pos   # Retorna a posição encontrada
            if(node2.data == val): return self.__count - 1 - pos # Retorna a posição retroativa
            node1 = node1.next # node1 anda para frente
            node2 = node2.prev # node2 anda para trás
        
        return -1   # Não encontrou o valor na lista

    """
        Método para inserção de novo nodo na lista
    """
    def insert(self, pos, val):
        inserted = Node(val)

        #   1º caso : lista vazia
        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted
        
        #   2º caso: inserção na posicao inicial
        elif pos == 0:
            inserted.next = self.__head # Aponta para o seguinte
            self.__head.prev = inserted # aponta para o anterior
            self.__head = inserted      # Ajusta o início da lista

        #   3º caso: inserção na posição final
        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted
        
        # 4º caso : inserção na posição intermediária
        else:
            node_pos = self.__find_node(pos)
            before = node_pos.prev
            before.next = inserted
            inserted.prev = before
            inserted.next = node_pos
            node_pos.prev = inserted


        self.__count += 1
    
    """
        Método de atalho para inserção no início da lista
    """
    def insert_head(self, val):
        self.insert(0,val)

    """
        Método de atalho para inserção no final da lista
    """
    def insert_tail(self,val):
        self.insert(self.__count, val)

    """
        Método para remoção de item
    """
    def remove(self,pos):

        # 1º caso : lista vazia ou posição fora dos limites
        if self.is_empty() or pos < 0 or pos > self.__count - 1: return None

        # 2º caso: Remoção do início da lista
        if pos == 0:
            # será removido o __head da lista
            removed = self.__head
            # O novo __head passa a ser o nodo seguinte ao removido
            self.__head = removed.next
            # se __head for um nodo válido , ele não pode ter antecessor(prev)
            if self.__head is not None: self.__head.prev = None
            # Em caso de remoção do único nodo restante, __head é None e __tail precisa ser None também
            if self.__count == 1: self.__tail = None

        # 3º caso: remoção do último nodo
        elif pos == self.__count -1:
            # Será removido o __tail da lista
            removed = self.__tail
            # O novo _tail passa a ser o nodo anterior ao removido
            self.__tail = removed.prev
            # Se __tail for um nodo válido, ele não pode ter sucessor (next)
            if self.__tail is not None: self.__tail.next = None
            # Em caso de remoção do único nodo restante, __tail é None, __head precisa ser None também
            if self.__count == 1: self.__head = None

        # 4º caso: remoção de posição intermediária
        else:
            # Manda encontrar o nodo a ser removido
            removed = self.__find_node(pos)
            before = removed.prev # Nodo anterior ao removido
            after = removed.next # Nodo posterior ao removido
            # O nodo before passa a apontar a frente para o nodo after
            before.next = after
            # O Nodo after passa a apontar para tras , para o nodo before
            after.prev = before

        self.__count -= 1
        return removed.data

    """
        Método de atalho para remoção na primeira posição
    """
    def remove_head(self):
        return self.remove(0)
    
    """
        Método de atalho para remoção na ultima posição
    """
    def remove_tail(self):
        return self.remove(self.count()-1)

    """
        Método para consultar qualquer nodo dada a sua posição
    """
    def peek(self, pos):
        # Lista vazia ou posição fora dos limites
        if self.is_empty() or pos < 0 or pos > self.__count - 1: return None
        node = self.__find_node(pos)
        return node.data

    """
        Método de atalho para mostrar o primeiro nodo
    """
    def peek_head(self):
        return self.peek(0)

    """
        Método de atalho para mostrar o último nodo
    """
    def peek_tail(self):
            return self.peek(self.__count - 1)

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
