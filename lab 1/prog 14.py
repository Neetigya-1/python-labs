print("Neetigya,24BEE113")
def celcius_to_fer(celcius):
    return (9/2*celcius)+32
celcius=float(input("Enter temperature in Celsius: "))
fahr=celcius_to_fer(celcius)
print("{} degree Celsius is equal to {} degree farrenheit".format(celcius,fahr))
              
