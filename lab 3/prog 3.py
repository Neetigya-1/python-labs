print("Neetigya,24BEE113")
a = input("Enter the first string : ")
b= input("Enter the second string : ")
isthere=False
for i in a:
   if i in b :
     isthere=True
   
if isthere:
   print("The second string is present in first string")
else:
   print("The second string is not present in first string")
