# 🏷️ Keyword Arguments

# Explicitly specify parameter names — order does not matter.

# These features make functions easier to use and harder to misuse.

def calculate_price(price, tax):
    total = price+ price*tax
    print(f"Total:{total}")
    return total
calculate_price(3000, 0.15)   # right argument order
# postion matters -> positional arguments
calculate_price(0.15, 3000)  # wrong argument order-> 0.15 (tax_rate) should be the 2nd argument