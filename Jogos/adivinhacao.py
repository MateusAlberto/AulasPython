print("************************************")
print("Bem vindo(a) ao jogo de Adivinhação!")
print("************************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou", chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!", end="\n\n")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.", end="\n\n")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.", end="\n\n")
    
    rodada += 1

print("************************************")
print("Fim do jogo")
print("************************************")