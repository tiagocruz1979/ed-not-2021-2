# Classe é uma estrutura que representa conjuntamento 
# tanto dados quanto algoritimos. Uma classe é como se 
# fosse uma "forma de bolo" com a qual podemos criar
# diferentes "bolos" (objetos)
# Cada "bolo"(objeto) pode ser feito com seus próprios 
# ingredientes (dados) e modos de fazer (algoritmos), mas
# terão sempre o formato determinado pela "fôrma" (classe).

class FormaGeometrica():
    # Dados
    #Quando pertencem a uma classe , ganham o nome de Atributos
    #base = 0
    #altura = 0
    #tipo = "R"  #Retângulo

    #algoritmos 
    # São representado por funções que , quando se encontram
    # dentro de uma classe , ganham o nome de Métodos

    # Este método é executado quando um objeto é criado a partir
    # de uma classe (construtor)
    def __init__(self, base, altura, tipo = "R"):
        # recebe os valores passados ao construtor e os armazena dentro 
        # dos atributos

        if type(base) not in [int,float] or base <= 0:
            raise Exception("A base deve ser numérica e maior do que 0")
        elif type(altura) not in [int,float] or altura <= 0:
            raise Exception("A altura deve ser numérica e maior do que zero")
        elif tipo not in["R","T","E"]:
            raise Exception("O Tipo deve ser R, T ou E.")
        
        self.__base = base  # colocamos __ para indicar que o atributo é privado
        self.__altura = altura
        self.__tipo = tipo

    #getter é um método que possibilida sabero valor de um atributo
    # privado do lado de fora da classe
    def __get_base(self):
        return self.__base
    
    #setter é um método que possibilida atribuir um valor de um atributo
    # privado do lado de fora da classe
    def __set_base(self, valor):
        if type(valor) not in [int,float] or valor <= 0:
            raise Exception("A base deve ser numérica e maior do que 0")

        self.__base = valor 
    
    # property "esconde" as funçoes getter e setter dentro do nome
    # de um atributo, tornando mais simples a manipulação do objeto
    base = property(__get_base, __set_base)

    # Essas linhas comaçadas com @ são chamadas "decorators"
    # Os decorators instruem o Python a criar uma property com 
    # um getter e um setter na hora da execução
    @property
    def altura(self): # Getter para a propriedade chamada "altura"
        return self.__altura
    
    @altura.setter
    def altura(self,valor): #setter para a propriedade chamada "altura"
        if type(valor) not in[int,float] or valor <= 0:
            raise Exception("A altura deve ser numérica e maior que zero")
        
        self.__altura = valor

#######################################################################

#criando objetos (instanciando) a partir da classe
retangulo1 = FormaGeometrica(15.5,10,"R")  # chama o __init__
triangulo1 = FormaGeometrica(6,9,"T")


# burlando o sistema de detecção de erro
#retangulo1.__base = 0
#retangulo1.__altura = -10
#retangulo1.__tipo = "sfds"


#problematico= FormaGeometrica(15.9,5,"W")

#retangulo1.set_base(-59.6)
retangulo1.base = 9.6 # vai executar o set_base da classe
print(f"[retangulo1] base: {retangulo1.base}") # vai executar o get_base da classe , proporcionado pelo property



#print(f'[retangulo1] base: {retangulo1.__base} , altura: {retangulo1.__altura}, tipo: {retangulo1.__tipo}')

#print(f'[triangulo1] base: {triangulo1.__base} , altura: {triangulo1.__altura}, tipo: {triangulo1.__tipo}')

#print(f'[problematico] base: {problematico.base} , altura: {problematico.altura}, tipo: {problematico.tipo}')




