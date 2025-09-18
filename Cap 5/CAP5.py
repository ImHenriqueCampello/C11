import pandas as pd

dados = pd.read_csv("paises.csv", delimiter=";")

# 1.a) Quais são os países da OCEANIA;
oceania = dados[dados["Region"].str.contains("OCEANIA", na=False)]
print("Países da Oceania:")
print(oceania["Country"])

# 1.b) Quantos países são da OCEANIA;
qtd_oceania = len(oceania)
print("Quantidade de países da Oceania:", qtd_oceania)

# 2. Encontre o nome e a região do país que possui a maior população segundo este Dataset;
maior_pop = dados.loc[dados["Population"].idxmax(), ["Country", "Region"]]
print("País com maior população:", maior_pop["Country"], "| Região:", maior_pop["Region"])

# 3. Agrupe os países por Regiões. Em seguida, mostre a média de alfabetização (Literacy (%)) de cada região do planeta;
media_alfabet = dados.groupby("Region")["Literacy (%)"].mean()
print("Média de alfabetização por região:")
print(media_alfabet)

# 4. Busque o nome de todos os países do Dataset que não possuem costa marítima e guarde-os em um novo arquivo chamado noCoast.csv;
sem_costa = dados.loc[dados["Coastline (coast/area ratio)"] == 0, "Country"]
print("Países sem costa marítima:")
print(sem_costa)
sem_costa.to_csv("noCoast.csv", index=False)

# 5. Faça uma função que receba a taxa de mortalidade de cada país (Deathrate) e retorne o texto ‘Balanced’ caso o valor seja < 9 e ‘Urgent’ caso contrário. Em seguida, crie um campo no Dataset chamado ‘Humanitarian Help’ que receba estes valores para cada país. No final, mostre o Dataset para verificar se a inserção da nova coluna foi feita com sucesso.
def classificar_taxa(mortalidade):
    return "Balanced" if mortalidade < 9 else "Urgent"

dados["Humanitarian Help"] = dados["Deathrate"].apply(classificar_taxa)
print(dados[["Country", "Deathrate", "Humanitarian Help"]])
dados.to_csv("paises_final.csv", sep=",", index=False)