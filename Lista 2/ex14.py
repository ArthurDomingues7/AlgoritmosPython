#Umalistadenúmeros inteirosdeveserreorganizadadeformaquetodososvalores
#paresapareçamantesdosvaloresímpares.
#Crieuma funçãochamadaseparar_pares_impares(valores)que retorne
#umanovalistacomessaorganização,preservandoaordemrelativaemqueosnú
#merosparesaparecementresieaordemrelativadosnúmerosímparesentresi.
#Porexemplo:
#[7, 4,2,9,6,3,8]
#deveproduzir:
#[4, 2,6,8,7,9,3]
#Nãoutilizesorted()pararesolveraquestão.

lista_numeros = []

def separar_pares_impares(valores):
    nova_lista = []
    for n in lista_numeros:
        if n % 2 == 0:
            nova_lista.append(n)
    for n in lista_numeros:
        if n % 2 == 1:
            nova_lista.append(n)
    return nova_lista

contador = 0
while contador == 0:
    valores = int(input("Digite um valor: "))
    if valores == 0:
        contador += 1
    else:
        lista_numeros.append(valores)

resultado = separar_pares_impares(lista_numeros)
print(resultado)