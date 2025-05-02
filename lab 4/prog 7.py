print("Neetigya,24BEE113")
n = int(input("Enter the value of n : "))
r =int(input("Enter the value of r : "))
def nCr(a,b):
    fact =1
    ract=1
    tact=1
    for i in range (1,a+1):
        fact = fact*i
    for j in range (1,b+1):
        ract=ract*j
    for k in range(1,(a-b)+1):
        tact=tact*k
    l = ract *tact
    k=fact//l
    print("The nCr value is {} ".format(k))
nCr(n,r)

def nPr (a,b):
    fact =1
    tact =1
    for i in range (1,a+1):
        fact = fact *i
    for j in range (1,(a-b)+1):
        tact=tact*j
    f = fact//tact
    print("The nPr value is {}".format(f))
nPr(n,r)
