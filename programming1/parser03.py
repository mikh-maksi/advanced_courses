import urllib.request
import json


access_key = "6a6aae9cbdb8f85997e56dd40fe081a6"
url = f"http://api.coinlayer.com/live?access_key={access_key}"

with urllib.request.urlopen(url) as response:
     body_json = response.read()

body_dict = json.loads(body_json)
# user_id = body_dict['userId'] # 1

print(body_dict['rates']['BTC'])
# print(user_id)