# Simple Project: Shopping Cart Total Calculator
# 🎯 Goal:

# Build a simple program that stores item prices in a list and calculates the final bill.

# 💻 Problem Statement:

# Write a program that:

# Takes prices of items one by one
# Stores them in a list
# Calculates:
# Total bill
# Number of items
# Average price per item
# Prints a bill summary

prices =[]
# Step 1: Take input using loop
n = int(input (" How many items you want to buy ?"))

for i in range(n):
    price = float(input(f"Enter the price of item {i+1}: "))
    prices.append(price)


# Step 2: Calculate total using loop
total = 0

for p in prices:
   total += p

# Step 3: Calculate number of items
average = total/ n

# Step 4: Display bill
print("\n--- Shopping Bill ---")
print("Items:", prices)
print("Total Items:", n)
print("Total Bill:", total)
print("Average Price:", average)