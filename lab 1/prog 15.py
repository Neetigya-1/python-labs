print("Neetigya,24BEE113")
def far_to_cel(far):
    return 5/9*(far-32)
fahr=float(input("Enter temperature in fahrenheit : "))
cel=far_to_cel(fahr)
print("{} degree celcius is equal to {} degree fahrenhiet ".format(cel,fahr))
