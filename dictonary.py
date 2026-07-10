
d={"name" : "Saiham", "age": 25, "city": "Dhaka"} #{key: value}
print(d)

#Dictonary Constrcutor function
x = dict(name="Mansur", age =25, city= "Gazipur")
print(x) 
print(d["age"])
# Dictonary  is mutable
d["work"]= "Ostad"
d["age"]= 35
print(d)

d = {'name': 'Saihan', 'age': 20, 'work': 'Ostad', 'city': 'dhaka', 'phone': 12345}


print(d.get("country", "BD"))


# A dictionary works like a search engine.
# You give a key, and it instantly returns the value.

student_info = {
    "Shovon": {"roll": 123, "city": "Dhaka", "age": 30},
    "Sadia": {"roll": 127, "city": "New York", "age": 29}
}


# A dictionary works like a search engine.
# You give a key, and it instantly returns the value.

student_info = {
    "Shovon": {"roll": 123, "city": "Dhaka", "age": 30},
    "Sadia": {"roll": 127, "city": "New York", "age": 29}
}

# Get full info
print(student_info.get("Shovon"))

# Get nested value safely
shovon_info = student_info.get("Shovon")
print(shovon_info.get("city"))

# Using default value if key does not exist
print(student_info.get("Hasan", "Student not found"))
