print("Neetigya,24BEE113")
def vowels():
    s=input("Enter a sentance: ")
    vow=("A,E,I,O,U,a,e,i,o,u")
    count=0
    for i in s:
        if i in vow:
            count=count+1

    print("Number of vowels in sentance are: ",count)
vowels()
