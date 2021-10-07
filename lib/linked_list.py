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

            #percorre a lista encadeada até a posição anterior àquela inserção
            for i in range(0,pos):
                print(f"before.data: {before.data}, i:{i}")
                before = before.next


        self.__count += 1


        print(f"[NODE] data: {inserted.data} , next: {inserted.next}")

##################################################

lista = LinekdList()

lista.insert((0), "1 kg de batata")
lista.insert((1), "café")
lista.insert((2), "miojo")
lista.insert((3), "óleo")
lista.insert((4), "sabonete")
lista.insert((5), "shampoo")

lista.insert((4), "tomate")






