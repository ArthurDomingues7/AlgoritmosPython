#Retome o cálculo do Exercício 3. Desta vez, o usuário não informará o percentual: 
# o programa deverá escolhê-lo de acordo com a idade.
#Leia a idade e o preço normal do ingresso.
#menor que 12 anos: desconto de 50%;
#12 a 17 anos: desconto de 30%;
#18 a 59 anos: sem desconto;
#60 anos ou mais: desconto de 40%.
#Apresente percentual de desconto, valor do desconto e valor final.
#Teste: 11, 12, 17, 18, 59 e 60 anos.

idade = int(input("digitar idade "))
preco_normal = int(input("digitar preço "))
preco_final = 0
percentual_desconto = 0

if idade < 12:
    preco_final = preco_normal * (50 / 100)
    percentual_desconto = 50
    valor_desconto = preco_normal - preco_final
if idade >= 12 and idade < 18:
    preco_final = preco_normal * (30 / 100)
    percentual_desconto = 30
    valor_desconto = preco_normal - preco_final
if idade >= 18 and idade < 60:
    preco_final = preco_normal
    percentual_desconto = 0
    valor_desconto = preco_normal - preco_final
if idade >= 60:
    preco_final = preco_normal * (40 / 100)
    percentual_desconto = 40
    valor_desconto = preco_normal - preco_final
print(f"percentual de desconto:", percentual_desconto ,"valor do desconto:", valor_desconto ,"valor final:", preco_final)

