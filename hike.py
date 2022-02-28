# This is the PYTHON version of the hike_planner

from WxAPI import get_weather
from tkinter import *


# Build the list
backpacks = []
tents = []
mattresses = []
sleep_bags = []
inventory = [
    backpacks,
    tents,
    mattresses,
    sleep_bags
]

print("*** WELCOME TO GUNNIE'S HIKE PLANNER ***\n")


# def login():
#     print("<<Log In>>>")
#     user_name = input("enter user name:\n>>>")
#     password = input("enter password:\n>>>")
#     if user_name == "Gunnie" and password == "12345":
#         main_menu()
#     else:
#         print("incorrect user name or password\n")
#         login()




def main_menu():
    x = True
    while x:
        print("<<<Main Menu>>>\nPlease select an option\n")

        selection = (input(str(
            "1 Inventory\n"
            "2 Plan Hike\n"
            "3 Weather\n"
            "4 Convert Document\n"
            "5 Help\n"
            "6 Quit\n"
            ">>>"
        )))

        if selection == '1':
            inventory_menu()

        if selection == '2':
            print("running hike planner function\n")
            plan_hike()

        if selection == '3':

            # make this function as a microservice instead of an import
            # 1. Get the zipcode as below. (I don't think it needs to be an integer, but check on this.
            # 2. with weather.json open, write zipcode to json
            # 3. WxAPI.py monitors weather.json every second. if weather.json != "", do it's API thing and write the
            #    weather back into weather.json
            # 4. Back in hike.py begin monitoring json every 2 seconds. if weather.json != str(zip_code) or
            #    weather.json != "", print out the json text
            # ?. (what happens if both processes are opening at the same time?)
            # 5. Put this in a separate function to be called when selecetion == 3. (i.e. don't write it
            #    here in the main_menu function.

            zip_code = int(input("Enter a US zipcode"))
            print(
                "\n\nThe Weather in your area is:",
                get_weather(zip_code),
                "\n\n"
            )
            main_menu()

        if selection == '4':
            print("converting your .txt file to pdf. because we can")
            # 1. the planHike function will write to a .txt file (e.g. hike_list.txt) saved in this directory
            # 2. this selection will call a convert_txt() function which calls the microservice
            convert_txt()
            print("Text file converted to pdf")  # figure out how to get an actual confirmation on this without
                                                    # having to monitor a pipe.
            main_menu()

        if selection == '5':
            help_menu()

        if selection == '6':
            selection = input(str("Are you sure you want to quit? Y/N\n>>>"))
            if selection == "Y" or selection == "y":
                print("See you next time!")
                x = False


def inventory_menu():
    while True:
        print("")
        print("<Inventory Menu>\nPlease select an option\n")
        selection = input(str(
            "1 Display Full Inventory\n"
            "2 Display Items by Type\n"
            "3 Add Item\n"
            "4 Edit Item\n"
            "5 Delete Item\n"
            "6 Return to Main Menu\n"
            ">>>"
        ))

        if selection == "1":
            print_inventory()
            inventory_menu()

        if selection == "2":
            print_item_by_type()
            inventory_menu()

        if selection == "3":
            item_type = input(str(
                "What type of item do you wish to add?\n"
                "1. Backpacks\n"
                "2. Tents\n"
                "3. Sleeping Bags\n"
                "4. Mattresses\n"
                ">>>"
            ))
            name = input(str(
                "Enter item name\n"
                ">>>"
            ))
            style = input(str(
                "What type/style of hike will you be doing?\n"
                "1. UL\n"
                "2. Heavy\n"
                "3. Day\n" 
                ">>>"
            ))
            weight = input(
                "What is the item's weight?\n" 
                "(Enter weight in pounds to nearest 10th. e.g. 5.7\n)"
                ">>>"
            )

            add_item(item_type, name, style, weight)
            inventory_menu()

        if selection == "6":
            print("")
            main_menu()


def print_inventory():
    print("INVENTORY\n\n       BACKPACKS\n")
    for item in backpacks:
        item.print_item_info()
        print("")
    print("       TENTS")
    for item in tents:
        item.print_item_info()
        print("")
    print("       MATTRESSES")
    for item in mattresses:
        item.print_item_info()
        print("")
    print("       SLEEPING BAGS")
    for item in sleep_bags:
        item.print_item_info()
        print("")


