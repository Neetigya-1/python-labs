print("Neetigya,24BEE113")
def convert_to_bytes(bytes):
    kilo=bytes/1024
    mega=kilo/1024
    giga=mega/1024
    return kilo,mega,giga
bits=float(input("Enter the size in bytes : "))
kilo,mega,giga=convert_to_bytes(bits)
print("{} bytes are equal to : ".format(bits))
print("{} KB".format(kilo))
print("{} MB".format(mega))
print("{} GB".format(giga))
