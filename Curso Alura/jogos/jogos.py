import forca
import advinhacao

def escolha_jogo():
    print ("*******************************")
    print ("******Escolhao seu jogo********")
    print ("*******************************")
    print ("(1) Forca  (2) Advinhação")
    jogo = int(input("Qual o jogo?"))
    if (jogo==1):
        print ("jogando Forca")
        forca.jogar()
    elif (jogo==2):
        print ("jogando Advinhação")
        advinhacao.jogar()
if (__name__== "__main__"):
    escolha_jogo()


