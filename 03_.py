import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pokemon = pd.read_csv(r'D:\Matpotlib\pokemon.csv')

print(pokemon.head())
print(pokemon.shape)

sb.countplot(data=pokemon, x='generation_id')
plt.title("Pokémon Count per Generation")
plt.xlabel("Generation")
plt.ylabel("Count")
plt.show()
