import random


print('#======================================#')
print("#  Bem vindo ao jogo de Adivinhação!   #")
print('#======================================#')

LIMITE_NUMERO_MINIMO = 1
LIMITE_NUMERO_MAXIMO = 100

numero_secreto = random.randint(LIMITE_NUMERO_MINIMO, LIMITE_NUMERO_MAXIMO)

quantidade_tentativas = 3
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

    if(chute < LIMITE_NUMERO_MINIMO or chute > LIMITE_NUMERO_MAXIMO):
        print('Valor de entrada inválido.',
              'Digite um valor de ',
              f'{LIMITE_NUMERO_MINIMO} a {LIMITE_NUMERO_MAXIMO}.')
        rodada_atual = rodada_atual + 1
        continue

    acertou_chute = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(acertou_chute):
        print("Você acertou o número secreto.")
        break
    elif(chute_maior):
        print("O chute é maior que o número secreto!")
    elif(chute_menor):
        print("O chute é menor que o número secreto!")

    rodada_atual = rodada_atual + 1

if(not acertou_chute):
    print("O número secreto era: {}".format(numero_secreto))
    print("Fim de Jogo!")
