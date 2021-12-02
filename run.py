SOIL = [50,100,850]
SOILPRICE = [3.99,10,65]
PLANTSIZE = [1,5,10]
PLANTPRICE = [1.99,2.99,15.99]

volume = 0

def calcarea():
    print("Please input the length of the area and press enter")
    length = float(input())

    print("Please enter the width of the area and press enter")
    width = float(input())

    print("Please enter the depth of the area and press enter")
    depth = float(input())

    global volume 
    mcubes = (length * width * depth)
    volume = (mcubes * 1000)
    print("The volume you have is" ,volume)
    whatsoil()

    return volume
    


def whatsoil():
    print("What size bag would you like to order")
    print("""
                ------1 = BULK-BAG ------
                ------2 = 100L BAG ------
                ------3 = 50L BAG  ------
                
        """)
    answer = input("")
    if answer== "1":
        bulkbag(volume)
    elif answer== "2":
        hundredbag(volume)
    elif answer== "3":
        fiftybag(volume)
       
    

def bulkbag(volume):
    bag = SOIL[2]
    total = volume / bag

    print("If you used bulk-bags you would need", total ,"bags")

    if total<1 :
        print("As you have less than one bulk-bag I would suggest ordering smaller bags")
        print("If you would like to order a smaller bag press 1")
            
            
        if input()== "1":
            hundredbag(volume)
                       

    

def hundredbag(volume):
        bag = SOIL[1]
        total = volume / bag

        if total % 50 == 0 :
            print("You could have this order in smaller bags")
            print("If you would like to order a smaller sized bag press 1")
            if input()== 1:
                fiftybag(volume)

        print("If you used 100L bags you would need", total ,"bags")
    

def fiftybag(volume):
        bag = SOIL[0]
        total = volume / bag

        print("If you used 50L bags you would need", total ,"bags")
    


calcarea()
    









    




