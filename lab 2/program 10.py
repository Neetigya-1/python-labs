lent=int(input("Enter the length: "))
brth=int(input("Enter the breath: "))
area=lent*brth
peri= 2*(lent+brth)
if(area>peri):
    print("area of rectangle is greater than it's perimter")
else:
    print("Perimeter of rectangle is greater than it's area")
    
