import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world_population.csv')

GlobalWorldPopulation2022 = 0
for i in range(len(df)):
    GlobalWorldPopulation2022 += df.loc[i, '2022 Population']
print(GlobalWorldPopulation2022)
