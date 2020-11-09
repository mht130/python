import random
import sys
import string

try:
    lenght=sys.argv[1]
except:
    print("usage : python password_generator.py [lengh]")

chars=string.ascii_letters+string.digits

output=''
counter=0
while counter<int(lenght):
    output+=chars[random.randint(0,61)]
    counter+=1
print(output)
