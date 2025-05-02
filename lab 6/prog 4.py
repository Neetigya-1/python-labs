print("Neetigya,24BEE113")
list =[("maggi" ,300) , ("dabeli" , 30) ,("vadapav" ,40) ,("dohkla" ,350)]
sortedlist=[]

while list:
    maxprice=list[0]
    for i in list:
        if(i[1]>maxprice[1]):
            maxprice=i
    sortedlist.append(maxprice)
    list.remove(maxprice)
for i in sortedlist:
    print(i)
