# Loop with sting
word = "Python"

for char in word:
    print(char)


# find the length of the string using for loop
 
count= 0
for char in word:
    count += 1
print("Length of the string:", count)


# Loop nesting

for i in range(1, 4):
    for j in range(1, 3):
        print(f" Outer loop i: {i}, Innar loop j: {j}")

