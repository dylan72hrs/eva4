import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.104/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("cisco", "cisco123!")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)
response_json = resp.json()
print(json.dumps(response_json, indent=4))