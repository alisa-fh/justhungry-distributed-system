# saved as greeting-server.py
import Pyro4


@Pyro4.expose
class GreetingMaker(object):
    def __init__(self):

        self.all_orders = []
        self.all_menus = [["Alishaan's", {"starters": [("apples", 5), ("pears", 3)], "mains": [
            ("apples", 5), ("pears", 3)], "desert": [("apples", 5), ("pears", 3)]}]]

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
        print("Called get_address(postcode)")
        self.all_orders[-1][3] = postcode
        # TODO add webservice

        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R1.update(self.all_orders)
        except:
            pass

        return ["28 Glebe Rd "]

    def confirm_address(self, confirmation_address):
        print("Called confirm_address(confirmation)")
        self.all_orders[-1][3] += " " + confirmation_address

        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R1.update(self.all_orders)
        except:
            pass

        return "Your Order is On its way"

    def update(self, data):
        self.all_orders = data
        print("Updating", self.all_orders)


# Other Preplicas
R1 = Pyro4.Proxy("PYRONAME:R1")
R2 = Pyro4.Proxy("PYRONAME:R2")

#


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(GreetingMaker)
# register the object with a name in the name server
ns.register("R3", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
