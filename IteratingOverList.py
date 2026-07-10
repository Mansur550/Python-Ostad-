fruits = ["Apple", "Banana", "Mango"]

for item in fruits:
    print (f"Processing {item}")



fruit = ["Apple", "Banana", "Mango"]

for item in fruit:
    print (f"Processing {item}")


fruitz = {"Apple", "Banana", "Mango"}

for item in fruitz:
    print (f"Processing {item}")



users = {"001", "002", "003"}

for id in users:
    print(f"processing {id}")


#Dictonary

students = {"sadiya": 25, "Abir": 30, "Alvi": 32}
print(students)

for item in students:
    print(item) #print only key

# Another way to print keys
for item in students.keys():
    print(item) 

#print values

for item in students.values():
    print(item)
