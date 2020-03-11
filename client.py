import Pyro4
from datetime import datetime


# use name server object lookup uri shortcut
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")


while True:
    name = input("Welcome to Just Hungry! What is your name? ").strip()

    while True:
        choice = input(
            "Would you like to see your pastorders or create a new one?[past/new] ").strip()
        if choice == 'past':
            your_orders = greeting_maker.past_orders(name)
            for order in your_orders:
                print(order)
            break
        if choice == 'new':
            all_menus = greeting_maker.get_menus(name)
            print(" Here are all the restaurants near you!")
            for c, i in enumerate(all_menus):
                print("{}. {}".format(c + 1, i[0]))

            # Get names of restaurants

            print("\n\n")
            while True:
                try:
                    n_menu = int(
                        input("Which restaurants menu do you want? ").strip())
                except:
                    print("please input an integer")
                else:
                    if n_menu <= len(all_menus) and n_menu > 0:
                        break
                    else:
                        print(
                            "Please input a menu within the correct range of menus")

            #         self.all_menus = [["Alishaan's", {"starters": [("apples", 5), ("pears", 3)], "mains": [
            # ("apples", 5), ("pears", 3)], "desert": [("apples", 5), ("pears", 3)]}]]

            chosen_menu = greeting_maker.get_menu(n_menu - 1)
            print("Menu for {} \n------------ \n\n".format(chosen_menu[0]))
            for course, options in chosen_menu[1].items():
                print("\n {}".format(course))
                c = 0
                for j in options:
                    print('{}) {:^25} £{}'.format(c, j[0], j[1]))

                    c += 1

            # Get send the Menu Back

            while True:
                try:
                    starter = int(
                        input("What is your starter? (number) ").strip())

                except:
                    print("please input an integer")
                else:
                    if starter <= 1 and starter >= 0:
                        break
                    else:
                        print(
                            "Please input a option within the correct range of options")

            while True:
                try:
                    main = int(input("What is your main? (number)").strip())

                except:
                    print("please input an integer")
                else:
                    if main <= 1 and main >= 0:
                        break
                    else:
                        print(
                            "Please input a option within the correct range of options")

            while True:
                try:
                    desert = int(
                        input("What is your desert? (number)").strip())

                except:
                    print("please input an integer")
                else:
                    if desert <= 1 and desert >= 0:
                        break
                    else:
                        print(
                            "Please input a option within the correct range of options")

            greeting_maker.get_meal([starter, main, desert])
            # Returns cost of the meal

            postcode = input("What is your Postcode? ").strip()
            region = greeting_maker.get_address(postcode)
            print("Is your postcode in this region?: ",
                  region)
            # Returns a list of Full Addresses

            while True:
                confirmation = input(
                    "Is this your Region?[y/n] ").strip()
                if confirmation == 'y' or confirmation == 'n':
                    break
                print("That was not an option\n")
            if confirmation == "y":
                # Returns your full order
                now = datetime.now()
                current_time = str(now)

                print(greeting_maker.confirm(region, current_time + postcode))
            else:
                corrected_region = input("What is your region then? ").strip()
                # Returns your full order
                now = datetime.now()
                current_time = str(now)

                print(greeting_maker.confirm(
                    corrected_region, current_time + postcode))
            break

        print("That was not an option\n")
