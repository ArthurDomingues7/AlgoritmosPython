#Leia:

#o preço normal de um ingresso;
#o percentual de desconto, informado pelo usuário.
#Calcule e apresente:

#o valor do desconto;
#o valor final do ingresso.
#Utilize:

#valor_desconto = preco_normal * (percentual_desconto / 100)
#valor_final = preco_normal - valor_desconto
#Neste momento, o usuário informa diretamente o percentual. Mais adiante, o próprio programa irá decidir qual desconto deve ser aplicado.

#Exemplo:

#Preço normal: R$ 80.00
#Percentual de desconto: 30

#Valor do desconto: R$ 24.00
#Valor final: R$ 56.00

preco_normal = int(input("digite o preço normal: "))
percentual_desconto = int(input("digite o desconto percentual: "))
valor_desconto = preco_normal * (percentual_desconto / 100)
valor_final = preco_normal - valor_desconto

print(preco_normal)
print(valor_final)