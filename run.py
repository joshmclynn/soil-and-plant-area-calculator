SOIL = [50,100,1000]
SOILPRICE = [3.99,10,65]
PLANTSIZE = [1,5,10]
PLANTPRICE = [1.99,2.99,15.99]

def calcsoil():
    print("Please input the length of the area and press enter")
    length = float(input())

    print("Please enter the width of the area and press enter")
    width = float(input())

    print("Please enter the depth of the area and press enter")
    depth = float(input())

    volume = length * width * depth

    return volume

calcsoil()

bulkbag(volume)   

    
def bulkbag(volume):
        bag = SOILPRICE[2]
        total = bag / volume

        print("If you used bulk-bags you would need", total ,"bags")

        









    




