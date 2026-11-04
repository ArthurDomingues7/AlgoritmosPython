#Crie um programa em Python que leia 5 números inteiros digitados pelo usuário
#e armazene todos eles em uma lista.

#O programa deve exibir:

#a lista completa;
#cada elemento da lista, um por linha.

#Observação: criar uma lista, adicionar elementos com append 
# e percorrer uma lista, usando as duas formas possíveis 
# de percurso com for (por índice e por valor).

lista = []

for n in range(5):
    numero_lista = int(input("digite um numero: "))
    lista.append(numero_lista)
print("a lista é", lista)
for numero in lista:
    print(numero)
