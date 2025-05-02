print("Neetigya,24BEE113")
list = [("24BEE113","Hello",18),("24BEE092","Hi",20),("24BEE095","Bye",19)]
rollnum =[]
age=[]
name=[]
for i in list:
    rollnum.append(i[0])
    age.append(i[2])
    name.append(i[1])
print(f"Roll number : {rollnum}")
print(f"Name : {name}")
print(f"Age:{age}")
