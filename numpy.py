""" 
Simple Linear Regression (Without scikit-learn)

This program calculates the slope and intercept using the
least squares method and predicts the house price for a
given area.

"""
import numpy as np
area = [260,300,320,360,400,426,450]
price = [55000,55600,16000,68000,72500,75500,79000]

# calculate mean
mean_area = np.mean(area)
mean_price = np.mean(price)

# calculate derivation
area_diff = area - mean_area
price_diff = price - mean_price

# Numerator
product = area_diff * price_diff
sum_of_all_product = np.sum(product)

# Denominator
square_of_x1 = np.square(area_diff)
sum_of_all_square_x1 = np.sum(square_of_x1)

# slope
slope = sum_of_all_product // sum_of_all_square_x1 

# Intercept
intercept = mean_price - (slope * mean_area)

# Predicte a price of new area
new_area = int(input("Enter the area: "))
y = slope * new_area + intercept
print("Slope: ",slope)
print("Intercept: ",round(intercept))
print(f"Predicted price for area 450 is : {round(y)}")