import pandas as pd
grocereries = pd.Series(data=[30,20,10,"yes", "no"],  index = ["apples", "bananas", "oranges", "milk", "bread"])
print(grocereries)
print(grocereries["milk"])