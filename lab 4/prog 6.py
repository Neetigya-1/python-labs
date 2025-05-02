print("Neetigya,24BEE113")
def days():
    for hour in range(24):  
        if hour == 0:
            print("12:00 AM - Midnight")
        elif hour < 12:
            print("{}:00 AM".format(hour))
        elif hour == 12:
            print("12:00 PM - Noon")
        else:
            print("{}:00 PM".format(hour-12))
days()
