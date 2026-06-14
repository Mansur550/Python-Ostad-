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