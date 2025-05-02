print("Neetigya,24BEE113")
def area(length,breadth):
    return length*breadth 
def perimeter(length,breadth):
    return (length+breadth)*2 
leng=float(input("Enter the length of rectangle  : "))
brth=float(input("Enter the breadth of rectangle  : "))
area=area(leng,brth)
peri=perimeter(leng,brth)
print("The area of rectangle of length {} is : {}".format(leng,area))
print("The perimeter of rectangle of length {} is : {}".format(leng,peri))
