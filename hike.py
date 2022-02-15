# This is the PYTHON version of the hike_planner

import WxAPI
import requests

backpacks = []
tents = []
mattresses = []
sleep_bags = []
pants = []
shirts = []
socks = []
jackets = []
rain_gear = []
shoes = []
snow_ice = []
cooking = []
bears = []
other = []
inventory = [backpacks,
             tents,
             mattresses,
             pants,
             sleep_bags,
             shirts,
             socks,
             jackets,
             rain_gear,
             shoes,
             snow_ice,
             cooking,
             bears,
             other]

print("*** WELCOME TO GUNNIE'S HIKE PLANNER ***\n")


def login():
    print("<<Log In>>>")
    user_name = input("enter user name:\n>>>")
    password = input("enter password:\n>>>")
    if user_name == "Gunnie" and password == "12345":
        main_menu()
    else:
        print("incorrect user name or password\n")
        login()


def main_menu():
    while True:
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
            #main_menu()
        if selection == '3':
            print("running weather API\n")
            x = requests.get("https://api.weather.gov/points/39.7456,-97.0892")
            print(x.text)
            main_menu()
        if selection == '6':
            selection = input(str("Are you sure you want to quit? Y/N\n>>>"))
            if selection == "Y" or selection == "y":
                print("See you next time!")
                return


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
                "(enter string):\n"
                "backpacks\n"
                "tents\n"
                "sleep_bags\n"
                "pants\n"
                "shirts\n"
                "socks\n"
                "jackets\n"
                "rain_gear \n"
                "shoes\n"
                "snow_ice \n"
                "cooking\n"
                "other\n"
                ">>>"
            ))
            name = input(str(
                "Enter item name\n"
                "Enter String\n"
                ">>>"
            ))
            style = input(str(
                "What type/style of hike will you be doing?\n"
                "(Enter string):\n"
                "'UL Day'  --- Ultra-light day hike\n"
                "'UL Short' --- Less than one week\n"
                "'UL Long' --- More than one week\n" 
                "'Normal Day' ---  Normal day hike\n"
                "'Normal Short' --- Less than one week\n"
                "'Normal Long' --- More than one week\n"
                "'Luxury' --- Bringing the Kitchen Sink\n"
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
    if selection == "1" or selection == "Backpacks" or selection == "backpacks":
        print("INVENTORY - BACKPACKS\n")
        for item in backpacks:
            item.print_item_info()
            print("")
    elif selection == "2" or selection == "Tents" or selection == "tents":
        print("\nINVENTORY - TENTS\n")
        for item in tents:
            item.print_item_info()
            print("")


def add_item(item_type, name, style, weight):
    new_item = Item(item_type, name, style, weight)
    if item_type == "Backpacks":
        backpacks.append(new_item)
    if item_type == "Mattress":
        mattresses.append(new_item)
    if item_type == "Sleeping Bag":
        sleep_bags.append(new_item)
    if item_type == "Tents":
        tents.append(new_item)

    # print("Item added")


def plan_hike():
    hike_type = input(str(
        "What type/style of hike will you be doing?\n"
        "(Enter string):\n"
        "'UL Day'  --- Ultra-light day hike\n"
        "'UL Short' --- Less than one week\n"
        "'UL Long' --- More than one week\n"
        "'Normal Day' ---  Normal day hike\n"
        "'Normal Short' --- Less than one week\n"
        "'Normal Long' --- More than one week\n"
        "'Luxury' --- Bringing the Kitchen Sink\n"
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

def save_inventory():
    pass
#  with inventory.txt open as in file:
#   write inventory list to the file


def load_inventory():
    pass
#  with inventory.txt open as in file:
#   read inventory list from the file, assign that value to inventory variable
# it should just be the a list in JSON format, I think


class Item:
    def __init__(self, item_type, name, style, weight):
        self._item_type = item_type  # Backpack, Tent, Mattress, Sleeping_Bag
        self._name = name
        self._style = style
        self._weight = weight

    def print_item_info(self):
        print(f"ITEM TYPE:      {self._item_type}\n"
              f"NAME:           {self._name}\n"
              f"HIKING STYLE:   {self._style}\n"
              f"WEIGHT:         {self._weight}"
              )

class Wearable:
    def __init__(self, type, name, style, weight):
        self._type = type  # Pants, Shirt, Jacket, Socks
        self._name = name
        self._style = style
        self._weight = weight

class Rain_Gear:
    def __init__(self) -> None:
        pass

class Safety:
    def __init__(self) -> None:
        pass

class Shoes:
    def __init__(self) -> None:
        pass

class Snow_and_Ice:
    def __init__(self) -> None:
        pass
        
class Cooking:
    def __init__(self) -> None:
        pass

class Bears:
    def __init__(self) -> None:
        pass

class Other:
    def __init__(self):
        pass







add_item("Backpacks", "Osprey Exos", "UL", 2.5)
add_item("Backpacks", "REI", "Heavy", 6.5)
add_item("Tents", "BigAgnes Copper Spur", "Ultra-light", 2.6)
add_item("Tents", "REI 4 pax", "Family", 8.2)
add_item("Mattress", "POWERLIX SLEEPING PAD", "Ultra-light", 1.32)
add_item("Mattress", "Therm-A-Rest", "Medium", 2.4)
add_item("Sleeping Bag", "REI Magma 15", "15 degree", 2.2)
add_item("Sleeping Bag", "Feathered Friends", "20", 2.4)
#
#
#
# print(inventory)
# print_inventory()
# print_inventory_packs()
login()





