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
    global answer
    answer = input("1")
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

        if total / 50 == 0 :
            print("You could have this order in smaller bags")
            print("If you would like to order a smaller bag press 1 or 2 to continue with your order")
            if input()== 1:
                fiftybag(volume)

        
    

def fiftybag(volume):
        bag = SOIL[0]
        global total
        total = volume / bag

        print("If you used 50L bags you would need", total ,"bags")
    




    
def payment():
    if answer =="1":
        pricedue = total * SOILPRICE[2]
        
    elif answer =="2":
        pricedue = total * SOILPRICE[1]
        
    elif answer =="3":
        pricedue = total * SOILPRICE[0]
       
    print("Your total is",pricedue)

    print("Please enter your card details below")
    cardno = input("")
    orderno = ((ORDERS.row_count) + 1)
    i = 1

    row = [orderno,cardno,pricedue]
    ORDERS.append_row(row)



calcarea()