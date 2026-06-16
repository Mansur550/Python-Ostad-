"""
1. 🔒 Mask Sensitive Data (NID/ID)

Hide part of sensitive information.
"""

nid = "1234567890"

masked = nid[:2] + "*" * 6 + nid[8:]
print(masked)


"""
2. 📞 Extract Country Code from Phone Number
"""
phone = "+880 1234 567890"
country_code= phone.split()[0] if " " in phone else phone[:4]
print(country_code)  # Output: "+880"

"""
3. 🔁 Palindrome Check

A string that reads the same forward and backward.

- racecar
- dad
- level
"""
text = "madam"

reversed_text = text[::-1]

if text == reversed_text:
    print(f"{text} is a palindrome.") 
else:
    print(f"{text} is not a palindrome.")

"""
4. 🔤 Anagram Check

Two strings with same characters in different order.

- Act / Cat
- Below / Elbow
- Cinema / Iceman
- Fried / Fired
- Lemon / Melon
"""
a="Act"
b="Cat"

if sorted(a.lower())== sorted(b.lower()):
    print(f"{a} and {b} are anagrams.")
else:   
    print(f"{a} and {b} are not anagrams.")

"""
5. 📄 Application Log Data Parsing

Used to extract useful info from raw logs (timestamps, errors, user actions).
"""

log = "2026-04-11 ERROR User login failed"

parts = log.split()
timestamp = parts[0]
level = parts[1]
message = "".join(parts[2:])

print(timestamp)
print(level)
print(message)

"""
6. 🎓 Grade Evaluator
"""
marks=88

if marks >=80 and marks <=100:
    print("A+")
elif marks >=70 and marks <80:
    print("A")
elif marks >=60 and marks <70:
    print("A-") 
else:
    print("Invalid marks")