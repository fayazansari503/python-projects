import random 
import string

pass_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charvalues)

print("your random password is", password)

#password = "".join([random.choice(charvalues) for i in range(pass_len)])   
#print("your random password is", password)            