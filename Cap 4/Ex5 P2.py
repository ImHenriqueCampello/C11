import numpy as np

matriz = np.random.randint(1, 51, size=(4,4))

media_linhas = np.mean(matriz, axis=1)  #linha
media_colunas = np.mean(matriz, axis=0) #coluna

print("Médias das linhas:", media_linhas)
print("Médias das colunas:", media_colunas)

maior_media_linha = np.max(media_linhas)
maior_media_coluna = np.max(media_colunas)

print("Maior média das linhas:", maior_media_linha)
print("Maior média das colunas:", maior_media_coluna)

valores, contagens = np.unique(matriz, return_counts=True)

print("Contagem de cada número:")
for v, c in zip(valores, contagens):
    print(f"Valor {v}: {c} vez(es)")

# Mostrar apenas os que aparecem 2 vezes
print("\nNúmeros que aparecem 2 vezes:", valores[contagens == 2])