def print_item_by_type():
    selection = (input(str(
        "Select Item Type:\n"
        "1 Backpacks\n"
        "2 Tents\n"
        "3 Mattresses\n"
        "4 Sleeping Bags\n"
        "5 Return to Inventory Menu\n"
        "6 Return to Main Menu\n"
        ">>>"
    )))
    if selection == "1" \
            or selection == "Backpacks" \
            or selection == "backpacks"\
            or selection == "B" \
            or selection == "b":
        print("INVENTORY - BACKPACKS\n")
        for item in backpacks:
            item.print_item_info()
            print("\n\n")

    elif selection == "2" \
            or selection == "Tents" \
            or selection == "tents" \
            or selection == "T" \
            or selection == "t":
        print("\nINVENTORY - TENTS\n")
        for item in tents:
            item.print_item_info()
            print("\n\n")

    elif selection == "3" \
            or selection == "Mattresses" \
            or selection == "mattresses" \
            or selection == "M" \
            or selection == "m":
        print("\nINVENTORY - TENTS\n")
        for item in mattresses:
            item.print_item_info()
            print("\n\n")

    elif selection == "4" \
            or selection == "Sleeping Bags" \
            or selection == "sleeping bags" \
            or selection == "S" \
            or selection == "s":
        print("\nINVENTORY - TENTS\n")
        for item in sleep_bags:
            item.print_item_info()
            print("\n\n")

    elif selection == "5":
        inventory_menu()

    elif selection == "6":
        main_menu()


def add_item(item_type, name, style, weight):

    # need to control variable names for new item creation
    new_item = Item(item_type, name, style, weight)
    if item_type == "Backpacks" \
            or item_type == "backpacks" \
            or item_type == "Backpack" \
            or item_type == "backpack" \
            or item_type == "1" \
            or item_type == "B" \
            or item_type == "b":
        item_type = "Backpack"
        backpacks.append(new_item)
    if item_type == "Mattress" \
            or item_type == "mattress" \
            or item_type == "mattresses" \
            or item_type == "Mattresses" \
            or item_type == "2" \
            or item_type == "M" \
            or item_type == "m":
        item_type = "Mattress"
        mattresses.append(new_item)
    if item_type == "Sleeping Bag" \
            or item_type == "sleeping bag" \
            or item_type == "Sleeping Bags" \
            or item_type == "sleeping bags" \
            or item_type == "Sleeping bag" \
            or item_type == "Sleeping bags" \
            or item_type == "3" \
            or item_type == "S" \
            or item_type == "s":
        item_type = "Sleeping Bag"
        sleep_bags.append(new_item)
    if item_type == "Tents" \
            or item_type == "tents" \
            or item_type == "Tent" \
            or item_type == "tent" \
            or item_type == "4" \
            or item_type == "T" \
            or item_type == "t":
        item_type = "Tent"
        tents.append(new_item)

    # print("Item added")


def plan_hike():
    hike_type = input(str(
        "What type/style of hike will you be doing?\n"
        "(Enter string: UL, Heavy, or Day):\n"
        ">>>"
    ))

    weather = input(str(
      "What is the expected weather?\n"
      "(Enter string):\n"
      "'Fair'\n"
      "'Rain'\n"
      "'Snow'\n"
      "'Sub-Zero'\n"
      ">>>"
    ))

    print(
        "\nITEM TYPE:      Backpacks\n"
        "NAME:           Osprey Exos\n"
        "HIKING STYLE:   UL\n"
        "WEIGHT:         2.5\n\n"
        
        "ITEM TYPE:      Tents\n"
        "NAME:           BigAgnes Copper Spur\n"
        "HIKING STYLE:   Ultra-light\n"
        "WEIGHT:         2.6\n\n"
        
        "ITEM TYPE:      Mattress\n"
        "NAME:           POWERLIX SLEEPING PAD\n"
        "HIKING STYLE:   Ultra-light\n"
        "WEIGHT:         1.32\n\n"
        
        "ITEM TYPE:      Sleeping Bag\n"
        "NAME:           REI Magma 15\n"
        "HIKING STYLE:   15 degree\n"
        "WEIGHT:         2.2\n\n"
    )

