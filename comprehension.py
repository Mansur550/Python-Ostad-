# Comprehensions in Python provide a concise, readable, and efficient 
# way to create new data structures from existing iterables

numbers =[1,4,6,8]
squared_numbers = [] 
for num in numbers:
    squared_numbers.append(num**2)
#print squared number
print(squared_numbers)
# Comprehensions
sq_num= [num**2 for num in numbers]
print(sq_num) 



#Comprehension for dictonary
price ={"Rice": 60, "Suger": 100, "Salt": 80}

# discount_price= {}
# for item , price in price.items():
#    discount_price.update({item: price*0.9})
# print(f"After discount: {discount_price}")

discount_price= {item:price*0.9 for item , price in price.items()}
print(f"After discount: {discount_price}")


#Even number
numbers = list(range(1,21))

even_numbers= []

for num in numbers:
    if num %2==0:
        even_numbers.append(num)

print(even_numbers)
      