print("Neetigya,24BEE113")
def intrest(principal,rate,time):
    return (principal*rate*time)/100
princ=float(input("Enter the principal amount : "))
rate=float(input("Enter the rate of interest : "))
time=float(input("Enter the time period in years :"))
interest=intrest(princ,rate,time)
print("The interest for a principal amount of {} at rate of {}% for {} years is : {}".format(princ,rate,time,interest))
    
