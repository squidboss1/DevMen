import json

dictonary_1 = {"key1" : "value1", "key2" : "value2"}

def reverse(**kwargs):
    dictonary_2 = {}
    for k, v in kwargs.items():
        dictonary_2[v] = k

    return dictonary_2

result = reverse(**dictonary_1)

with open("result.txt", "w", encoding="utf-8") as plik:
    plik.write(json.dumps(result))
    # json.dump(result, plik)
