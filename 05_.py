import pandas as pd

distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]

planets = ['Earth','Saturn', 'Venus', 'Mars', 'Jupiter']

dist_planets = pd.Series(data = distance_from_sun, index = planets)

time_light = dist_planets / 18

close_planets = time_light[time_light < 40]

print(time_light)
print(close_planets)