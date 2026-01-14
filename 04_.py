import pandas as pd
data = {"name": ["kunalmalik", "lucky malik"] , "marks":[98,99]}

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.shape)
print(df.isnull())