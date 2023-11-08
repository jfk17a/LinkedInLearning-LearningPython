import json

theJSON = open("testing.json")
x = json.load(theJSON)
print(x["users"][1]["name"])