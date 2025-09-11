import numpy as np
import pandas as pd

#1. Crie duas Series com os seguintes valores:
s1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
s2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

#2. Os valores das Series criadas na Questão 1 representam as fatias de
#mercado (porcentagem) de 3 linguagens de programação populares em
#dois anos consecutivos. Para cada ano, apresente a porcentagem total que
#elas juntas representam no mercado;
print('Total Ano 1:', s1.sum())
print('Total Ano 2:', s2.sum())

#3. Apresente o crescimento/declínio no mercado de cada linguagem do
#primeiro ano para o segundo ano;
print('Crescimento/Declinio:')
print(s2-s1)

#4. Baseado nos resultados da Questão 3, mostre apenas os dados das
#linguagens que tiveram crescimento;
s3 = s2 - s1
print('Crescimento:')
print(s3[s3>0])

#5. Se estas porcentagens de crescimento/declínio se mantivessem iguais
#para os próximos 2 anos, qual seria a linguagem mais popular?
#Dica: use o nlargest(1) no final para retornar rapidamente a label
#e maior valor de uma Series.
largest = s2 + (s3 * 2)
print('Linguaguem mais popular:')
print(largest.nlargest(1))

#6. Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a
#média dos elementos da coluna X que são menores que 30;
np.random.seed(10)

df = pd.DataFrame(
    data=np.random.randint(1, 50, [5, 4]),
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z']
)

var = df['X']
print('Media de elementos menor que 30:')
print(var[var < 30].mean())

#7. Utilizando do mesmo DataFrame, apresente a média dos elementos da
#linha D usando a função loc() como base e a soma dos elementos da linha E
#usando a função iloc() como base;
aux = df.loc['D', :].mean()
aux2 = df.iloc[4, :].sum()

print('Média da linha D:', aux)
print('Soma da linha E:', aux2)

#8. Faça um Slicing na matriz mostrando apenas as linhas A, C e E
#juntamente com as colunas X e Y. Em seguida, mostre qual seria a soma dos
#elementos de cada uma destas linhas e cada uma destas colunas.
slic = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print('Soma de cada linha:', slic.sum(axis=1))
print('Soma de cada coluna:', slic.sum(axis=0))