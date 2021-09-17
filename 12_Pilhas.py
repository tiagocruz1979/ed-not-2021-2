# Palindromo é um texto que quando lido de tràs para frente ,
# mantém o mesmo conteúdo (desprezando acentos e espaçamento)

palindromo = "SOCORRAM-ME, SUBI NO ÔNIBUS EM MARROCOS"
texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÃO"

pilha = []

# Percurso do palíndromo, colocando cada letra na lista

for letra in texto:
    pilha.append(letra) # append() sempre acrescenta por último

# #pervertendo a pilha con inserções no meio da pilha
# pilha.insert(10,'y')
# pilha.insert(19,'g')
# pilha.insert(6,'ç')
# # remoção de elementos em posiçõe sque não são a final 
# del pilha[11]
# del pilha[21]
# del pilha[8]

print(pilha)

inverso = ""

#Retira cada letra da lista , de trás para frente , e coloca no inverso 
while len(pilha) > 0:
    inverso += pilha.pop() # pop() retira sempre o último elemento

print(inverso)

# Pilha
# A pilha é um tipo abstrato de dados (TAD) que permite a entrada e a saída
# de dados apenas na sua extremidade final, como consequência, ela segue
# a regra LIFO ( Last in - first out - último a entrar , primeiro a sair)
# e tem acesso limitado aos seus elementos.


