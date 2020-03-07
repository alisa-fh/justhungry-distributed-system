import Pyro4


# use name server object lookup uri shortcut
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")


name = input("What is your name? ").strip()
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
        "That was not an option\nIs this your Region?[y/n] ").strip()
    if confirmation == 'y' or confirmation == 'n':
        break
if confirmation == "y":
    print(greeting_maker.confirm(region))  # Returns your full order
else:
    corrected_region = input("What is your region then? ").strip()
    print(greeting_maker.confirm(corrected_region))  # Returns your full order
