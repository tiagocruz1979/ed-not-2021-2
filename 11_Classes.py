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
    base = 0
    altura = 0
    tipo = "R"  #Retângulo

    #algoritmos 
    # São representado por funções que , quando se encontram
    # dentro de uma classe , ganham o nome de Métodos

    # Este método é executado quando um objeto é criado a partir
    # de uma classe (construtor)
    def __init__(self, base, altura, tipo = "R"):
        # recebe os valores passados ao construtor e os armazena dentro 
        # dos atributos
        if base <= 0:
            raise Exception("A Base deve ser maior que zero")
        elif altura <= 0:
            raise Exception("A altura deve ser maior que zero")
        elif tipo not in["R","T","E"]:
            raise Exception("O Tipo deve ser R, T ou E.")
        
        self.base = base
        self.altura = altura
        self.tipo = tipo


#######################################################################

#criando objetos a partir da classe
retangulo1 = FormaGeometrica(15,10,"R")  # chama o __init__
triangulo1 = FormaGeometrica(6,9,"T")

print(f'[retangulo1] base: {retangulo1.base} , altura: {retangulo1.altura}, tipo: {retangulo1.tipo}')

print(f'[triangulo1] base: {triangulo1.base} , altura: {triangulo1.altura}, tipo: {triangulo1.tipo}')
