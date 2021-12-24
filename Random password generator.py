import random
Charecters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&*()-=_+*[]}{;':\|.,</>"
Special = '"'
All = Charecters + Special
length = 10
password = "".join(random.sample(All,length))
print("password:",password)