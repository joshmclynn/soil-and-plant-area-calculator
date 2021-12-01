<<<<<<< HEAD
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

        









    




=======
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

price = SHEET.worksheet('price')

priceData = price.get_all_values()

print(priceData)
>>>>>>> e2b4f1861c90b64ce40dd69b4b5f88f51a61dbe0
