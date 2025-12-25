class Shirt:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

shirt_one  = Shirt('red','M','long sleeved',45)
shirt_two  = Shirt('orange','S','short sleeved',30)
print(shirt_one.price)
print(shirt_one.color)
shirt_two.change_price(45)
print(shirt_two.price)
shirt_one.color = 'yellow'
shirt_one.size = 'L'
shirt_one.price = 38 
print(shirt_one.color)
print(shirt_one.size)   
print(shirt_one.price)