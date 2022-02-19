

import requests
import json

def jprint(obj):
    text = json.dump(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://petstore.swagger.io/pet/cat")
print(response.status_code)

jprint(response.json())
