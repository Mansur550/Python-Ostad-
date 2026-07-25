# Scenario: An e-commerce system needs to calculate final price of products
# Case 1
# price = 1000       # oven
# tax_rate = 0.25    # 25%
# total_price = price + (price * tax_rate)   # logic / calcultion -> final price
# print("Final Price:", total_price)

# Case 2 (same logic repeated)
# price = 2000     # tv
# tax_rate = 0.25
# total_price = price + (price * tax_rate) # logic / calcultion -> final price
# print("Final Price:", total_price)

# ❗ Problem:
# - Code duplication
# - Hard to maintain
# - If tax rate changes, you must update everywhere