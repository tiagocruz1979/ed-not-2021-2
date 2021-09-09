# Dicionario é uma estrutura da linguagem Python
# capaz de armazenar multiplos valores em uma única
# variável, por meio e pares de chave-valor
pessoa = {
    #"nome" é a chave
    #"Fulano de tal" é o valor
    "nome": "Fulano de Tal",
    "sexo": "M",
    "Idade": 39,
    "peso": 76,
    "altura": 1.82
}

print(pessoa)

imc = pessoa["peso"]/(pessoa["altura"]**2)
print(f"O IMC de {pessoa['nome']} é {imc}.")

forma1 = {
    "base": 7.5,
    "altura": 12.0,
    "tipo": "R" # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo":"T"  #Triângulo
}


forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     #elipse
}


forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "W"     #Tipo não reconhecido
}

forma5 = {
    "legume":"batata",
    "fruta":"abacate",
    "tipo":"T"
}


from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": # caso ser um retangulo
        return forma["base"]*forma["altura"]
    elif forma["tipo"]=="T":
        return forma["base"]*forma["altura"] / 2
    elif forma["tipo"]=="E":
        return forma["base"]/2 * forma["altura"]/2 * pi
    else:
        #gerar um erro
        raise Exception("Tipo de forma não reconhecido.")

print(f"Área de um retângulo de 7.5x12: {calcular_area(forma1)}")
print(f"Área de um triângulo 6x2.5: {calcular_area(forma2)}")
print(f"Área de uma elipse de 5x3: {calcular_area(forma3)}")
#print(f"Área de uma forma W de 10x5: {calcular_area(forma4)}")
#print(f"Área de um objeto imcompatível0x5: {calcular_area(forma5)}")