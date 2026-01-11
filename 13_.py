import pandas as pd
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]
items = pd.DataFrame(items2, index = ["store1", "store2"])
print(items)
items ['kunal'] = [12, 23] 
print(items)
# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
items['shirts'] = [15, 2]
print(items)
# We display the modified DataFrame
print(items)
items['jaat'] = [23,23]
print(items)
items.loc['store3'] = {
    'bikes': 25,
    'pants': 40,
    'watches': 20,
    'glasses': 10,
    'kunal': 18,
    'shirts': 30,
    'jaat': 22
}
print(items)