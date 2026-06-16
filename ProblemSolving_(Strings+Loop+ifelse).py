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