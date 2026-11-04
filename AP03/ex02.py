#Leia um número inteiro.
#Calcule e apresente:
#o próprio número;
#o resultado da divisão inteira por 2 utilizando //;
#o resto da divisão por 2 utilizando %.
#Não classifique o número como par ou ímpar ainda. Apenas observe o valor produzido pelo operador %.
#Exemplos:

#Número: 8
#Divisão inteira por 2: 4
#Resto da divisão por 2: 0

#Número: 7
#Divisão inteira por 2: 3
#Resto da divisão por 2: 1#

num_int = int(input("digite um numero inteiro: "))
num_div = num_int // 2
resto = num_int % 2 

print(num_div)
print(resto)
