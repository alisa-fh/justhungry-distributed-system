# saved as greeting-server.py
import Pyro4


@Pyro4.expose
class GreetingMaker(object):

    def get_menus(self, name):
        try:
            print("R1")
            return R1.get_menus(name)
        except:
            try:
                print("R2")
                return R2.get_menus(name)
            except:
                try:
                    print("R3")
                    return R3.get_menus(name)
                except:
                    return "No Backup Servers to get_menus(name)"

    def get_menu(self, n_menu):
        try:
            print("R1")
            return R1.get_menu(n_menu)
        except:
            try:
                print("R2")
                return R2.get_menu(n_menu)
            except:
                try:
                    print("R3")
                    return R3.get_menu(n_menu)
                except:
                    return "No Backup Servers to get_menu(n_menu)"

    def get_meal(self, order):

        try:
            print("R1")
            return R1.get_meal(order)
        except:
            try:
                print("R2")
                return R2.get_meal(order)
            except:
                try:
                    print("R3")
                    return R3.get_meal(order)
                except:
                    return "No Backup Servers to get_meal(order)"

    def get_address(self, postcode):

        try:
            print("R1")
            return R1.get_address(postcode)
        except:
            try:
                print("R2")
                return R2.get_address(postcode)
            except:
                try:
                    print("R3")
                    return R3.get_address(postcode)
                except:
                    return "No Backup Servers to get_address(postcode)"

    def confirm(self, confirmation):

        try:
            print("R1")
            return R1.confirm(confirmation)
        except:
            try:
                print("R2")
                return R2.confirm(confirmation)
            except:
                try:
                    print("R3")
                    return R3.confirm(confirmation)
                except:
                    return "No Backup Servers to confirm_address(postcode)"


# Register the Backend Replicas
R1 = Pyro4.Proxy("PYRONAME:R1")
R2 = Pyro4.Proxy("PYRONAME:R2")
R3 = Pyro4.Proxy("PYRONAME:R3")

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(GreetingMaker)
# register the object with a name in the name server
ns.register("example.greeting", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
