#print(): utilizado para exibir informações
print("Olá Mundo é o caralho! Meu nome é Zé Pequeno!")

#input(): permite entrada de informações
nome = input("Qual é o seu nome? ")
print(f"Ok! Seu nome é {nome}")

# int() converte o valor informado no input() para numero inteiro
idade =int(input("Informe a sua idade: "))

if idade >= 18:
    print("Você já pode beber.")
    print("Você já pode tirar a carteira de habilitação")
else:
    print("Você não pode beber")
    print("Você não pode tirar carta seu infeliz!")

