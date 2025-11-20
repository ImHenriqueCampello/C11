import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

air = pd.read_csv('airtravel.csv')
co2 = pd.read_csv('co2_emissions.csv')

air['Date'] = pd.to_datetime(air['Date'])
air.set_index('Date', inplace=True)

co2['Date'] = pd.to_datetime(co2['Year'].astype(str) + '-01-01')
co2.set_index('Date', inplace=True)

plt.figure(figsize=(10,4))
plt.plot(air['Passengers'])
plt.title("Air Travel Passengers")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(co2['CO2_Emissions'])
plt.title("CO2 Emissions (Annual)")
plt.show()

# Airtravel
air_dec = seasonal_decompose(air['Passengers'], model='multiplicative', period=12)
air_dec.plot()
plt.show()

#c02
co2_dec = seasonal_decompose(co2['CO2_Emissions'], model='additive', period=1)
co2_dec.plot()
plt.show()


#RESPOSTAS

#Airtravel
# a. A série possui tendência?
#    Sim, a tendência é crescente ao longo dos anos

# b. A série possui sazonalidade?
#    Sim, sazonalidade mensal com período = 12

# c. A série possui ciclo?
#    Sim, há oscilações de longo prazo além da sazonalidade, indicando ciclos associados ao crescimento estrutural da aviação



#CO2
# a. A série possui tendência?
#    Sim, a tendência geral decrescente

# b. A série possui sazonalidade?
#    Não, Os dados são anuais não há repetição sazonal detectável

# c. A série possui ciclo?
#    Existe um ciclo lento de longo prazo associado a mudanças econômicas e ambientais, mas não é sazonal
