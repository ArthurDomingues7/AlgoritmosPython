#O calendário gregoriano utiliza uma regra especial para determinar os anos que
#possuem 366 dias. Um ano é bissexto quando é divisível por 4, exceto os anos
#divisíveis por 100, que somente são bissextos quando também são divisíveis por 400.
#Faça um programa que leia um ano inteiro positivo e informe se ele é bissexto ou
#não bissexto.
#Exemplos:
#2024 é bissexto;
#1900 não é bissexto;
#2000 é bissexto;
#2025 não é bissexto.

inteiro_positivo = int(input("digite um numero inteiro positivo: "))

if inteiro_positivo % 4 == 0 (inteiro_positivo % 4 == 0 and inteiro_positivo % 100 != 0):
    print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")