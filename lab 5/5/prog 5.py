print("Neetigya,24BEE113")
def fact():
    l=[]
    n=int(input("Enter the range : "))
    for i in range(n):
        l.append((int(input("Enter the value of the list : "))))
    for a in l :
        fact=1
        for j in range(1,a+1):
            fact=fact*j
        print("The factorial of numbers {} are {}".format(a,fact))
fact()
