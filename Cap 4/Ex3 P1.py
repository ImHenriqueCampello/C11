#3. Mini Campo Minado
#a)Crie um NumPy Array 2x2 formado apenas por 0’s
#b)Em seguida, adicione um número 1 em uma posição aleatória desta matriz;
#c)Faça uma entrada de dados para solicitar o usuário que faça uma jogada (selecione uma posição da matriz)
#I.Se ele selecionar todas as posições em que o número 1 não se encontra, mostre a
#mensagem “Congratulations! You beat the game! :)”
#II.Senão, se dentro das 3 primeiras jogadas ele achar o número 1, mostre a mensagem “Game Over! :( Try Again!”
import random as ran
import numpy as np

tentativas = 0
perdeu = False
arr = np.zeros([2,2])

linha = ran.randint(0,1)
coluna = ran.randint(0,1)

arr[linha,coluna] = 1

while tentativas < 3 and not perdeu:
    tentativas += 1
    print(f"\nTentativa {tentativas}:")

    l = int(input("Digite a linha: "))
    c = int(input("Digite a coluna: "))

    if arr[l, c] == 1:
        print("Game Over! :( Try Again!")
        perdeu = True
    else:
        print("Parabéns!")

if not perdeu:
    print("Congratulations! You beat the game! :)")


