import pandas as pd
items = {"kunal" :pd.Series([10,20,30,40], index = ["book", "pen", "notebook", "bag"]),
         "lucky": pd.Series ([15,25,35,45], index = ["book", "pen", "notebook", "bag"]),}
print(type(items))
df = pd.DataFrame(items)
print(df)