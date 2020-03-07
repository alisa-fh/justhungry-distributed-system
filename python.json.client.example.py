import json
import urllib
import urllib.request

j = urllib.request.urlopen('https://api.postcodes.io/postcodes/SW130EA')

str_response = j.read().decode('utf-8')
js = json.loads(str_response)

print(js["result"]["region"])
