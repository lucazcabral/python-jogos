import random


def jogar() -> None:
    print('#======================================#')
    print("#  Bem vindo ao jogo de Adivinhação!   #")
    print('#======================================#')

    LIMITE_NUMERO_MINIMO = 1
    LIMITE_NUMERO_MAXIMO = 100

    numero_secreto = random.randint(LIMITE_NUMERO_MINIMO, LIMITE_NUMERO_MAXIMO)

    print('Qual nível de dificuldade desejada?')
    print('1 - Fácil   2 - Médio   3 - Difícil ')
    nivel_dificuldade = int(input())
    pontuacao = 1000
    pontos_perdidos_erro = 50

    if(nivel_dificuldade == 1):
        quantidade_tentativas = 20
    elif(nivel_dificuldade == 2):
        quantidade_tentativas = 10
    elif(nivel_dificuldade == 3):
        quantidade_tentativas = 5
    else:
        raise IOError("Seleção de nível incorreto.")

    acertou_chute = False
    rodada_atual = 1

    for rodada_atual in range(1, quantidade_tentativas + 1, 1):
        print('Tentativa {} de {}:'.format(
            rodada_atual,
            quantidade_tentativas
        ))

        msg_digite_numero = 'Digite um número' + \
            f'(Entre {LIMITE_NUMERO_MINIMO} e {LIMITE_NUMERO_MAXIMO}): '
        input_usuario = input(msg_digite_numero)
        chute = int(input_usuario)

        pontos_perdidos_erro = abs(numero_secreto - chute)

        if(chute < LIMITE_NUMERO_MINIMO or chute > LIMITE_NUMERO_MAXIMO):
            print('Valor de entrada inválido.',
                  'Digite um valor de ',
                  f'{LIMITE_NUMERO_MINIMO} a {LIMITE_NUMERO_MAXIMO}.')
            rodada_atual = rodada_atual + 1
            pontuacao = pontuacao - pontos_perdidos_erro
            continue

        acertou_chute = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou_chute):
            print("Você acertou o número secreto.")
            print(f'Pontuação: {pontuacao}')
            break
        elif(chute_maior):
            pontuacao = pontuacao - pontos_perdidos_erro
            print("O chute é maior que o número secreto!")
        elif(chute_menor):
            pontuacao = pontuacao - pontos_perdidos_erro
            print("O chute é menor que o número secreto!")

        rodada_atual = rodada_atual + 1

    if(not acertou_chute):
        print("O número secreto era: {}".format(numero_secreto))
        print("Fim de Jogo!")


if(__name__ == '__main__'):
    jogar()
