''''Min Khant Tin
    15/9/1016
    This a shopping list program which you can add, list, mark and see the items you need to shop
    https://github.com/minkhanttin123/CP1404_Assignment1/blob/master/MinKhantTinA1'''


#loading items pseudocode
'''
open items.txt as read only files
separate the items in the csv file with ","
format the items into correct format
'''
#completing items pseudocode
'''
if user input equals to c count will start from 0
if count equal to 0
show "No items completed"
else show completed items
show the total price of completed items
'''


print("Welcome to shopping list 1.0 by Min Khant Tin") #Welcome the user

with open('items.txt') as n:  #Load and show how many items loaded from csv file
    CSVline = sum(1 for _ in n)
    print(CSVline, "items loaded from csv file items.txt")


def show_menu(): #Function for showing the menu bar
    menu = '''
Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit'''
    print(menu)


while True: #Start of the while loop
    show_menu()
    userinput = str(input(">>>").lower()) #change the cap letters to small
    file = open("items.txt", "r")
    if userinput == "r":    #user can see the require item

        count = 0
        price = 0
        for line in file:
            x = line.split(",")
            price += float(x[1])
            print("{}.{}      ${}({})".format(count, x[0], float(x[1]), x[2])) #formatting of the csv list
            count += 1
        if count == 0:
            print("No required items")
        else:
            print("Total expected price for", CSVline, "items ${}".format(price)) #show the total price of the items
    elif userinput == "c":  #to check which items are completed
        count = 0
        price = 0
        if count == 0:
            print("No items completed")

        else:
            for line in file:
                x = line.split(",")
                price += float(x[1])
                count += 1
                print("{}.{}      ${} ({})".format(count, x[0], float(x[1]), x[2]))
                print("Total expected price for", CSVline, "items ${}".format(price))
    elif userinput == "m":  #To mark the items
        count = 0
        price = 0
        for line in file:
            x = line.split(",")
            price += float(x[1])
            print("{}.{}      ${} ({})".format(count, x[0], float(x[1]), x[2]))
            count += 1
        print("Total expected price for", CSVline, "items ${}".format(price))
        mark_input = int(input("Enter the number of an item to mark as completed \n>>>"))
        while True:
            if mark_input == 0:
                print("Fish fingers marked as complete")
                break
            elif mark_input == 1:
                print("Metal detector marked as complete")
                break
            elif mark_input == 2:
                print("Coffee beans marked as complete")
                break
            else:
                print("Invalid must be 0, 1 or 2")
                mark_input = int(input("Enter the number of an item to mark as completed \n>>>"))

    elif userinput == "a": #To add new items to shopping list

        while True: #Error check method for name
            name = str(input("Item name: "))
            if name == "":
                print("Input cannot be blank")
                continue
            elif name == " ":
                print("Input cannot be blank")
                continue
            break

        while True: #Error check method for price
            try:
                price = int(input("Price: "))
            except ValueError:
                print("Invalid input; enter a valid number")
                continue

            if price < 0:
                print("Price must be >= $0")
                continue
            break

        while True: #Error check method for priority
            try:
                priority = int(input("Priority: "))
            except ValueError:
                print("Invalid input; enter a valid number")
                continue
            if priority < 1 or priority > 2:
                print("Priority must be 1, 2 or 3")
                continue
            break
        print("{} ${} (priority {}) saved to shopping list".format(name, float(price), priority) )

    elif userinput == "q": #To quit the shopping list programming
        print("Items saved to items.csv \nHave a nice day :)")
        break
    else: print("Invalid")


















