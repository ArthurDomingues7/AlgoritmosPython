#Crie uma função chamada calcular_comissao(valor_venda) que receba o valor 
# de uma venda e retorne a comissão correspondente a 5% desse valor.

#No programa principal:

#leia o valor da venda;
#chame a função;
#exiba o valor retornado.

def calcular_comissao(valor_venda):
    valor_venda = int(input("digite o valor da venda: "))
    desconto = valor_venda / 20
    return(desconto)

print(calcular_comissao(valor_venda))

#incompleto