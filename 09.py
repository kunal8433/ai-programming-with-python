import pandas as pd

# We create a dictionary of Pandas Series 
items = {'Alice': pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants']),
         'Bob': pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch'])}

# We print the type of items to see that it is a dictionary
print(type(items))
# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
print(shopping_carts)

print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:\n', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)