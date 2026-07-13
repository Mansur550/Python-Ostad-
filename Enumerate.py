fruits=["Apple", "Banana", "Mango"]

for item in fruits:
    print(item) 

#Alt
for idx in range(len(fruits)):
    print(idx+1, fruits[idx])
#Enumerate:
print(list(enumerate(fruits)))

for idx in enumerate(fruits, start=10):
    print(idx, item)