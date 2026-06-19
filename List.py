mylist= [1,2,3,5,3.5, "Hello", [1,2], (3,4), {"name": "Alice"}, True]
print(mylist)
print(type(mylist))

l1= list(range(1,6)) #list constractor function
print(l1)

print(mylist[8])

fruitlist = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print(fruitlist[-5]) # Accessing first element

print(fruitlist[::2])

print(fruitlist[::-1]) # Reversing the list

fruitlist.append("fig") # Adding an element to the end of the list
print(fruitlist)

# insert with index positon in list
fruitlist.insert(3, "Guava")
print(fruitlist)

#remove last item 
fruitlist.pop()
print(fruitlist)

#remobve item with index position
fruitlist.pop(2)
print(fruitlist)

len(fruitlist) # length of the list
print(len(fruitlist))

# remove_item = "Banana"

fruitlist.remove("Banana") # remove item by value
print(fruitlist)


#add new list to the existing list
new_fruits = ["Honeydew", "Indian Fig"]
fruitlist.extend(new_fruits) # extend method is used to add elements of one list to another list
print(fruitlist)

extra = ["Jackfruit", "Kiwi"]
fruitlist += extra # using + operator to add elements of one list to another list   
print(fruitlist)
