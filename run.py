import random
import re
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('plant_shop')
ORDERS = SHEET.worksheet('orders')

SOIL = [50,100,2831]
SOILPRICE = [3.99,10,65]
PLANTSIZE = [1,5,10]
PLANTPRICE = [1.99,2.99,15.99]
enter_input = "Enter your input here:"
volume = 0
answer = ""
pricedue = 0
ordernumber = 0
num_invalid ="Please only enter numbers"


def calcarea():
    correctinput = r"^[.0-9]+$"
    while True:
        
        print("Please input the length of the area(in M and CM) and press enter")
        length = input(enter_input)
        true = re.match(correctinput,length)
        if true:
            int(float(length))
            break
            
        else:
            print(num_invalid)
        

        
    while True:
        print("Please enter the width of the area(in M and CM) and press enter")
        width = input(enter_input)
        true = re.match(correctinput,width)
        if true:
            int(float(width))
            break
        else:
            print(num_invalid)
    while True:
        print("Please enter the depth of the area(in M and CM) and press enter")
        depth = input(enter_input)
        true = re.match(correctinput, depth)
        if true: 
            
            break
        else:
            print(num_invalid)
    length = int(float(length))
    
    width = int(float(width))
    
    depth = int(float(depth))
            
    global volume 
    mcubes = (length * width * depth)
    volume = (mcubes * 1000)
    print("The total volume you have is" ,volume,"in litres")
    whatsoil()

    return volume
    
        
def whatsoil():
    print("What size bag would you like to order")
    print("""
                ------1 = BULK-BAG/PRICE £65 ------
                ------2 = 100L BAG/PRICE £10 ------
                ------3 = 50L BAG £3.99 ------
                
        """)
    global answer
    answer = input(enter_input)
    if answer== "1":
        bulkbag(volume)
    elif answer== "2":
        hundredbag(volume)
    elif answer== "3":
        fiftybag(volume)
        
    

def bulkbag(volume):
    bag = SOIL[2]
    global total
    total = volume / bag
    print("If you used bulk-bags you would need", total ,"bags")
    print("Press 1 to proceed to payment")
    print("Press 2 to return to the menu")
    while True:
        bulkbagansw = input(enter_input)
        if bulkbagansw == "1":
            payment()
            break
        elif bulkbagansw == "2":
            main()
            break
        else:
            print("Incorrect input please choose between 1 and 2")
        
              
           
def hundredbag(volume):
        bag = SOIL[1]
        global total
        total = volume / bag

        print("If you used 100L bags you would need", total ,"bags")

        
        print("If you would like to order a smaller bag press 1 or 2 to continue with your order")
        print("Or to return to the menu press 3")
        while True:
            hundbag = input(enter_input)
            if hundbag == "1":
                fiftybag(volume)
            elif hundbag == "2":
                payment()
            elif hundbag == "3":
                main()
            else:
                print("Please choose between 1 and 3")
    

def fiftybag(volume):
        bag = SOIL[0]
        global total
        total = volume / bag
        print("If you used 50L bags you would need", total ,"bags")
        print("To continue to payment please press 1")
        print("To return to the menu press 2")
        while True:
            fifbag = input(enter_input)
        
            if fifbag == "1":
                payment()
            elif fifbag == "2":
                main()
            else:
                print("Please choose either 1 or 2")




    
def payment():
    if answer =="1":
        pricedue = round(total * SOILPRICE[2],2)
        
    elif answer =="2":
        pricedue = round(total * SOILPRICE[1],2)
        
    elif answer =="3":
        pricedue = round(total * SOILPRICE[0],2)
    
    
    print("Your total is : £",pricedue)
    print("To pay please press 1")
    print("Press m to return to the main menu")
    while True:
        payans = input(enter_input)
        
        if payans == "1":
            print("Please enter your card number")
            cardno = input(enter_input)
            orderno = random.randint(1, 1000)
            row = [orderno,cardno,pricedue]
            ORDERS.append_row(row)
            print("Your order number is",orderno,"you can use it to cancel your order")
            print("Enter m to return to the main menu")
        if  payans == "m":
            main()
            break
        else:
            print("To return to the menu press m!")
    

        
        



def cancelorder():
    print("Please enter your order number")
    while True:
        userorder = input(enter_input)
        currentorders = [o for o in ORDERS.col_values(1)]
        if userorder in currentorders:
            order = ORDERS.row_values(ORDERS.find(userorder).row)
            ordernum = order[0]
            ordercred = order[1]
            orderamount = order[2]
            break
        if userorder == "r":
                main()
        else:
            print("Incorrect order number please re-enter your order number or enter r to return to menu")
            
    print("Your order is ","ORDER-NUMBER:",ordernum,"CARD-NUM:",ordercred,"ORDER-PRICE:£",orderamount,"are you sure you want to cancel it?")
    print("If you wish to continue with cancelling your order please press 1")
    print("If you no longer wish to cancel it, press 2")
    while True:
        cancel_input = input(enter_input)
        if cancel_input == "1":
            ORDERS.delete_rows(ORDERS.find(userorder).row)
            print("order",userorder,"has now been cancelled")
            main()
            break
        elif cancel_input == "2":
            main()
            break
        else:
            ("Please either press 1 or 2")
    


def main():
    print("""
    
                        𝕊𝕠𝕚𝕝 𝕒𝕟𝕕 𝕡𝕝𝕒𝕟𝕥 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣  
                                                                                                                                                         """)
    print("""                                     
            ------------ 1. Soil Calculator and Purchase            ----------
            ------------ 2. Plant Calculator and Purchase           ----------
            ------------ 3. Cancel an Order using your order number ----------
            ----        Enter the corresponding number to access your     ----
            ------------            selection (1 - 3)               ----------
                """)
    global choice
    while True:
        choice = input(enter_input)
        if choice == "1":
            calcarea()
            break
        elif choice == "2":
            plantcalc()
            break
        elif choice == "3":
            cancelorder()
            break
        else:
            print("Please choose between 1-3")

main()