#Crie um programa em Python que leia 8 palavras e armazene todas elas em uma lista.

#Depois, exiba as palavras na ordem inversa da leitura.

#Importante: não use reverse() nem fatiamento com [::-1].

lista_palavras = []

for n in range(8):
    numero_lista = str(input("digite uma palavra: "))
    lista_palavras.append(numero_lista)
for n in range(len(lista_palavras)-1, -1, -1):
    print("as palavras ao contrário são", lista_palavras[n])