# importar o valor da constante pi
# math é o nome da biblioteca onde pi se encontra
from math import pi


def area_forma(base, altura, forma='R'):
    """
        Função que calcula a área de uma das seguintes formas feometricas: retangulo , triangulo ou elipse
        parametro
        "R" == retangulo (parâmetro opcional com valor padrão)
        "T" == triangulo
        "E" == elipse
    """
    area = 0
    if forma == "R": # retângulo
        area = base * altura
    elif forma == "T": # triangulo
        area = base * altura / 2
    elif forma == "E" or forma == "C": # elipse ou circulo
        area = ( base / 2 ) * ( altura /2 ) * pi
    return area

print(f"Retângulo 7.5x11: {area_forma(7.5,11.0,'R')}")
print(f"Triângulo 6.5x10.5: {area_forma(7.5,11.0,'T')}")
print(f"Elipse 8.8x15.7: {area_forma(8.8,15.7,'E')}")
print(f"Circulo 15.0x15.0: {area_forma(15.0,15.0,'E')}")
print(f"Retangulo 5.5x4.5 (sem parametro): {area_forma(5.5,4.5)}")
print(f"Parametro invalido: {area_forma(3.0,3.7,'X')}")
print(f"Circulo 1.0x1.0: {area_forma(1.0,1.0,'C')}")



