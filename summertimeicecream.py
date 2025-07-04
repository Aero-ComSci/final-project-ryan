total_price = []
order = []
order_Options = []
icecream_menu = ["vanilla", "choclate", "oil"]
toppings_menu = ["sprinkles", "gummies", "bolts"]
freesummergiveaway_menu = ["electric bike", "GeForce RTX 5090", "Birthday card"]


def Reset():
    global total_price, order, order_Options, icecream_menu, freesummergiveaway_menu, toppings_menu
    total_price = []
    order = []
    order_Options = []
    icecream_menu = ["vanilla", "choclate", "oil"]
    toppings_menu = ["sprinkles", "gummies", "bolts"]
    freesummergiveaway_menu = ["electric bike", "GeForce RTX 5090", "Birthday card"]
    iceCream()
    Toppings()
    Free_summer_giveaway()


def iceCream():
    global iceCream_userInput, iceCream_amount, iceCream_option
    iceCream_option = input("Do you want ice cream (yes or no):")
    if iceCream_option == "reset":
        print("\nYou have reset your order.")
        Reset()
    if iceCream_option == "yes":
        order_Options.append(iceCream_option)
        print("\nWhich ice cream flavour do you want: ")
        for each in icecream_menu:
            print(each)
        iceCream_userInput = input("Type here: ")
        if iceCream_userInput == "reset":
            print("\nYou have reset your order.")
            Reset()

        while iceCream_userInput not in icecream_menu:
            print("\nThat is not an option. Choose from above")
            for each in icecream_menu:
                print(each)
            iceCream_userInput = input("Type here: ")
            if iceCream_userInput == "reset":
                print("\nYou have reset your order.")
                Reset()

        if iceCream_userInput == "vanilla":
            order.append("vanilla")
            while True:
                try:
                    iceCream_amount = input("How many vanilla ice cream scoops do you want: ")
                    if iceCream_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    iceCream_amount = int(iceCream_amount)
                    if iceCream_amount > 0:
                        total_price.append(5.25 * iceCream_amount)
                        break
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Please input an integer.")
        elif iceCream_userInput == "choclate":
            order.append("choclate")
            while True:
                try:
                    iceCream_amount = input("How many choclate ice cream scoops do you want: ")
                    if iceCream_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    iceCream_amount = int(iceCream_amount)
                    if iceCream_amount > 0:
                        total_price.append(6.25 * iceCream_amount)
                        break
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Please input an integer.")
        elif iceCream_userInput == "oil":
            order.append("oil")
            while True:
                try:
                    iceCream_amount = input("How many oil ice cream scoops do you want: ")
                    if iceCream_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    iceCream_amount = int(iceCream_amount)
                    if iceCream_amount > 0:
                        total_price.append(5.25 * iceCream_amount)
                        break
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Please input an integer.")
    elif iceCream_option == "no":
        order_Options.append("no")
        order.append("no")
        iceCream_amount = ""
        print()
    else:
        print("\nThat is not an option")
        iceCream()


def Toppings():
    global Toppings_userInput, Toppings_amount, Toppings_option
    Toppings_option = input("Do you want toppings (yes or no):")
    if Toppings_option == "reset":
        print("\nYou have reset your order.")
        Reset()
    if Toppings_option == "yes":
        order_Options.append("yes")
        print("\nWhich topping do you want: ")
        for each in toppings_menu:
            print(each)
        Toppings_userInput = input("Type here: ")
        if Toppings_userInput == "reset":
            print("\nYou have reset your order.")
            Reset()

        while Toppings_userInput not in toppings_menu:
            print("\nThat is not an option. Choose from above")
            for each in toppings_menu:
                print(each)
            Toppings_userInput = input("Type here: ")
            if Toppings_userInput == "reset":
                print("\nYou have reset your order.")
                Reset()

        if Toppings_userInput == "sprinkles":
            order.append("sprinkles")
            while True:
                try:
                    Toppings_amount = input("How many servings of sprinkles do you want: ")
                    if Toppings_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    Toppings_amount = int(Toppings_amount)
                    if Toppings_amount > 0:
                        total_price.append(0.50 * Toppings_amount)
                        break
                    else:
                        print("Please input a positive integer.")
                except ValueError:
                    print("Please input an integer.")
        elif Toppings_userInput == "gummies":
            order.append("gummies")
            while True:
                try:
                    Toppings_amount = input("How many servings of gummies do you want: ")
                    if Toppings_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    Toppings_amount = int(Toppings_amount)
                    if Toppings_amount > 0:
                        total_price.append(1.00 * Toppings_amount)
                        break
                    else:
                        print("Please input a positive integer.")
                except ValueError:
                    print("Please input an integer.")
        elif Toppings_userInput == "bolts":
            order.append("bolts")
            while True:
                try:
                    Toppings_amount = input("How many servings of bolts do you want: ")
                    if Toppings_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    Toppings_amount = int(Toppings_amount)
                    if Toppings_amount > 0:
                        total_price.append(5.00 * Toppings_amount)
                        break
                    else:
                        print("Please input a positive integer.")
                except ValueError:
                    print("Please input an integer.")
    elif Toppings_option == "no":
        order_Options.append("no")
        order.append("no")
        Toppings_amount = ""
        print()
    else:
        print("\nThat is not an option")
        Toppings()