def convert_txt():

    # 1. write True to converter.txt (initialize as False)
    # 2. WxAPI.py will monitor converter.txt every second. If True, it will first overwrite True with False.
    # 3. it will then do it's file conversion
    # 4. figure out a good way to return a success message without having to monitor another file...
    with open('converter.txt', 'w') as signal:
        signal.write("True")


def save_inventory():
    pass
#  with inventory.txt open as in file:
#   write inventory list to the file

def load_inventory():
    pass
#  with inventory.txt open as in file:
#   read inventory list from the file, assign that value to inventory variable
# it should just be the a list in JSON format, I think

def help_menu():
    selection = (input(str(
        "What do you want to know about?\n"
        "1 Inventory\n"
        "2 Plan Hike\n"
        "3 Weather\n"
        "4 Convert Document\n"
        "main menu\n"
    )))

    if selection == 1 \
            or selection == '1' \
            or selection == 'Inventory' \
            or selection == 'inventory' \
            or selection == 'i' \
            or selection == 'I':
        print(
            "Information about the inventory:\n"
            "In the inventory menu, you can organize and manage your gear.\n"
            "1 Display Full Inventory: This will display your entire inventory\n"
            "2 Display Items by Type: This will display items sorted by type\n"
            "3 Add Item: You can add an item to your inventory with this option\n"
            "4 Edit Item: here you can edit the attributes of any item\n"
            "5 Delete Item: Delete an item from the inventory\n"
        )
    elif selection == 2 \
            or selection == '2' \
            or selection == 'Plan Hike' \
            or selection == 'plan hike' \
            or selection == 'p' \
            or selection == 'P':
        print("Information about Planning Hikes:\n\n\n")

    elif selection == 3 \
             or selection == '3' \
             or selection == 'Weather' \
             or selection == 'weather' \
             or selection == 'w' \
             or selection == 'W':

                print(
                    "Information about the Weather\n"
                    "Enter you ZIP code (US only) to retrieve today's weather.\n"
                    "This functionality draws on the NOAA's weather service API\n"
                    "Currently, this program returns a summary of today's weather for demonstration purposes.\n"
                    "Additional information is available through this API for future expansion(e.g. forecast)\n\n"
                )

    elif selection == 4 \
             or selection == '4' \
             or selection == 'Convert Document' \
             or selection == 'convert document' \
             or selection == 'c' \
             or selection == 'C':
        print("Information about Converting documents\n\n\n")

    else:
        help_menu()


class Item:
    def __init__(self, item_type, name, style, weight):
        self._item_type = item_type  # Backpack, Tent, Mattress, Sleeping_Bag
        self._name = name  # any
        self._style = style  # UL, Heavy, Day
        self._weight = weight  # float

    def print_item_info(self):
        print(f"ITEM TYPE:      {self._item_type}\n"
              f"NAME:           {self._name}\n"
              f"HIKING STYLE:   {self._style}\n"
              f"WEIGHT:         {self._weight}"
              )


add_item("Backpacks", "Osprey Exos", "UL", 2.5)
add_item("Backpacks", "REI", "Heavy", 6.5)
add_item("Tents", "BigAgnes Copper Spur", "UL", 2.6)
add_item("Tents", "REI 4 pax", "Heavy", 8.2)
add_item("Mattress", "POWERLIX SLEEPING PAD", "UL", 1.32)
add_item("Mattress", "Therm-A-Rest", "UL", 2.4)
add_item("Sleeping Bag", "REI Magma 15", "UL", 2.2)
add_item("Sleeping Bag", "Feathered Friends", "UL", 2.4)

#login()
main_menu()

# window = Tk()
# window.title("Gunnie's Hike Planner")
# window.geometry("600x600")
# window.configure(background="black")
#
# main_picture = PhotoImage(file="mountain_gif.gif")
# Label(window, image=main_picture, bg="black").grid(row=0, column=0)
#
# Label(window, text="Welcome to Gunnie's Hike Planner", bg="black", fg="white", font="none 12 bold")\
#     .grid(row=1, column=0)
#
# window.mainloop()





