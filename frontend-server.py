# saved as greeting-server.py
import Pyro4
import sys
import os


@Pyro4.expose
class GreetingMaker(object):

    def get_menus(self, name):
        try:
            print("R1")
            return R1.get_menus(name)
        except Exception as e:
            print(e)
            try:
                print("R2")
                return R2.get_menus(name)
            except Exception as e:
                print(e)
                try:
                    print("R3")
                    return R3.get_menus(name)
                except Exception as e:
                    print(e)
                    return "No Backup Servers to get_menus(name)"

    def get_menu(self, n_menu):
        try:
            print("R1")
            return R1.get_menu(n_menu)
        except Exception as e:
            print(e)
            try:
                print("R2")
                return R2.get_menu(n_menu)
            except Exception as e:
                print(e)
                try:
                    print("R3")
                    return R3.get_menu(n_menu)
                except Exception as e:
                    print(e)
                    return "No Backup Servers to get_menu(n_menu)"

    def get_meal(self, order):

        try:
            print("R1")
            return R1.get_meal(order)
        except Exception as e:
            print(e)
            try:
                print("R2")
                return R2.get_meal(order)
            except Exception as e:
                print(e)
                try:
                    print("R3")
                    return R3.get_meal(order)
                except Exception as e:
                    print(e)
                    return "No Backup Servers to get_meal(order)"

    def get_address(self, postcode):

        try:
            print("R1")
            return R1.get_address(postcode)
        except Exception as e:
            print(e)
            try:
                print("R2")
                return R2.get_address(postcode)
            except Exception as e:
                print(e)
                try:
                    print("R3")
                    return R3.get_address(postcode)
                except Exception as e:
                    print(e)
                    return "No Backup Servers to get_address(postcode)"

    def confirm(self, confirmation, orderid):

        try:
            print("R1")
            return R1.confirm(confirmation, orderid)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(
                exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            try:
                print("R2")
                return R2.confirm(confirmation, orderid)
            except Exception as e:
                print(e)
                try:
                    print("R3")
                    return R3.confirm(confirmation, orderid)
                except Exception as e:
                    print(e)
                    return "No Backup Servers to confirm_address(postcode)"

    def past_orders(self, confirmation):

        try:
            print("R1")
            return R1.past_orders(confirmation)
        except Exception as e:
            print(e)
            try:
                print("R2")
                return R2.past_orders(confirmation)
            except Exception as e:
                print(e)
                try:
                    print("R3")
                    return R3.past_orders(confirmation)
                except Exception as e:
                    print(e)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(
                        exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    return "No Backup Servers to show past orders"


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
