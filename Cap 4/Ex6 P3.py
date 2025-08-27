#Baseado nos comandos que vimos até o momento e no Dataset fornecido,
#crie scripts em Python que respondam às seguintes perguntas:

import numpy as np

# carregar dataset
dataset = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# ignorar cabeçalho
dados = dataset[1:]

#1.Apresente a porcentagem de missões que deram certo
status = dados[:, 7]
total = len(status)
sucessos = np.sum(status == "Success")
percentual = (sucessos / total) * 100
print("1)", round(percentual, 2), "% das missões deram certo")

#2.Qual a media de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (> 0)?
gastos = dados[:, 6].astype(float)
media = gastos[gastos > 0].mean()
print("2) Média de gastos: ", round(media, 2))

#3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (EUA)
paises = dados[:, 2]
missoes_usa = np.sum(np.char.count(paises, "USA") > 0)
print("3) Missões dos EUA: ", missoes_usa)

#4. Encontre qual foi a missão mais cara realizada pela empresas “SpaceX”
nome = dados[:, 1].astype(str)
indices_spacex = np.where(nome == "SpaceX")[0]
maiscaro = indices_spacex[np.argmax(gastos[indices_spacex])]
missao = dados[maiscaro, 4]
print("Missão mais cara da SpaceX:", missao)


#5. Mostre o nome das empresas que já realizaram missões espaciais,
#juntamente com suas respectivas quantidades de missões (use o for
#no final para mostrar as informações)
empresas = dados[:, 1]
nomes, contagens = np.unique(empresas, return_counts=True)
print("5) Empresas e quantidades:")
for i in range(len(nomes)):
    print(nomes[i], contagens[i])
