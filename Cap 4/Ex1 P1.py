#1. Crie dois NumPy Arrays unidimensionais de tamanho 8: um formado apenas
#por 1’s e outro formado por números aleatórios entre 0 e 9. Some estes dois
#NumPy Arrays e guarde o resultado dentro de um terceiro NumPy Array. Por
#fim, faça o seguinte:
#Se a soma de todos os elementos do Array resultante for >= 40, remodele este
#NumPy Array para se tornar uma matriz com mais linhas do que colunas. Senão,
#remodele para que se torne uma matriz com mais colunas do que linhas.

import numpy as np

array1 = np.ones(8)
array2 = np.random.randint(0, 10, size=8)

array3 = array1 + array2
soma = np.sum(array3)

if soma >= 40:
    # Mais linhas que colunas (ex: 4x2)
    matriz = array3.reshape(4, 2)
else:
    # Mais colunas que linhas (ex: 2x4)
    matriz = array3.reshape(2, 4)

print("Matriz resultante:\n", matriz)