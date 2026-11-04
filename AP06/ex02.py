#Leia duas palavras de mesmo tamanho.

#Compare as duas palavras posição por posição, utilizando índices, 
# e determine quantas posições possuem caracteres diferentes.
#Ao final, mostre também quais posições são diferentes.

#Exemplo:
#casa
#capa
#As palavras diferem apenas na posição 2.

#Importante: utilize texto[i]. Não percorra diretamente os caracteres com for letra in texto.

palavra_1 = input("digite a palavra 1: ")
palavra_2 = input("digite a palavra 2: ")
diferentes = 0
pos_diferente = 0
letras = 0

if len(palavra_1) == len(palavra_2):
    for letra in range(len(palavra_1)):
        if palavra_1[letra] != palavra_2[letra]: #errado, vai comparar uma letra com a palavra_2 inteira
            diferentes += 1
            print("as palavras diferem nessas posições:", letras)
    print("as palavras diferem nessa quantidade de vezes: ", diferentes)
else:
    print("palavras não sao do mesmo tamanho, tente novamente")





