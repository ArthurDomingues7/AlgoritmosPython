#Um plano de internet possui um limite mensal de dados. 
# O sistema precisa informar ao usuário se seu consumo 
# ainda está dentro do pacote contratado.

#Leia o limite do plano, em GB, e o consumo atual, em GB.

#Se o consumo for menor ou igual ao limite, informe que o 
#usuário ainda está dentro do plano e mostre quantos GB restam. 
#Caso o consumo seja maior que o limite, informe que o pacote foi
#excedido e mostre quantos GB foram utilizados além do permitido.

limite = int(input("Qual o limite do plano? "))
consumo_usuario = int(input("Digite o seu consumo: "))

if consumo_usuario <= limite:
    print("usuário ainda está dentro do plano, restam", limite-consumo_usuario, "Gigas." )
else:
    print("o pacote foi excedido, passaram-se", consumo_usuario-limite, "Gigas." )