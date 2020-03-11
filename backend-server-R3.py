# saved as greeting-server.py
import Pyro4


@Pyro4.expose
class GreetingMaker3(object):
    def __init__(self):

        self.all_orders = []
        self.all_menus = [["Alishaan's", {"starters": [("Prawn Cocktail", 5), ("Tomato Soup", 3)], "mains": [
            ("Haddock Florentine", 9), ("Canelloni", 11)], "desert": [("Rasberry Ripple Icecream", 4), ("Cheeseboard", 6)]}], ["Lebeneat", {"starters": [("Wrap", 5), ("Tomato Soup", 3)], "mains": [
                ("Cheese Ball", 9), ("Canelloni", 11)], "desert": [("Icycle", 4), ("Chocolate Sundae", 6)]}]]

    def get_menus(self, name):
        print("Called get_menus(self, name)")
        self.all_orders.append([name, -1, -1, -1])
        print("Have recieved")
        # TODO send an update to all other replicas
        # TODO keep a timestamp
        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R1.update(self.all_orders)
        except:
            pass

        return self.all_menus

    def get_menu(self, n_menu):
        print("Called get_menu(n_menu)", n_menu, self.all_orders[-1][1])
        print(self.all_menus)
        print("Hello")
        self.all_orders[-1][1] = n_menu
        try:
            print("Hello")
            print(self.all_menus[n_menu])
        except:
            print("Not making it")

        print("Hello")

        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R1.update(self.all_orders)
        except:
            pass

        return self.all_menus[n_menu]

    def get_meal(self, order):
        self.all_orders[-1][2] = order
        print("Called get_meal(order)")

        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R1.update(self.all_orders)
        except:
            pass

        return order

    def get_address(self, postcode):
        print("Called get_address(postcode)", postcode)
        self.all_orders[-1][3] = postcode
        # TODO add webservice

        try:
            region = webservice1.get_address(postcode)
        except Exception as e:
            try:
                print(e)
                region = webservice2.get_address(postcode)
            except:
                region = "Unable to find region"
        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R3.update(self.all_orders)
        except:
            pass
        return region

    def confirm(self, confirmation_region, orderid):
        print("Called confirm_address(confirmation)",
              confirmation_region, self.all_orders)
        self.all_orders[-1][3] += " " + confirmation_region
        self.all_orders[-1][4] = orderid
        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R3.update(self.all_orders)
        except:
            pass
        return "Your Order is On its way to " + self.all_orders[-1][3]

    def update(self, data):
        self.all_orders = data
        print("Updating", self.all_orders)

    def past_orders(self, name):
        print("past orders")
        your_orders = []
        for order in self.all_orders:
            if order[0] == name:
                your_orders.append(order)
        result = []
        for order in your_orders:
            c = 0
            delivering = ""
            for course, options in self.all_menus[order[1]][1].items():
                print("past orders")

                delivering += options[order[2][c-1]][0] + "\n "
                c += 1
            print(delivering)
            print("past orders")

            result.insert(0, "Ben your order from " + self.all_menus[order[1]]
                          [0] + " at " + order[4][:19] +
                          " of: \n " + delivering
                          )
        return result


# Other Preplicas
R1 = Pyro4.Proxy("PYRONAME:R1")
R2 = Pyro4.Proxy("PYRONAME:R2")

#

# Websercies
webservice1 = Pyro4.Proxy("PYRONAME:webservice1")
webservice2 = Pyro4.Proxy("PYRONAME:webservice2")
#


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object


instance = GreetingMaker3()
uri = daemon.register(instance)


# register the object with a name in the name server
ns.register("R3", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
