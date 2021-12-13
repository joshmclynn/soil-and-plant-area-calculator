import random
import math
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
PLANTS = SHEET.worksheet('plants')

SOIL = [50,100,2831]
SOILPRICE = [3.99,10,65]
PLANTSIZE = [.13,.225,.28]
enter_input = "Enter your input here:"
volume = 0
answer = ""
pricedue = 0
ordernumber = 0
num_invalid ="Please only enter numbers"
break_line = "-----------------------------------------------------------------"
total_area = 0
pot_choice = 0
plant_price_amount = 0


def plantcalc():
    # This function prompts the user to enter the pot size they want, sets the variables to match there choice then asks the user to enter the dimensions of the area they wish to plant
    # the function then calculates the area in m^2 and returns this to the user and then calls the function that will calculate total number of pots required at the users required size
    #
    print("Which pot size would you like to use in your garden")
    print(break_line)
    print("""
          ------------ 1. 1 Litre ------------
          ------------ 2. 5 Litre ------------
          ------------ 3. 10 Litre -----------
          """)
    print(break_line)
    print("Please enter the corrosponding number to your choice of pot size")
    while True:
        answer = input(enter_input)
        global pot_choice
        global pot_type
        if answer == "1":
            pot_choice = PLANTSIZE[0]
            pot_type = "1 Litre"
            
            break
        elif answer == "2":
            pot_choice = PLANTSIZE[1]
            pot_type = "5 Litre"
            
            break
        elif answer == "3":
            pot_choice = PLANTSIZE[2]
            pot_type = "10 Litre"
            break
        else:
            print("Please only choose from the above choices 1-3!")
    
    correctinput = r"^[.0-9]+$"
    while True:
        print(break_line)
        print("Please input the length of the area(in M and CM) and press enter")
        length = input(enter_input)
        true = re.match(correctinput,length)
        if true:
            break
            
        else:
            print(num_invalid)
    while True:
        print(break_line)
        print("Please enter the width of the area(in M and CM) and press enter")
        width = input(enter_input)
        true = re.match(correctinput,width)
        if true:
            
            break
        else:
            print(num_invalid)
    
    length = int(float(length))
    width = int(float(width))
    total_area = (length * width)
    print(break_line)
    print("The area you have is",total_area,"meters squared")
    
    calc_plant(total_area,pot_choice)
    
    
def calc_plant(total_area,pot_choice):
    # This function calculates the total plants needed for the user to fill their area, by dividing the total area by the  users selected pot size, it then prompts the user to either find
    # out how much a variety of plants would cost with that amount of individual units needed
    amount_needed = (total_area / pot_choice)
    amount_needed_round = math.floor(amount_needed)
    print(break_line)
    print("To fill the area with",pot_type,"pots, you would need",amount_needed_round,"pots")
    print("If you would like to know the average cost for",amount_needed_round,"pots,")
    print("please press 1, to return to the main menu press 2")
    
    while True:
        answer = input(enter_input)
        if answer == "1":
            plant_price(pot_type,amount_needed_round)
        elif answer == "2":
            main()
        else:
            print("Please choose from the above options 1-2")
    

def plant_price(pot_type, amount_needed_round):
    # This function calculates the price of the plants which the user would need, taking the information from a google sheets spreadsheet, it then times the price of each plant by the amount of pots
    # the user needs, returning this information to them. Using a for loop to create tuples within a list grouping the plant to the correct pricing.
    #
    print(break_line)
    print("Here are some examples of total prices for the amount of plants that you need for the pot size you want")
    print("Plant-Name / total price in pounds")
    
    print(break_line)
    price_list = []
    plant_list = []
    while True:
        if pot_type == "1 Litre":
            plant_list = PLANTS.col_values(1)
            price_list = PLANTS.col_values(2)
            break   
        elif pot_type == "5 Litre":
            plant_list = PLANTS.col_values(1)
            price_list = PLANTS.col_values(3)
            break
        elif pot_type == "10 Litre":
            plant_list = PLANTS.col_values(1)
            price_list = PLANTS.col_values(4)
            break
    
    display_list = []
    full_price = [(int(float(price_list[i])) * amount_needed_round)for i in range(0,len(price_list))]
    display_list = [(plant_list[i],full_price[i]) for i in range(0, len(plant_list))]
    print(display_list)
    print("To return to the menu please enter 1")
    print(break_line)
    answer = input(enter_input)
    if answer =="1":
        main()
    else:
        print("To return to the menu enter 1!")
            
            
