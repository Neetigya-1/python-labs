print("Neetigya,24BEE113")
def dollar_to_rupee(dollar):
    return dollar*48
def rupee_to_pound(rupee):
    return rupee/70
def dollar_to_pound(dollar):
    rupee=dollar_to_rupee(dollar)
    pound=rupee_to_pound(rupee)
    return pound
dollar=float(input("Enter amount in dollar: "))
pound=dollar_to_pound(dollar)
print("{}$ is equal to {} euro.".format(dollar,pound))

