print("Neetigya,24BEE113")
def rupee_to_dollar(rupee):
    return rupee/48
rupee=float(input("Enter the amount of rupee: "))
dollar=rupee_to_dollar(rupee)
print("{}rupees are equal to {}$. ".format(rupee,dollar))
