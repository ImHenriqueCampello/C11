#4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e
#colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor
#unidimensional com número par ou ímpar de elementos
import random
import numpy as np

linha = random.randint(0,50)
coluna = random.randint(0,50)

array = np.zeros([linha,coluna])

total_elementos = linha * coluna

if total_elementos % 2 == 0:
    print(f"A matriz {linha}x{coluna} tem {total_elementos} elementos → PAR")
else:
    print(f"A matriz {linha}x{coluna} tem {total_elementos} elementos → ÍMPAR")
