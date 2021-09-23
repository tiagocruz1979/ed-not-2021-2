"""
    Analisador de expressões matemáticas
"""
from lib.stack import Stack

simbolos = {
    "P": "parêntese",
    "C": "colchete",
    "X": "chave"
}

expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1] * 3} / 5"
#expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1]] * 3} / 5"
#expressao = "2 * {4 - {7 / [(5 - (7 * 9) + 1] * 3} / 5"

analisador = Stack()    #cria a pilha

def verif_fechamento(tipo_fecha, pos_fecha , dados_abre):
    #pass # não faz nada ; função vazia
    
    # se o tipo que veio da pilha for igual ao tipo encontrado no fechamento, OK
    #print(f"DEBUG - > tipo_fecha:{tipo_fecha},  pos_fecha: {pos_fecha} , dados_abre: {dados_abre}")
    
    if dados_abre is None: # A Pilha ficou vazia antes do término da análise da expressão
        print(f"ERRO: Há mais símbolos de fechamento do que símbolos de abertura na expressão, tipo {tipo_fecha}, posicao {pos_fecha}")
    elif dados_abre["tipo"] == tipo_fecha:
        print(f"Símbolo {tipo_fecha} aberto na posicao {dados_abre['pos']} e fechado na posição {pos_fecha}")
    else:   #tipos errados
        print(f"ERRO: símbolo de fechamento do tipo {tipo_fecha} encontrado {pos_fecha}; esperado símbolo do tipo {dados_abre['tipo']}")

# percorre a expressão em usca de parenteses, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        # Empilha informações sobre o abre parenteses
        analisador.push({"tipo": "P","pos": pos})
    elif expressao[pos] == "[":
        # Empilha informações sobre o abre colchetes
        analisador.push({"tipo": "C", "pos": pos})
    elif expressao[pos] == "{":
        #empilha informações osbre o abre chaves
        analisador.push({"tipo": "X", "pos": pos})
    elif expressao[pos] == ")":
        verif_fechamento("P", pos, analisador.pop())
    elif expressao[pos] == "]":
        verif_fechamento("C", pos, analisador.pop())
    elif expressao[pos] == "}":
        verif_fechamento("X", pos, analisador.pop())

# Verificar se houve sobra(s) na pilha
while not analisador.is_empty():
    sobra = analisador.pop()
    print(f"ERRO: símbolo de abertura {sobra['tipo']} sem simbolo de fechamento correspondente na posicao {sobra['pos']}")

#print(analisador.to_str())

    