import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world_population.csv')

Year = ['2022 Population','2020 Population','2015 Population']

df.plot(kind='bar',x='Continent',y='2022 Population',legend=False)

plt.show()