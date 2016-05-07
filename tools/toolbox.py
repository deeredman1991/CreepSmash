import json

def parseJson(filepath):
    with open(filepath, 'r') as infile:
        jsonData = json.load(infile) 
    return jsonData