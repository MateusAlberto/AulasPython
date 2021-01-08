import random

def jogar():
    print("************************************")
    print("Bem vindo(a) ao jogo de Forca!")
    print("************************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    posicao = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    total_tentativas = 6

    print(letras_acertadas)

    #Game loop
    while(not enforcou and not acertou):
                
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f'Ops, você errou! Falta(m) {total_tentativas-erros} tentativa(s)...')

        enforcou = erros == total_tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("************************************")
    print("Fim do jogo")
    print("************************************")

if(__name__ == "__main__"):
    jogar()