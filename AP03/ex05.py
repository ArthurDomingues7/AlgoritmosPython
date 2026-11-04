#Retome o uso do operador % trabalhado no Exercício 2.

#Leia um número inteiro e apresente duas informações independentes:

#se o número é positivo, negativo ou zero;
#se o número é par ou ímpar.
#Atenção: classificar o sinal e verificar a paridade são duas decisões diferentes. 
#Pense se elas devem fazer parte da mesma cadeia de if / elif / else.

num_int = int(input("digite um numero inteiro: "))

if num_int // 2 == 0:
    print("o numero", num_int, "é par")
if num_int < 0:
    print("o numero", num_int, "é negativo")
if num_int > 0:
    print("o numero", num_int, "é positivo")
if num_int < 0:
    print("o numero", num_int, "é neutro")