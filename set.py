#set is unorderd collection of element

s={2,3,2,True, "hello",(1,3)} 
print(s) #no duplicate item is set
s.add(7)
print(s)
s.remove(3)
print(s)

old_subscriber = {"rafin@gmail.com", "shafin@gmail.com", "sadia@gmail.com", "hasan@gmail.com"}
new_subscriber = {"sadia@gmail.com", "hasan@gmail.com", "sayem@gmail.com", "adnan@gmail.com"}
# Total unique subscribers
total_unique = old_subscriber.union(new_subscriber)
print("Total Unique Subscribers:", total_unique)

# Users who shifted to new channel (common subscribers)
shifted_users = old_subscriber.intersection(new_subscriber)
print("Users shifted to new channel:", shifted_users)

# Users who stayed only in old channel
only_old = old_subscriber.difference(new_subscriber)
print("Only in old channel:", only_old)