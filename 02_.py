import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pokemon = pd.read_csv(r'D:\Matpotlib\pokemon.csv')

sb.countplot(data=pokemon, x='generation_id')
plt.show()
