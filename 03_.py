import pandas as pd
data = {"name": ["kunalmalik", "lucky malik"] , "marks":[98,99]}
df = pd.DataFrame(data)
print(df)
x  =  df.isnull()
print(x)
y = df.isnull().sum().sum()
print(y)