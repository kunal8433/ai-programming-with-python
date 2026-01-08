import pandas as pd
grocereries = pd.Series(data=[30,20,10,"yes", "no"],  index = ["apples", "bananas", "oranges", "milk", "bread"])
print(grocereries)
print(grocereries.dtype)
print(grocereries.size)
print(grocereries.ndim)
print(grocereries.index)
print(grocereries.values)
print("apples" in grocereries)