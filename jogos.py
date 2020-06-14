import forca
import adivinhacao


def escolhe_jogo():
    opcao_jogo = None

    while(opcao_jogo != 'S'):
        print('\n*********************************')
        print('****   Escolha o seu jogo!   ****')
        print('*********************************')

        print('Lista de jogos:')
        print('(1) Forca')
        print('(2) Adivinhação')
        print('(S) Sair')
        try:
            opcao_jogo = input("Escolha uma opção: ").upper()

            if (opcao_jogo == '1'):
                forca.jogar()
            elif (opcao_jogo == '2'):
                adivinhacao.jogar()
            elif (opcao_jogo == 'S'):
                break
            else:
                print("Opção incorreta")
        except Exception:
            opcao_jogo = None


if(__name__ == '__main__'):
    escolhe_jogo()
