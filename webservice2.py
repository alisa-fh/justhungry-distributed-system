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

            return self.previously_called[postcode]

        print("Called get_address(postcode)", postcode)
        # TODO add webservice

        j = urllib.request.urlopen(
            'http://api.getthedata.com/postcode/' + postcode)

        str_response = j.read().decode('utf-8')
        js = json.loads(str_response)

        if js["status"] != "match":
            raise ValueError("There was no match for this postcode")
        self.previously_called[postcode] = js["result"]["region"]

        webservice1.update(self.previously_called)

        return js["data"]["country"]

    def update(self, data):
        self.previously_called = data


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(Webservice)
# register the object with a name in the name server
ns.register("webservice2", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()


# Websercies
webservice1 = Pyro4.Proxy("PYRONAME:webservice1")
#