def calcarea():
    # This function prompts the user to enter the dimensions of the area they are wanting to fill with soil, it only allows the user to enter numbers, prompting them to re-enter if 
    # otherwise, it then calculates the volume of the area, then converts this number into litres then returning this information to the user, it then sends the user to a function allowing
    # them to choose the size of soil bags they want
    correctinput = r"^[.0-9]+$"
    while True:
        print(break_line)
        print("Please input the length of the area(in M and CM) and press enter")
        length = input(enter_input)
        true = re.match(correctinput,length)
        if true:
            break
        else:
            print(num_invalid)
    while True:
        print(break_line)
        print("Please enter the width of the area(in M and CM) and press enter")
        width = input(enter_input)
        true = re.match(correctinput,width)
        if true:
            break
        else:
            print(num_invalid)
    while True:
        print(break_line)
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
    print(break_line)
    print("The total volume you have is" ,volume,"in litres")
    whatsoil()
    return volume
    
        
def whatsoil():
    # This function prompts the user to choose from the soil bag sizes and then sends this infomation to the relevant function (50L, 100L or bulkbag)
    print(break_line)
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
    # This function returns the total amount of "bulk-bags" needed to fill the users inputed area, it then prompts the user to either navigate to payment or return to the menu
    bag = SOIL[2]
    global total
    pretotal = (volume / bag)
    total = math.ceil(pretotal)
    print(break_line)
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
    # This function returns the total amount of 100 litre soil bags needed to fill the users inputed area, it then asks if the user would like to either 
    # buy smaller bags or continue to payment, or return to the menu
        bag = SOIL[1]
        global total
        pretotal = volume / bag
        total = math.ceil(pretotal)
        print(break_line)
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
    # This function returns the total amount of 50 litre soil bags needed to fill the users inputed area(rounded up as you cant sell half bags)
    # It then prompts the user to either continue to payment or return to the menu
        bag = SOIL[0]
        global total
        pretotal = volume / bag
        total = math.ceil(pretotal)
        print(break_line)
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
    # This function calculates the price due from the users order, then returns the price to the user and asks whether they would like to continue
    # it then asks for the users card number only allowing 12 digits to be entered otherwise returning a message asking for resubmission, it then sends the information to the addtoorder function
    global pricedue
    if answer =="1":
        pricedue = round(total * SOILPRICE[2],2)
        
    elif answer =="2":
        pricedue = round(total * SOILPRICE[1],2)
    elif answer =="3":
        pricedue = round(total * SOILPRICE[0],2)
    
    print(break_line)
    print("Your total is : £",pricedue)
    print("To pay please enter 1")
    print("enter 2 to return to the main menu")
    while True:
        payans = input(enter_input)
        
        if payans == "1":
            validate_card()
            break  
        elif payans =="2":
                main()
                break
        else: 
            print("Please enter either 1 or 2!")
            

def validate_card():
    print(break_line)
    print("Please enter your 12 digit card number")
    while True:
        cardno = input(enter_input)
        correct_card = r"^[0-9]{12}$"
        true = re.match(correct_card, cardno)       
        if true:
            addtoorders(cardno,pricedue)
            break
        else:
            print("Incorrect input please enter your 12 digit card number")
                  
    
def addtoorders(cardno,pricedue):
    # This function adds the users order in a new row to the googlesheets spreadsheet, it also generates a random number between 1 and 1000 for the users order number.
    # this function also returns the users order number allowing them to cancel that order in the future using other features of this application
    #
    orderno = random.randint(1, 1000)
    row = [orderno,cardno,pricedue]
    ORDERS.append_row(row)
    print(break_line)
    print("Your order number is",orderno,"you can use it to cancel your order")
    print("Enter 1 to return to the main menu")
    order_ans = input(enter_input) 
    while True:
        if  order_ans == "1":
            main()
            break
        else:
            print("To return to the menu press m!")
        
        
def cancelorder():
    # When the user completes an order they are given an order number, this function allows the user to cancel their order
    # This function allows the user to enter there order number and if this number corresponds to a number within the spreadsheet held on google sheets
    # the user is returned the option to cancel there order, it then communicates with google sheets and deletes the row from the spreadsheet
    # If the order number doesnt exist the user is returned a message that the order number is incorrect
    print(break_line)
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
    print(break_line)       
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
    # This is the main function with the options allowing the user to navigate through the application
    # It has 3 options to choose from which will send the user to the chosen part.
    # The user will also be returned here after using each one of the different options
    print("""
    
                        𝕊𝕠𝕚𝕝 𝕒𝕟𝕕 𝕡𝕝𝕒𝕟𝕥 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣  
                                                                                                                                                         """)
    print("""                                     
            ------------ 1. Soil Calculator and Purchase            ----------
            ------------ 2. Plant Calculator and Purchase           ----------
            ------------ 3. Cancel an Order using your order number ----------
            ------------------------------------------------------------------       
              Enter the corresponding number to access your selection (1 - 3)
        
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