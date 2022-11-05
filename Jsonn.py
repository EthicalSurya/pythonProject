import json

data='{"var1":"Surya","var2":56}'
print(data)

parsed=json.loads(data)
print(parsed['var1'])

# print(json.load(parsed))
#_________________________________Dumps___________________________
data2={
    "Dippam":"donga",
    "choco":["dairymilk","5star","munch"],
    "food":("gupchup","chaat","dahipuri"),
    "isbad":False
}

js=json.dumps(data2)
print(js)
