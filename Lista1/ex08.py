#Em diversas aplicações matemáticas é necessário determinar o Máximo Divisor
#Comum (MDC) e o Mínimo Múltiplo Comum (MMC) entre dois números.
#6
#Faça um programa que leia dois números inteiros positivos e calcule inicialmente o
#MDC utilizando o seguinte processo:
#enquanto os dois valores forem diferentes, subtraia o menor valor do maior;
#quando os dois valores se tornarem iguais, esse valor será o MDC.
#Depois, utilize o MDC encontrado para calcular o MMC por meio da relação:
#MMC(a, b) = a · b
#MDC(a, b)
#Ao final, exiba o MDC e o MMC dos dois números.
#Exemplo:
#Entrada:
#18, 24
#Saida:
#MDC: 6 MMC: 72

import math

numero_inteiro1 = int(input("digite um primeiro numero inteiro: "))
numero_inteiro2 = int(input("digite um segundo numero inteiro: "))
a = numero_inteiro1
b = numero_inteiro2

while numero_inteiro1 != numero_inteiro2:
    print(numero_inteiro1,numero_inteiro2)
    if numero_inteiro1 < numero_inteiro2:
        numero_inteiro2 -= numero_inteiro1
    if numero_inteiro2 < numero_inteiro1:
        numero_inteiro1 -= numero_inteiro2
if numero_inteiro2 == numero_inteiro1:
    mdc = numero_inteiro2
    mmc = (a * b) // mdc
print(mdc,mmc)