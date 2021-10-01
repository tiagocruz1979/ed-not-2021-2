class Queue:
    """
    Estrutura de Dados Fila
    - Fila é uma lista linear de acesso restrito, que permite apenas as operações de enfileiramento (enqueue) e desenfileiramento (dequeue), a primeira
    ocorrendo no final da estrutura e a seguda no inicio da estrutura.
    - como consequência , a fila funciona pelo princípio FIFO ( First in, first out - primeiro a entrar , primeiro a sair).
    - a Principal aplicação das filas são tarefas que envolvem o processamento de tarefas por ordem de chegada
    """
    """
        Construtor da classe
    """
    def __init__(self):
        self.__data = []    # inicializa uma lista privada vazia

    """
        Método para inserção
        o Nome do método para inserção em filas é padronizado: enqueue()
    """
    def enqueue(self, val):
        self.__data.append(val)     # insere no final da fila

    """
        Método para retirada
        o nome do método de retirada em filas também é
        padronizado: dequeue()
    """
    def dequeue(self):
        if self.is_empty(): return None
        # retira e retorna o primeiro da fila
        return self.__data.pop(0)

    """
        Método para consultar o início da fila (primeiro elemento), sem retirá-lo
        Nome padronizado: peek()
    """        
    def peek(self):
        if self.is_empty(): return None
        return self.__data[0]

    """
        Método para verificar se a fila está vazia ou não 
        Retorna True se vazia ou False caso contrário
    """
    def is_empty(self):
        return len(self.__data) == 0

    """
        Método que exibe a fila como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        for el in self.__data:
            if string != "": string += ", "
            string += str(el)
        return "[" + string + " ]"

