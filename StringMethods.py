text = " hello world "
print(text.upper())  # Output: "HELLO WORLD"
print(text.lower()) # Output: "hello world"
print(text.title())  
print(text.strip())  # Output: "hello world"
print(text.replace(" ", "_"))  # Output: "_hello_world_"



text2 = "Hello World"
print(text2.replace("World", "Bangladesh"))
print(len(text2))
print(text2)
print(text2.startswith("Hello"))  # Output: True
print(text2.endswith("World"))    # Output: True
print(text2.split())  # Output: ['Hello', 'World']


sentence ="python programming is fun"
print(sentence.count("o")) # Output: 2 (counts occurrences of 'o')
print(sentence.find("gram"))  # Output: 10 (finds position of substring)
print(sentence.split()) 


# Chaining mulltiple methods
text3 = " Java progRaMming  "
result =text3.strip().replace("java", "Python").upper().title()
print(result)


# String Indexing
name = "Mansur"
print(name[0])  # Output: 'M'
print(name[1])  # Output: 'a'
print(name[-1]) # Output: 'r'


# String Slicing
print(name[0:3])  # Output: 'Man'
print(name[:4])  # Output: 'Mans' starts from index 0 to 3 (excluding index 4)
print(name[2:])   # Output: 'nsur' starts from index 2 to the end of the string

print(name[::-1])  # Output: 'rusnaM' reverses the string
print(name[::2])  # Output: 'Mnsr' takes every second character starting from index 0



