#Agora retome a lógica do Exercício 1.

#Leia o saldo disponível e o valor da compra.

#Se o saldo for suficiente, informe que a compra foi aprovada e mostre o saldo restante. Caso contrário, informe que a compra foi recusada e mostre quanto dinheiro ainda faltaria.

#Exemplo 1:

#Saldo disponível: 250.00
#Valor da compra: 180.00

#Compra aprovada.
#Saldo restante: R$ 70.00
#Exemplo 2:

#Saldo disponível: 100.00
#Valor da compra: 135.00

#Compra recusada.
#Valor que falta: R$ 35.00

saldo_disp = int(input("digite o saldo: "))
valor_compra = int(input("digite o valor da compra: "))

if saldo_disp >= valor_compra:
    saldo_pos_compra = saldo_disp - valor_compra
    print("compra aprovada")
    print(f"seu saldo é", saldo_pos_compra)
if saldo_disp < valor_compra:
    print("compra aprovada")
    print(f"valor que falta é: ", valor_compra - saldo_disp)