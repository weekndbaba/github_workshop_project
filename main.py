import json

CONFIG = {}

with open('config.json','r') as f:
    CONFIG = json.load(f)


message = f"Hello {CONFIG.get('name','John')}"

if(CONFIG.get('age',18) >= 18):
    message += ", You are allowed on this website"

else:
    message += ", You are not allowed on this website"

print(message)
