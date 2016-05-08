import json
import os.path

class JDict(dict):
    def __init__(self, filepath, *args, **kwargs):
        assert filepath
        
        if str(filepath).split('.')[-1] == 'json':
            self.filepath = str(filepath)
        else:
            self.filepath = str('{}.json'.format(filepath))
            
        if os.path.isfile(self.filepath):
            super(JDict, self).__init__(self.read())
        else:
            super(JDict, self).__init__(*args, **kwargs)
            self.write()
        
    def __setitem__(self, key, value):
        assert key
        assert value
        
        dict.__setitem__(self, key, value)
        self.write()
      
    def write(self):
        with open(self.filepath, 'w') as outfile:
            json.dump(self, outfile, sort_keys = True, indent = 4,
                ensure_ascii=False)
        
    def read(self):
        with open(self.filepath, 'r') as infile:
            jsonData = json.load(infile)
        self = jsonData
        return self