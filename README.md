# Soil and Plant calculator
## Description
   Soil and Plant Calculator is an interactive application that allows the user to gain useful information based on there inputs, such as 
   soil calculations from the users entered information with pricing and ordering available. The plant calculator calculates various amounts of 
   plants needed for the user givens area, it then also returns a variety of example plants with the total cost for said plants(that the user would need).
## Contents
   * UX 
      * User Story
      * Project Goals
      * Structure of application
    * Features
      * Current features
      * Future features
    * Technologies Used
      * Language
      * Other
    * Testing
      * Bugs/Fixes
      * Validation
    * Deployment
    * Credits
## UX
### User Story
   . The user I invisage using this application would be someone who would be looking to either buy soil or different types of plants.
   . The user could also be someone planning a garden design and needing to work out costs for various aspects of there garden.
   
   . "As a user I want to be able to easily navigate and find the information that im after"
   ." As a user I want my input to be acknoledged and provided back to me in meaninful ways"
   ." As a user I want to be able to understand the information that is provided back to me"
### Project Goals
   . When creating this program my goals were:
      * To create an application that was easy to operate
      * To create an application that provided functionality
      * To have a link between data stores in GoogleSheets and the user
      * Use readable and easy to maintain code
### Structure
![DATA Structure](/docs/data_model_flow.PNG "Image showing the functionality and flow of the application")

   . The structure of the application is demonstrated above, with three functions "payment/cardno/orderno" and "return example of pots" adding/returning/or removing information from GoogleSheets via API
   . I felt an important aspect was having a central main menu style in order to allow the user to navigate easily throughout the application
## Features
### Current Features
* Main Menu 
    * The main menu is loaded when the application is started up, it has a small welcome message followed by the options of the different features within the application
        allowing the user to navigate to their desired sections
    * The main menu is also used as the escape from different functions if the user decides they no long wish to proceed with their chosen function
![Main_Menu](/docs/mainmenu.PNG "ScreenShot of main menu")
* Soil Calculator
    * The soil calculator takes inputs from the user for the length, depth and width of the area they wish to fill with soil in M/Cm, It then takes this information and converts       it into m^3 then into litres and prints the literage of the users area to them.
    * The user is the prompted on what size soil bag they would like from three options.
    * Each given bag due to them all being different sizes, returns the amount of bags(User choice) required to fill the area they have.
    * If the user orders under 1 bulk bag they are also given the option to choose a smaller bag in order for them to not have wastage.
    * The user is then prompted on whether they would like to proceed to payment for the soil they need, if they choose to complete payment they will be forwarded to the next         function which I will discuss below.
![Soil Calculator](/docs/soilcalc.PNG "Screen shot of the soil calculator function")
* Plant Calculator
    * The plant calculator first asks the user the size of pot they would like there plants to be in order to fill their gardens or areas
    * The user is then prompted to enter the length and width of the area to return and print to the user the users area in m^2.
    * The user is also told how many pots, at their chosen size it would take for them to fill the area with plants.
![Plant Calculator](/docs/plantcalc.PNG "Screenshot of the plant calculator")
    * The user is then also given the option to get the prices for a variety of plants at the amount of pots they need.
    * The function then gets the needed information from the googlesheets document and times the individual pot size price by the amount of pots they need, printing this to the        user.
![Plant Calculator/Plant amounts](/docs/plantprice.PNG "Screenshot showing the returned variety of plants and total cost for the amount needed")
* Payment
    * When using the soil calculator you are given the option to "purchase" the amount of soil you need.
    * This function tells the user to total price and asks them to enter their 12 digit card number.
    * When this card no is correct (Twelve digits 0/9) the function creates the order adding the below to a new row in the "orders" googlesheet :
      * Randomized order number
      * Card number 
      * total price
![Payment](/docs/payment.PNG "Screenshot of the payment function")
![PaymentAPI](/docs/api.PNG "Screenshot of the googlesheet with the above order in")
* Cancel an Order
    * When the user completes an order they are given an order number, this feature allows the user to use that order number in order to cancel the order.
    * Firstly the user is prompted to enter there order number, if this order number cant be found on the "order" sheet a message is returns prompting the user to enter again.
    * When an order is found it is printed to the user, asking if they are sure they would like to cancel the order, if they choose to cancel the order, the order is then removed from the "order" sheet and a message is returned that the order has been deleted.
![Cancel Order](/docs/cancelorder.PNG "Screenshot of the cancel an order feature")
###  Future features
 * In the future I would like to build the front end interface allowing for more userbility, allowing for a more tailored experience for the user.
 * I would also like to update the payment function to be more real word asking for a full CC number with expiry date etc.
## Technologies Used
### Main Languages
The project aside from the code institutes template is 100% [python](https://www.python.org/)
### Other
  * [GoogleSheets](https://www.google.co.uk/sheets/about/)To hold the users information and the plants information
  * [Heroku](https://www.heroku.com/) deployment
  * [Gspread](https://docs.gspread.org/en/latest/)Api
  * [Pep8](http://pep8online.com/) validation
  * [Regex101](https://regex101.com/) Testing regex
## Testing
### Bugs/Fixes
  * Most of the bugs during this project were caused by spelling mistakes or mislabling/not converting from string to float
  * One bug that was brought to my attention was when a user entered a number below 1 in the functions that would calculate area it would always return 0 for the total area,
    I later discoved this was due to me converting from a string to an int, when I should have just been converting a float instead.
  * As far as I am aware there are no current bugs.
  * During testing I have been very thorough when making sure that I try to input wrong information in each of the input sections, all of these tests have proved positive.
  * I found a way to avoid bugs during the development of this code was to complete individual functions and run them on the command line and test before I moved on.
  * One potential bug I could see would be a user ordering a soil amount that would return a price that would be longer than the terminal(80 characters) caused a split line on the users end.
### Validations
  * I used [Pep8 online](http://pep8online.com/) to validate my code, not warnings.
![Pep8](/docs/pep8.PNG "Screenshot from pep8")
## Deployment
To deploy this project in heroku these steps were taken:
* Create/Log in to your account Heroku.
* Select "new" and "Create new app" from the main dashboard.
* Create a unique name for the project.
* Click the deploy tab and select the setting tab.
* Config Var for creating the app :
    * Click reveal config var. In the key field add CREDS and in the value field input the creds.json file that has been added to the gitignore list.
* Add buildpacks for this application. Firstly python and NodeJs, python will have to be the buildpack at the top.
* Select the deploy tab and navigate to the deployment method section.
* Select github and connect your github to this section.
* Enter the name of the repo you wish to use.
* Select connect to application
* Select the manual deploy button which will rebuild and deploy your site and give you a live link to the page.
* You can also choose automic deploys which will tell heroku to rebuild and then deploy your application everytime you commit on github.

### The deployed application is located here:
[Soil and Plant Calculator](https://soil-and-plant-area-calculator.herokuapp.com/)

## Credits
All Code is written and produced by myself.

[Regex101](https://regex101.com/) For testing regex againts multiple inputs at a time.


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
  
