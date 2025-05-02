print("Neetigya,24BEE113")
l=["tina","maya","dhara",("neetigya","pulkit","Rushi"),"kritika"]
a=len(l)
c=0
d=0
for i in l:
    if isinstance(i,tuple):
        c+=len(i)
    else:
        d+=1
print("the Number of Boys are : {}".format(c))
print(f"The number of girls are : {d}")
