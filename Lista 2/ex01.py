# Você está desenvolvendo o módulo de segurança de um aplicativo financeiro. 
# Durante o cadastro, o sistema pede ao usuário que crie uma senha. 
# Crie uma função validar_senha(senha) que verifique se a senha é segura. 
# Uma senha é válida se: tiver pelo menos 8 caracteres, contiver pelo menos
# um número, contiver pelo menos uma letra maiúscula e não contiver espaços. 
# O programa principal deve ler senhas repetidamente até que o usuário digite
# "sair", imprimindo "Válida" ou "Inválida" para cada tentativa, e ao final 
# informar a porcentagem de senhas válidas testadas

senha = int(input("digite uma senha: "))

def validar_senha(senha):
   if len(senha) < 8:
        return False
   for caractere in senha:
    if caractere.isdigit():
        tem_numero = True


#while sair != True:
    #senha = int(input("digite uma senha: "))
    #print(validar_senha)
    #if sair == True:
        #break

# ta tudo errado