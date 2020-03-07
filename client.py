import Pyro4


# use name server object lookup uri shortcut
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")


while True:
    name = input("What is your name? ").strip()

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
            n_menu = int(input("Which restaurants menu do you want? ").strip())

            #         self.all_menus = [["Alishaan's", {"starters": [("apples", 5), ("pears", 3)], "mains": [
            # ("apples", 5), ("pears", 3)], "desert": [("apples", 5), ("pears", 3)]}]]

            chosen_menu = greeting_maker.get_menu(n_menu - 1)
            print("Menu for {} \n------------ \n\n".format(chosen_menu[0]))
            for course, options in chosen_menu[1].items():
                print("\n {}".format(course))
                c = 0
                for j in options:
                    c += 1
                    print("{}. {} \t|\t£{}".format(c, j[0], j[1]))
            #  1. {} Price: {} 2. {} Price: {} 3 {} Price: {} \n\n Main\n------------\n\n 1. {} Price: {} 2. {} Price: {} 3 {} Price: {} \n\n Desert\n------------\n\n 1. {} Price: {} 2. {} Price: {} 3 {} Price: {}"
                #   .format(chosen_menu[0], chosen_menu[1]["starters"][0][0], chosen_menu[1]["starters"][0][]))

            # Get send the Menu Back

            starter = int(input("What is your starter? ").strip())
            main = int(input("What is your main? ").strip())
            desert = int(input("What is your desert? ").strip())

            print(greeting_maker.get_meal([starter, main, desert]))
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
                print(greeting_maker.confirm(region))
            else:
                corrected_region = input("What is your region then? ").strip()
                # Returns your full order
                print(greeting_maker.confirm(corrected_region))
            break

        print("That was not an option\n")
