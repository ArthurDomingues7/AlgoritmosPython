#Crie um programa em Python que leia 6 números reais e armazene os valores em uma lista.

#Depois, calcule e exiba:

#a soma dos valores;
#a média dos valores.
#Exemplo de entrada
#5.0
#7.5
#8.0
#6.5
#10.0
#9.0
#Saída esperada
#Soma: 46.0
#Média: 7.666666666666667

lista_valores = []
soma = 0
media = 0

for n in range(6):
    valores = float(input("digite um numero real:"))
    lista_valores.append(valores)
for n in lista_valores:
    soma += n
media += soma / len(lista_valores)
print("soma: ", soma)
print("media: ", media)
#media += soma % range
#print("soma: ", soma)
#print("media: ", media)