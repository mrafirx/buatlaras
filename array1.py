# def apply_discount(prices):
#     discounted_prices = [price * 0.9 for price in prices]
#     return discounted_prices

# # Example usage
# item_prices = [50, 30, 20, 10, 5]
# discounted_prices = apply_discount(item_prices)

# print("Original Prices:", item_prices)
# print("Discounted Prices:", discounted_prices)

print("-------------------------------------------")

# Create an array of item prices
item_prices = [50, 30, 20, 10, 5]

# Apply a 10% discount and create a new array
discounted_prices = [int(price * 0.9) for price in item_prices]

# Print the original and discounted prices
print("Original Prices:", item_prices)
print("Discounted Prices:", discounted_prices)

print(item_prices[0])
print(discounted_prices[1])