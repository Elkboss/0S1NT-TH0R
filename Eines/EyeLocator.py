##########################
# Author: A              #
#                        # 
# Date: 30.05.2021       #
########################## 

import requests
import json
import colorama
from colorama import Fore, Back, Style
import maigret

username = input('Que vols cercar? --> ')

print(Fore.RED+' RESULTATS DE psbdmp '+Style.RESET_ALL)
print('')
url = 'http://www.psbdmp.ws/api/v3/search/{0}'.format(str(username))
r = requests.get(url)
json_object = json.loads(r.text)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)

print(Fore.RED+' RESULTATS DE Wilby.me '+Style.RESET_ALL)
print()
url2 = 'https://wiby.me/json/?q={0}'.format(str(username))
e = requests.get(url2)
json_object = json.loads(e.text)
json_formatted_st = json.dumps(json_object, indent=2)
print(json_formatted_st)

print(Fore.RED+' RESULTATS DE Social Searcher '+Style.RESET_ALL)
url3 = 'https://api.social-searcher.com/v2/search?q={0}&network=web'.format(str(username))
x = requests.get(url3)
json_object = json.loads(x.text)
json_formatted_s = json.dumps(json_object, indent=2)
print(json_formatted_s)



print(Fore.RED+' Busqueda en Empresa '+Style.RESET_ALL)
url4 = 'https://api.opencorporates.com/v0.4/companies/search?q={0}'.format(str(username)) 
y = requests.get(url4)
json_object = json.loads(y.text)
json_formatted_ = json.dumps(json_object, indent=2)
print(json_formatted_)


print(Fore.RED+' Busqueda en GRAVATAR '+Style.RESET_ALL)
url5 = 'http://en.gravatar.com/{0}.json'.format(str(username)) 
f = requests.get(url5)
json_object = json.loads(f.text)
json_formatted = json.dumps(json_object, indent=2)
print(json_formatted)