def Free_summer_giveaway():
    global Free_summer_giveaway_userInput, Free_summer_giveaway_amount, Free_summer_giveaway_option
    Free_summer_giveaway_option = input("Do you want a free summer gift (yes or no):")
    if Free_summer_giveaway_option == "reset":
        print("\nYou have reset your order.")
        Reset()
    if Free_summer_giveaway_option == "yes":
        order_Options.append("yes")
        print("\nWhich summer gift do you want for free: ")
        for each in freesummergiveaway_menu:
            print(each)
        Free_summer_giveaway_userInput = input("Type here: ")
        if Free_summer_giveaway_userInput == "reset":
            print("\nYou have reset your order.")
            Reset()

        while Free_summer_giveaway_userInput not in freesummergiveaway_menu:
            print("\nThat is not an option. Choose from above")
            for each in freesummergiveaway_menu:
                print(each)
            Free_summer_giveaway_userInput = input("Type here: ")
            if Free_summer_giveaway_userInput == "reset":
                print("\nYou have reset your order.")
                Reset()

        if Free_summer_giveaway_userInput == "electric bike":
            while True:
                Free_summer_giveaway_userInput_Upgrade = input("Do you want to get a birthday card instead (yes or no): ")
                if Free_summer_giveaway_userInput_Upgrade == "reset":
                    print("\nYou have reset your order.")
                    Reset()
                if Free_summer_giveaway_userInput_Upgrade == "yes":
                    order.append("Birthday card")
                    while True:
                        try:
                            Free_summer_giveaway_amount = input("How many birthday cards do you want: ")
                            if Free_summer_giveaway_amount == "reset":
                                print("\nYou have reset your order.")
                                Reset()
                            Free_summer_giveaway_amount = int(Free_summer_giveaway_amount)
                            if Free_summer_giveaway_amount > 0:
                                total_price.append(0.00 * Free_summer_giveaway_amount)
                                break
                            else:
                                print("Please input a positive integer.")
                        except ValueError:
                            print("Please input an integer.")
                    break
                elif Free_summer_giveaway_userInput_Upgrade == "no":
                    order.append("electric bike")
                    while True:
                        try:
                            Free_summer_giveaway_amount = input("How many electric bikes do you want: ")
                            if Free_summer_giveaway_amount == "reset":
                                print("\nYou have reset your order.")
                                Reset()
                            Free_summer_giveaway_amount = int(Free_summer_giveaway_amount)
                            if Free_summer_giveaway_amount > 0:
                                total_price.append(0.00 * Free_summer_giveaway_amount)
                                break
                            else:
                                print("Please input a positive integer.")
                        except ValueError:
                            print("Please input an integer.")
                    break
                else:
                    print("\nPlease input a valid option:")
        elif Free_summer_giveaway_userInput == "GeForce RTX 5090":
            order.append("GeForce RTX 5090")
            while True:
                try:
                    Free_summer_giveaway_amount = input("How many GeForce RTX 5090 do you want: ")
                    if Free_summer_giveaway_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    Free_summer_giveaway_amount = int(Free_summer_giveaway_amount)
                    if Free_summer_giveaway_amount > 0:
                        total_price.append(0.00 * Free_summer_giveaway_amount)
                        break
                    else:
                        print("Please input a positive integer.")
                except ValueError:
                    print("Please input an integer.")
        elif Free_summer_giveaway_userInput == "Birthday card":
            order.append("Birthday card")
            while True:
                try:
                    Free_summer_giveaway_amount = input("How many Birthday cards do you want: ")
                    if Free_summer_giveaway_amount == "reset":
                        print("\nYou have reset your order.")
                        Reset()
                    Free_summer_giveaway_amount = int(Free_summer_giveaway_amount)
                    if Free_summer_giveaway_amount > 0:
                        total_price.append(0.00 * Free_summer_giveaway_amount)
                        break
                    else:
                        print("Please input a positive integer.")
                except ValueError:
                    print("Please input an integer.")
    elif Free_summer_giveaway_option == "no":
        order_Options.append("no")
        order.append("no options")
        Free_summer_giveaway_amount = ""
        print()
    else:
        print("\nThat is not an option")
        Free_summer_giveaway()


iceCream()
Toppings()
Free_summer_giveaway()

print("\n\nYour total is: " + "{:.2f}".format(sum(total_price)))
print("You have ordered: " + str(iceCream_amount) + " " + order[0] + " ice cream scoops, " + str(Toppings_amount) + " " + order[1] + " servings, and " + str(Free_summer_giveaway_amount) + " " + order[2] + " out of the free gifts")
