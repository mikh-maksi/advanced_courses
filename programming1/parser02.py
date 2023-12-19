import urllib.request
import json

url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"

with urllib.request.urlopen(url) as response:
     body_json = response.read()

body_dict = json.loads(body_json)
# user_id = body_dict['userId'] # 1

print(body_dict)
# print(user_id)