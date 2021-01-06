print("************************************")
print("Bem vindo(a) ao jogo de Adivinhação!")
print("************************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou", chute)

if (numero_secreto == chute):
    print("Você acertou!", end="\n\n")
else:
    print("Você errou!", end="\n\n")

print("************************************")
print("Fim do jogo")
print("************************************")