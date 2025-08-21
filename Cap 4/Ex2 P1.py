#2. Crie dois NumPy Arrays unidimensionais: um de números pares de 0 à 51 e
#outro também de números pares de 100 até 50. Em seguida, os concatene e
#mostre os resultados ordenados

import numpy as np
array1 = np.arange(0, 52, 2)
array2 = np.arange(0, 101, 2)

array = np.concatenate((array1, array1))
ordenado = np.sort(array)

print("Resultado:\n", ordenado)
