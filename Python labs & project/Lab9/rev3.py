import numpy as np
# Input Inventory Array
inventory = np.array([10, 0, 5, 0, 20, 0])
# Determine the out of stock products
out_of_stock = inventory[inventory == 0]
print("Out of Stock Products:", out_of_stock)
