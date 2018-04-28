apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2*price for price in apple_prices]
apple_prices_lowered = [price-100 for price in apple_prices]

print(apple_prices_doubled)



first_apples = [x for ind, x in enumerate(apple_prices) if 3 > ind > 0]
print(first_apples)