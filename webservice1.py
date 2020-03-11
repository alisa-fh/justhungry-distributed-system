# saved as greeting-server.py
import Pyro4
import json
import urllib
import urllib.request


@Pyro4.expose
class Webservice(object):
    def __init__(self):
        self.previously_called = {}

    def get_address(self, postcode):
        if postcode in self.previously_called:
            print("Called Before", self.previously_called)
            return self.previously_called[postcode]
        print("Called get_address(postcode)", postcode)
        # TODO add webservice

        j = urllib.request.urlopen(
            'https://api.postcodes.io/postcodes/' + postcode)

        str_response = j.read().decode('utf-8')
        js = json.loads(str_response)

        self.previously_called[postcode] = js["result"]["region"]

        return js["result"]["region"]


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(Webservice)
# register the object with a name in the name server
ns.register("webservice1", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
