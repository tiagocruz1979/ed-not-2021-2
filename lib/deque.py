class Deque:
    """
        - Deque = Double Ended Queue (fila de duas pontas)
        - Deque é uma lista linear de acesso restrito , que permite apenas as operações de enfileiramento ( insert_front/Insert_Back) e desenfileiramento (remove_front/remove_back), acontecendo em qualquer uma das extremidades da estrutura. 
        - como consequência, o deque não segue o princípio FIFO (First In , First Out) - primeiro a entrar , primeiro a sair).
        - a Principal aplicação dos deques são situações em que filas precisam aceitar a inserção de itens prioritários e a desistência do último item
    """

    """
        Construtor da classe
    """
    def __init__(self):
        self.__data = []    #Inicializa uma lista privada varia

    """
        Método para inserção no início do deque
    """
    def insert_front(self, val):
        self.__data.insert(0,val)

    """
        Método para inserção no final do deque
    """
    def insert_back(self,val):
        self.__data.append(val)
    
    """
        Método para remoção no início da deque
    """
    def remove_front(self):
        if self.is_empty(): return None
        return self.__data.pop(0)
    
    """ 
        Método para remoção no final da deque
    """
    def remove_back(self):
        if self.is_empty(): return None
        return self.__data.pop()

    """
        Método para verificar qual é o primeiro elemento da fila
    """
    def peek_front(self):
        if self.is_empty(): return None
        return self.__data[0]

    """
        Método para verificar qual é o último elemento da deque
    """
    def peek_back(self):
        if self.is_empty(): return None
        return self.__data[-1]


    """
        Método para verirficar se a deque está vazia
    """
    def is_empty(self):
        return len(self.__data) == 0 
        
    """
        Método que exive o deque como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        for el in self.__data:
            if string != "": string += ", "
            string += str(el)
        return "[" + string + " ]"

