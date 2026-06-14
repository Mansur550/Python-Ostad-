counter = 0

while counter < 3:
    print("Hello world")
    counter = counter + 1


num = 12

while True:  # infinite loop
    print(num)
    num = num + 2

    if num > 20:
      break       # stop the loop when condition is met

#Problem Solving
"""
1. 🔒 Mask Sensitive Data (NID/ID)

Hide part of sensitive information.
"""
nid = "1234567890"
masked_nid = nid[:2]+ "*" *6 + nid[8:]
print(masked_nid)  # Output: "12******90"