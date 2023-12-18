# This is for the delay on print text.
import time
print ("""    
  _      __    __                     __                      _   __            ___             __  ___         __   _         
 | | /| / /__ / /______  __ _  ___   / /____    __ _  __ __  | | / /__ ___  ___/ (_)__  ___ _  /  |/  /__ _____/ /  (_)__  ___ 
 | |/ |/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \  /  ' \/ // /  | |/ / -_) _ \/ _  / / _ \/ _ `/ / /|_/ / _ `/ __/ _ \/ / _ \/ -_)
 |__/|__/\__/_/\__/\___/_/_/_/\__/  \__/\___/ /_/_/_/\_, /   |___/\__/_//_/\_,_/_/_//_/\_, / /_/  /_/\_,_/\__/_//_/_/_//_/\__/ 
                                                    /___/                             /___/                                    
""")

# This will display the list of available choices with their codes and prices.
print("            ▂▃▅▇█▓▒░𝙷𝚎𝚛𝚎 𝚒𝚜 𝚝𝚑𝚎 𝚕𝚒𝚜𝚝 𝚘𝚏 𝚒𝚝𝚎𝚖𝚜░▒▓█▇▅▃▂")
print("""==========================+Drinks+=============================""")
print("""||        Name: Redbull| Price: 2.50 Aed| Code: a1           || 
||        Name: Water| Price: 1.00 Aed| Code: a2             ||
||        Name: Vimto| Price: 3.50 Aed| Code: a3             ||
||        Name: Coca-Cola| Price: 2.50 Aed| Code: a4         ||
||        Name: Lipton Iced Tea| Price: 5.00 Aed| Code: a5   ||
||        Name: Starbucks| Price: 10.00 Aed| Code: a6        ||""")
print("""===========================+Snacks+============================""")
print("""||        Name: Kitkat| Price: 4.00 Aed| Code: b1            ||
||        Name: Snickers| Price: 4.00 Aed| Code: b2          ||
||        Name: M&M| Price: 4.00 Aed| Code: b3               ||
||        Name: Sohar Chips| Price: 3.00 Aed| Code: b4       ||
||        Name: Ruffles| Price: 7.50 Aed| Code: b5           ||
||        Name: Skittles| Price: 5.00 Aed| Code: b6          ||
===============================================================
""")

#==================================================#
# This is the dictionaries that the code will look at when we select an item.
Products = {
  'a1' : {"name" : "Redbull","price" : 2.50},
  'a2' : {"name" : "Water","price" : 1.00},
  'a3' : {"name" : "Vimto","price" : 3.50},
  'a4' : {"name" : "Coca-Cola","price" : 2.50},
  'a5' : {"name" : "Lipton Iced Tea","price" : 5.00},
  'a6' : {"name" : "Starbucks","price" : 10.00},
  'b1' : {"name" : "Kitkat","price" : 4.00},
  'b2' : {"name" : "Snickers","price" : 4.00},
  'b3' : {"name" : "M&M","price" : 4.00},
  'b4' : {"name" : "Sohar Chips","price" : 3.00},
  'b5' : {"name" : "Ruffles","price" : 7.50},
  'b6' : {"name" : "Skittles","price" : 5.00}
  }

# This part asks for the users input.
choice = input("Enter the item number you wish to purchase. Don't worry we have an infinite amount of the products: ")

# This part checks if the users input is in the products dictionary and if it is it will print the statement below.
if choice in Products:                                                 
    choosen_item = Products[choice]
    print(f"You have selected {choosen_item['name']}.")
    # time.sleep will delay the appearance of the text and "money" will check the chosen items price and will display it.
    time.sleep(1)
    money = choosen_item['price']
    while money > 0:
        try:
            time.sleep(1)
            # This part asks for the users money with 2 decimals due to ".2f" and if money is greater than money which is 0-
            # it will deduct from the chosen items price.
            payment = float(input(f"Please insert {money:.2f} Aed: "))
            if payment >= money:
                change = payment - money
                print("Processing Order...")
                time.sleep(1)
                # This will print the amount of change the user will recieve also available in decimals due to ".2f"
                print(f"Thank You for using the vending Machine Your change is {change:.2f} Aed.")
                time.sleep(1)
                # This prints the users chosen items name.
                print(f"{choosen_item['name']} Has been dispensed.")
                time.sleep(1)
                # This asks if the users wants to purchase more items in either lower or uppercase letters.
                again = input("Will there be anything else? Y or N: ").lower()
                # If they decide to continue with the 'yes' or 'y' it would ask them what other items do they want to purchase.
                # The process is similar to the one above.
                if again == "y" or again == "yes":
                  time.sleep(1)
                  choice = input ("What else would you like?: ")
                  choosen_item = Products[choice]
                  time.sleep(1)
                  money = choosen_item['price']
                  continue
                # If they dont want to continue it would print the statement below and break process 
                else:
                    time.sleep(1)
                    print ("Thank you for using the vending machine")
                    break
            # If the user inputs a insufficient amount of money this will print.
            else:  
              time.sleep(1)
              print("Insufficient payment. Please insert more money.")
            money -= payment
          # If the user inputs a letters, symbol or anything that isn't a number this will print.
        except ValueError:
           time.sleep(1)
           print("Invalid payment amount. Please enter a valid number.")

# If the user inputs a invalid code or values this would print.       
else:
    time.sleep(1)
    print(f"There is no item with the code: \"{choice}\"")
    time.sleep(1)
    print("Please try again.")
    # All of these are just like the ones above please refer to those for explanations
    time.sleep(1)
    choice = input ("What would you like?: ")
    choosen_item = Products[choice]
    time.sleep(1)
    money = choosen_item['price']
    while money > 0:
            time.sleep(1)
            payment = float(input(f"Please insert {money:.2f} Aed: "))
            if payment >= money:
                change = payment - money
                time.sleep(1)
                print("Processing Order...")
                time.sleep(1)
                print(f"Thank You for using the vending Machine Your change is {change:.2f} Aed.")
                time.sleep(1)
                print(f"{choosen_item['name']} Has been dispensed.")
                time.sleep(1)
                again = input("Will there be anything else? Y or N: ").lower()
                if again == "y" or again == "yes":
                  time.sleep(1)
                  choice = input ("What else would you like?: ")
                  choosen_item = Products[choice]
                  time.sleep(1)
                  money = choosen_item['price']
                  continue
                else:
                 time.sleep(1)
                 print ("Thank you for using the vending machine")
                break
# Credit to Denz for helping me.