import random
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

volume = 0
answer = ""
pricedue = 0
ordernumber = 0


def calcarea():
    print("Please input the length of the area and press enter")
    length = float(input())

    print("Please enter the width of the area and press enter")
    width = float(input("Enter the width here:"))

    print("Please enter the depth of the area and press enter")
    depth = float(input("Enter the length here:"))

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
    global answer
    answer = input("Enter your input here:")
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
    print("Press 2 to proceed to payment")
    if input() == "2":
        
        payment()
    if total<1 :
        print("As you have less than one bulk-bag I would suggest ordering smaller bags")
        print("If you would like to order a smaller bag press 1 or 2 to continue with your order")
        print("To return to the main menu enter 3")    
            
        if input()== "1":
            hundredbag(volume)
        elif input()== "2":
            payment()
        elif intput()=="3":
            menu()
           

    
def hundredbag(volume):
        bag = SOIL[1]
        global total
        total = volume / bag

        print("If you used 100L bags you would need", total ,"bags")

        
        print("If you would like to order a smaller bag press 1 or 2 to continue with your order")
        hundbag = input("")
        if hundbag == "1":
                fiftybag(volume)
        elif hundbag == "2":
                payment()
        else:
            print("Please enter either 1 or 2") 
        
    

def fiftybag(volume):
        bag = SOIL[0]
        global total
        total = volume / bag

        print("If you used 50L bags you would need", total ,"bags")
        print("To continue to payment please press 1")
        print("To return to the menu press 2")
        fifbag = input("")
        if fifbag == "1":
            payment()
        elif fifbag == "2":
            main()
        else:
            print("Please enter a number between 1 to 2") 




    
def payment():
    if answer =="1":
        pricedue = total * SOILPRICE[2]
        
    elif answer =="2":
        pricedue = total * SOILPRICE[1]
        
    elif answer =="3":
        pricedue = total * SOILPRICE[0]
    else:
        print("Please enter a number between 1 and 3") 
       
    print("Your total is",pricedue)

    print("Please enter your card details below")
    cardno = input("")
    global ordernumber
    orderno = random.randint(1, 1000)
    row = [orderno,cardno,pricedue]
    ORDERS.append_row(row)
    print("Your order number is",orderno,"you can use it to cancel your order")

    print("Press 1 to return to the main menu")
    if input()== "1":
        main()
    else:
        print("Please enter 1 to return to the main menu")
        
        



def cancelorder():
    print("Please enter your order number")
    
    userorder = input()
    order = ORDERS.row_values(ORDERS.find(userorder).row)
    
   
    
        
    

    print("Your order is ",order,"are you sure you want to cancel it?")
    print("If you wish to continue with cancelling your order please press 1")
    print("If you no longer wish to cancel it, press 2")
    
    if input() == "1":
        ORDERS.delete_rows(ORDERS.find(userorder).row)
        print("order",userorder,"has now been cancelled")
        main()
    if input()() == "2":
        main()
    else:
        print("Please enter a number between 1 and 2")    
    






def main():
    print("""
    
                        𝕊𝕠𝕚𝕝 𝕒𝕟𝕕 𝕡𝕝𝕒𝕟𝕥 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣  
                                                      |_|                                                                                                   """)
    print("""                                     
            ------------ 1. Soil Calculator and Purchase  ----------
            ------------ 2. Plant Calculator and Purchase ----------
            ------------ 3. Cancel an Order               ----------
                """)
    choice = input("Press the number of what you would like to do")
    if choice == "1":
        calcarea()
    if choice == "2":
        plantcalc()
    if choice == "3":
        cancelorder()
    else:
        print("Not a valid input please enter a number between 1 and 3")

main()