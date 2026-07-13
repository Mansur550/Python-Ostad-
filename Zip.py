user_id=["1", "2","3"]
user_name= ["Mansur", "Dristy", "Tahsin"]
user_mails= ["mansur@gmail.com", "dristy@gmail.com", "tahsin@gmail.com"]
user_age= [22,20,21]

for info in zip(user_id, user_name, user_mails, user_age):
    print(info)