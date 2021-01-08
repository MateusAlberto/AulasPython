def jogar():
    print("************************************")
    print("Bem vindo(a) ao jogo de Forca!")
    print("************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    #Game loop
    while(not enforcou and not acertou):
        
        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f'Encontrei a letra {letra} na posição {index}')
            index += 1

    print("************************************")
    print("Fim do jogo")
    print("************************************")

if(__name__ == "__main__"):
    jogar()