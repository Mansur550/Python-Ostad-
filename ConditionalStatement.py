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