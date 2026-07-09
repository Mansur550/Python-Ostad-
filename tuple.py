t =(1,2,3,4,45)

print(t)
print(type(t))

T= tuple(range(1,20))
print(T)
l= [10,20,30]
print(type(l))
L= tuple(l)
print(type(t))

#tuple
x=(1,2,3,4,5,6)
print(x.count(4))  #Number of 4
print(x.index(5)) #gives the position of 5

# tuple unpacking

# y= (1,3,4,"hello", "hi")
# a, b, c, d,e =y

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

Y= (1,3,"hello", "hi")
A, B, *C =Y
print(A)
print(B)
print(C)

