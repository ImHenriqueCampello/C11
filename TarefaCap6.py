import pandas as pd
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", delimiter=";")
space = pd.read_csv("space.csv", delimiter=";")

paises_na = paises[paises["Region"].str.contains("AMERICA", case=False, na=False)]
x = paises_na["Country"]
y1 = paises_na["Deathrate"]
y2 = paises_na["Birthrate"]
plt.plot(x, y1, "r-", label="Deathrate")
plt.plot(x, y2, "b-", label="Birthrate")
plt.xticks(rotation=45)
plt.legend()
plt.show()

empresas = space[space["Location"].str.contains("USA|China")]
empresas_unicas = empresas.drop_duplicates(subset=["Company Name"])
contagem_usa = empresas_unicas["Location"].str.contains("USA").sum()
contagem_china = empresas_unicas["Location"].str.contains("China").sum()
plt.bar(["USA", "China"], [contagem_usa, contagem_china], color="green")
plt.show()

roscosmos = space[space["Company Name"] == "Roscosmos"]
sucesso = (roscosmos["Status Mission"] == "Success").sum()
fracasso = (roscosmos["Status Mission"] != "Success").sum()
plt.pie([sucesso, fracasso], labels=["Sucesso", "Fracasso"], autopct="%1.1f%%")
plt.show()