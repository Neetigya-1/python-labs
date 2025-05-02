print("Neetigya,24BEE113")
a = input("Enter a string : ")
b = len(a)
c=0
d=0
for i in a:
    if('a'<= i <= 'z') or ('A'<= i <='Z'):
        c+=1
    else:
        d+=1
print("The number of alphabets is  : {}".format(c))
print("The number of digits is  : {}".format(d))
