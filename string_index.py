a= "this is a String"
print (a[0])
print(a[4])
print(a[5])

print(len(a))
# len counts the number of characters in the string, including spaces and punctuation.
print(a[len(a)-1])

# Short Cut
print(a[-1])

b="Rahim"
        #-5-4-3-2-1
print(b[-4])

#String is immautable, which means you cannot change the characters in a string after it has been created. You can only create a new string with the desired changes.
# For example, if you want to change the first character of the string "Rahim" to "M", you cannot do it directly. Instead, you can create a new string by concatenating the desired character with the rest of the original string.
b[1]="X"
print(b) # This will raise an error because strings are immutable.