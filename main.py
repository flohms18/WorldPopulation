import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('world_population.csv')

GlobalPopulation = 0
YearCensor = [2022, 2020,2015,2010, 2000, 1990, 1980, 1970]

for j in YearCensor:
    for i in range(len(df)):
        GlobalPopulation += df.loc[i,str(j) + ' Population']
    print(f'GlobalPopulation in {j} is {GlobalPopulation}')