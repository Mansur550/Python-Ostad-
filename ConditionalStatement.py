age =9
if age<13:
    print("You are an adult.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult")


# Nested COnditions
age =18
hasLicense = False

if age >=18:
    if hasLicense:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")


# Aulternative (And Operator)
age = 18
has_license = False

if age >= 18 and has_license:
    print("You need a license to drive cars")
else:
    print("You are too young or you don't have a license")


# Example-2
temperature = 8
is_sunny = True

if temperature > 15:
    print("The weather is warm enough. Let's go out.")
else:
    if is_sunny:
        print("It's cold, but sunny. Let's go out.")
    else:
        print("It's cold and not sunny, so it's risky to go outside.")


# This nested condition clearly explains why going outside is risky.
# The above code can be converted using or operator.

temp= 7
is_sunny = True

if  temp >15 or is_sunny:
    print("Let's go out.")
else:
    print("It's cold and not sunny, so it's risky to go outside.")