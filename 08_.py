import pandas as pd
items = {"kunal" :pd.Series([10,20,30,40], index = ["book", "pen", "notebook", "bag"]),
         "lucky": pd.Series ([15,25,35,45], index = ["book", "pen", "notebook", "bag"]),}
print(type(items))
df = pd.DataFrame(items)
print(df)

print(items.values)
data = {'Alice': pd.Series([40, 110, 500, 45]),
        'Bob': pd.Series([245, 25, 55])}

df = pd.DataFrame(data)
print(df)
