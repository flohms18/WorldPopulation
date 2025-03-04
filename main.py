import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world_population.csv')

GlobalWorldPopulation2022 = 0
GlobalWorldPopulation2022 += df['2022 Population'].mean()
print(GlobalWorldPopulation2022)
