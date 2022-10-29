#Programa de verificação com 2 fatores de soma
#A soma dos 2 fatores precisa ser 20

senha = int(input("senha: "))
contrasenha = int(input("Contra senha: "))

x = senha + contrasenha

while (x != 20):
    print("ACESSO NEGADO")
    contrasenha = int(input("Contra senha: ")) # Essa linha não está somando com o valor de {senha}

if (x == 20):
    print("ACESSO LIBERADO")






