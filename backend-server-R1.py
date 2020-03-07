# saved as greeting-server.py
import urllib
import urllib.request
import Pyro4
import json


@Pyro4.expose
class GreetingMaker1(object):
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
            R3.update(self.all_orders)
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
            R3.update(self.all_orders)
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
            R3.update(self.all_orders)
        except:
            pass
        return order

    def get_address(self, postcode):
        print("Called get_address(postcode)", postcode)
        self.all_orders[-1][3] = postcode
        # TODO add webservice

        j = urllib.request.urlopen(
            'https://api.postcodes.io/postcodes/' + postcode)

        str_response = j.read().decode('utf-8')
        js = json.loads(str_response)

        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R3.update(self.all_orders)
        except:
            pass
        return js["result"]["region"]

    def confirm(self, confirmation_region):
        print("Called confirm_address(confirmation)")
        self.all_orders[-1][3] += " " + confirmation_region

        try:
            R2.update(self.all_orders)
        except:
            pass
        try:
            R3.update(self.all_orders)
        except:
            pass
        return "Your Order of cost" + "is On its way to " + self.all_orders[-1][3]

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

            result = ["Ben your order from " + self.all_menus[order[1]]
                      [0] + " of: \n " + delivering
                      ]
        print(result)
        return result

    def update(self, data):
        self.all_orders = data
        print("Updating", self.all_orders)


# Other Preplicas
R2 = Pyro4.Proxy("PYRONAME:R2")
R3 = Pyro4.Proxy("PYRONAME:R3")
#

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(GreetingMaker1)
# register the object with a name in the name server
ns.register("R1", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
