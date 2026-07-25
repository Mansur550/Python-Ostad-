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

# Solution->
def greet():
    print("Hello Cuastomer!")

def calculate_final_price(price, item):
    tax_rate= 0.25
    total_price = price+ (price*tax_rate)
    greet()
    print(f"Final price of {item} is: ",total_price )

calculate_final_price(1000, "Tv")
calculate_final_price(3500, "Solar Panel")

def greeting(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    return

greeting("Mansur")


# Default Parameter
#A default parameter is a parameter that already has
#a value assigned in the function definition.

# If you don’t provide a value when calling the function,
#  Python uses the default.
def greet_name(name="Guest"):#here Guest is the defult value of name
    print(f"Hello {name}")
    
greet_name("Mansur")
greet_name()

## Machine leaning Use Case

## person -> age, sallary, family_member_count

## data - normalize - 0 - 1 -> fed into ml model
def normalize_data(value, max_value):
    normalized =value/ max_value
    n=f"Original Data: {value} | Normalised: {normalized}"
    print(n)
    return n
result=normalize_data(25,89)
print(result)

# ============================================================
# EXAMPLE: Understanding `print` vs `return`
# Real Use Case: Student Result Processing System
# ============================================================


# -------------------------------
# ❌ Using print (NOT reusable)
# -------------------------------

def calculate_grade_print(marks):
    grade = "A" if marks >= 80 else "B" # logic
    print("Grade:", grade)

# Output is shown, but cannot be reused
result = calculate_grade_print(85)
print("Stored result:", result)

# ❗ Problem:
# - The grade is displayed
# - But it cannot be stored, compared, or sent elsewhere

# ============================================================
# ✅ Using return (Reusable & Powerful)
# ============================================================

def calculate_grade_return(marks):
    grade = "A" if marks >= 80 else "B" # logic
    return grade
result2 = calculate_grade_return(85)
print("Stored result:", result2)
print("Grade:", result2)

# ============================================================
# ✅ Why `return` is important
# ============================================================

# 1️⃣ The returned value can be stored in variables
# 2️⃣ It can be used in conditions
# 3️⃣ It can be passed to another function
# 4️⃣ Essential for real-world software logic
# Example: Decision making using returned value
if result2 == "A":
    print("Eligible for scholarship")
else:
    print("Keep impoving")