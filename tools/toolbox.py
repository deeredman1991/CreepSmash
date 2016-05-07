import os.path
import shutil
import json

def parseJson(filepath):
    if not str(filepath).split('.')[-1] == 'json':
        filepath = '{}.json'.format(filepath)
    if not os.path.isfile(filepath):
        defaults_filepath = filepath.split('/')
        filename = defaults_filepath.pop(-1)
        defaults_filepath = '{}/.defaults/{}'.format('{}'.join(defaults_filepath), filename)
        shutil.copyfile(defaults_filepath, filepath)
        
    with open(filepath, 'r') as infile:
        jsonData = json.load(infile) 
    return jsonData