def jogar():
    import random
    print ("*******************************")
    print ("Bem-vindo ao jogo de advinhação")
    print ("*******************************")

    numero_secreto = random.randrange (1,101)
    pontos = 1000

    print("Qual o número de dificuldade?")
    print ("(1)Fácil (2)Médio) (3)Difícil")


    nivel = int(input ("Definir o nível: "))
b
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range (1, tentativas+1):
        print ("Tentativa {} de {}".format(rodada, tentativas))
        chute = input ("Digite um número entre 1 e 100: ")
        print ("Você digitou: " + chute)
        chute = int(chute)

        if (chute < 1) or (chute >100):
                print ("Você deve digitar um número entre 1 e 100!")
                continue


        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print ("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print ("É menor que isso")
            elif (menor):
                print("É maior que isso")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print ("O número secreto era: ", numero_secreto)

if (__name__ =="__main__"):
    jogar()