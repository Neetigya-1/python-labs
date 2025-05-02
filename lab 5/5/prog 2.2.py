print("Neetigya,24BEE113")
list =[]
def sqr(l):
    lit =[]
    sqr=[]
    n = int(input("Enter the range : "))
    for i in range (n):
        lit.append((int(input("Enter the values of the list : "))))
        a=lit[i]
        
        b=a*a
        sqr.append(b)
    print(lit)
    print(sqr)
sqr(list)
