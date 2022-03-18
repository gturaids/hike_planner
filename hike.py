# This is the PYTHON version of the hike_planner

from WxAPI import get_weather


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
            plan_hike()

        # This is the microservice provided to my teammate
        if selection == '3':
            zip_code = int(input("Please enter a US zipcode"))
            print(
                "\n\nThe Weather in your area is:",
                get_weather(zip_code),
                "\n\n"
            )
            main_menu()

        if selection == '4':
            print("converting your .txt file to pdf. because we can")
            convert_txt()
            print("Text file converted to pdf")
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
            if item_type == "1":
                item_type = "Backpack"
            if item_type == "2":
                item_type = "Tent"
            if item_type == "3":
                item_type = "Sleeping Bag"
            if item_type == "4":
                item_type = "Mattress"

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
            if style == "1":
                style = "UL"
            if style == "2":
                style = "Heavy"
            if style == "3":
                style = "Day"
            weight = input(
                "What is the item's weight?\n" 
                "(Enter weight in pounds to nearest 10th. e.g. 5.7\n)"
                ">>>"
            )

            description = input(str(
                "Enter an item description.\n"
                ">>>"
            ))

            add_item(item_type, name, style, weight, description)
            inventory_menu()

        if selection == "6":
            print("")
            main_menu()


def print_inventory():
    print("INVENTORY\n\n       BACKPACKS")
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


def add_item(item_type, name, style, weight, description):

    if item_type == "Backpacks" \
            or item_type == "backpacks" \
            or item_type == "Backpack" \
            or item_type == "backpack" \
            or item_type == "1" \
            or item_type == "B" \
            or item_type == "b":
        item_type = "Backpack"
        new_item = Item(item_type, name, style, weight, description)
        backpacks.append(new_item)
    if item_type == "Mattress" \
            or item_type == "mattress" \
            or item_type == "mattresses" \
            or item_type == "Mattresses" \
            or item_type == "2" \
            or item_type == "M" \
            or item_type == "m":
        item_type = "Mattress"
        new_item = Item(item_type, name, style, weight, description)
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
        new_item = Item(item_type, name, style, weight, description)
        sleep_bags.append(new_item)
    if item_type == "Tents" \
            or item_type == "tents" \
            or item_type == "Tent" \
            or item_type == "tent" \
            or item_type == "4" \
            or item_type == "T" \
            or item_type == "t":
        item_type = "Tent"
        new_item = Item(item_type, name, style, weight, description)
        tents.append(new_item)
    # print("\nItem added")


def plan_hike():
    hike_type = input(str(
        "What type/style of hike will you be doing?\n"
        "(Enter string: UL, Heavy, or Day):\n"
        ">>>"
    ))

    packing_list = []

    for item_list in inventory:
        for item in item_list:
            if item._style == hike_type:
                packing_list.append(item)

    print(packing_list)
    with open('hike_list.txt', 'w') as out_file:
        for item in packing_list:
            out_file.write(str(item._item_type) + "\n")
            out_file.write(str(item._name) + "\n")
            out_file.write(str(item._style) + "\n")
            out_file.write(str(item._weight) + "\n")
            out_file.write(str(item._description) + "\n\n")

def convert_txt():

    # 4. This is the microservice provided by my teammate
    with open('converter.txt', 'w') as signal:
        signal.write("True")

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
    def __init__(self, item_type, name, style, weight, description):
        self._item_type = item_type  # Backpack, Tent, Mattress, Sleeping_Bag
        self._name = name  # any
        self._style = style  # UL, Heavy, Day
        self._weight = weight  # float
        self._description = description   # any

    def print_item_info(self):
        print(f"ITEM TYPE:      {self._item_type}\n"
              f"NAME:           {self._name}\n"
              f"HIKING STYLE:   {self._style}\n"
              f"WEIGHT:         {self._weight}\n"
              f"DESCRIPTION:    {self._description}"
              )




add_item("1", "Osprey Exos", "UL", 2.5, "My PCT pack")
add_item("1", "REI", "Heavy", 6.5, "Made his one op")
add_item("2", "BigAgnes Copper Spur", "UL", 2.6, "Broken Zipper")
add_item("2", "REI 4 pax", "Heavy", 8.2, "Car camping")
add_item("3", "REI Magma 15", "UL", 2.2, "Another broken zipper")
add_item("3", "Feathered Friends", "UL", 2.4, "Wish I had one of these")
add_item("4", "POWERLIX SLEEPING PAD", "UL", 1.32, "Seems flimsy")
add_item("4", "Therm-A-Rest", "UL", 2.4, "Too fat for this one")



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





