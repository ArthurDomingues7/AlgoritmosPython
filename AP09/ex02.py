#Crie um procedimento chamado exibir_cliente(nome) 
# que receba o nome de um cliente e exiba a mensagem:

#Cliente: nome_informado
#No programa principal:

#leia o nome do cliente;
#chame o procedimento passando esse valor.

nome = ()

def exibir_cliente(nome):
    nome = str(input("digite o nome do cliente: "))
    print("Olá", nome)
    return(nome)

print(exibir_cliente(nome))