# The MIT License (MIT)
# 
# Copyright (c) 2016 deeredman1991
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os



class JList(list):
    def __init__(self, filepath_or_parent, *args, **kwargs):
    
        assert (filepath_or_parent)
        
        if type(filepath_or_parent) == type(""):
            if str(filepath_or_parent).split('.')[-1] == 'json':
                self._jpyon_filepath = str(filepath_or_parent)
            else:
                self._jpyon_filepath = str('{}.json'.format(filepath_or_parent))
                
            if os.path.isfile(self._jpyon_filepath):
                super(JList, self).__init__(self.read())
            else:
                super(JList, self).__init__(*args, **kwargs)
                self.write()
        else:
            self._jpyon_parent = filepath_or_parent
            super(JList, self).__init__(*args, **kwargs)
        
    def __getitem__(self, key):
        _item = super(JList, self).__getitem__(key)
        if type(_item) == type({}):
            super(JList, self).__setitem__( key, JDict(self, _item) )
            _item = super(JList, self).__getitem__(key)
        if type(_item) == type([]):
            super(JList, self).__setitem__( key, JList(self, _item) )
            _item = super(JList, self).__getitem__(key)
        if type(_item) == type('') and '.json' in _item and _item != self._jpyon_filepath:
            _item = JPyon(self, parseJson(_item))
        return _item
        
    def __setitem__(self, key, value):
        super(JList, self).__setitem__(key, value)
        self.write()
        
    def __delitem__(self, key):
        super(JList, self).__delitem__(key)
        self.write()
        
    def __setslice__(self, i, j, sequence):
        super(JList, self).__setslice__(i, j, sequence)
        self.write()
    
    def __delslice__(self, i, j):
        super(JList, self).__delslice__(i, j)
        self.write()
        
    def append(self, x):
        super(JList, self).append(x)
        self.write()
        
    def extend(self, L):
        super(JList, self).extend(L)
        self.write()
        
    def insert(self, i, x):
        super(JList, self).insert(i, x)
        self.write()
        
    def remove(self, x):
        super(JList, self).remove(x)
        self.write()
        
    def pop(self, i=0):
        _pop = super(JList, self).pop(i)
        self.write()
        return _pop
        
    def sort(self, cmp=None, key=None, reverse=False):
        _sort = super(JList, self).sort(cmp, key, reverse)
        self.write()
        return _sort
        
    def reverse(self):
        _reverse = super(JList, self).reverse()
        self.write()
        return _reverse
        
    def write(self):
        if hasattr(self, '_jpyon_parent'):
            self._jpyon_parent.write()
        else:
            with open(self._jpyon_filepath, 'w') as outfile:
                _list_copy = self
                for v in _list_copy:
                    if issubclass(type(v), JPyon):
                        _list_copy[_list_copy.index(v)] = v._jpyon_filepath
                json.dump(_list_copy, outfile, sort_keys = True, indent = 4,
                    ensure_ascii=False)
                    
    def read(self):
        if hasattr(self, '_jpyon_parent'):
            return self
        else:
            self = parseJson(self._jpyon_filepath)
            return self

class JDict(dict):
    def __init__(self, filepath_or_parent, dicti={}):
        assert (filepath_or_parent)
        
        if type(filepath_or_parent) == type(""):
            if str(filepath_or_parent).split('.')[-1] == 'json':
                dicti['_jpyon_filepath'] = filepath_or_parent
            else:
                dicti['_jpyon_filepath'] = '{}.json'.format(filepath_or_parent)
                
            if os.path.isfile(dicti['_jpyon_filepath']):
                super(JDict, self).__init__(dict(dicti.items() + parseJson(filepath_or_parent).items()))
            else:
                super(JDict, self).__init__(dicti)
                self.write()
        else:
            dicti['_jpyon_parent'] = filepath_or_parent
            super(JDict, self).__init__(dicti)
            
    def __getitem__(self, key):
        _item = super(JDict, self).__getitem__(key)
        if type(_item) == type({}):
            super(JDict, self).__setitem__( key, JDict(self, _item) )
            _item = super(JDict, self).__getitem__(key)
        if type(_item) == type([]):
            super(JDict, self).__setitem__( key, JList(self, _item) )
            _item = super(JDict, self).__getitem__(key)
        if type(_item) == type(object()):
            super(JDict, self).__setitem__( key, JPyon(self, _item) )
            _item = super(JDict, self).__getitem__(key)
        if type(_item) == type('') and '.json' in _item and _item != super(JDict, self).__getitem__('_jpyon_filepath'):#self['_jpyon_filepath']:
            _item = JPyon(self, parseJson(_item))
        return _item
        
    def __setitem__(self, key, value):
        super(JDict, self).__setitem__(key, value)
        self.write()
        
    def __delitem__(self, key):
        super(JDict, self).__delitem__(key)
        self.write()
        
    def clear(self):
        super(JDict, self).clear()
        self.write()
        
    def fromkeys(self, seq, value=None):
        _fromkeys = super(JDict, self).fromkeys(seq, value)
        self.write()
        return _fromkeys
        
    def pop(self, key, default=object()):
        _pop = super(JDict, self).pop(key, default)
        self.write()
        return _pop
        
    def popitem(self):
        _popitem = super(JDict, self).popitem()
        self.write()
        return _popitem
        
    def setdefault(self, key, default=None):
        _setdefault = super(JDict, self).setdefault(key, default)
        self.write()
        return _setdefault
        
    def update(self, arg=None, **kwargs):
        _update = super(JDict, self).update(arg, **kwargs)
        self.write()
        return _update
        
    def write(self):
        if self.has_key('_jpyon_parent'):
            self['_jpyon_parent'].write()
        else:
            with open(self['_jpyon_filepath'], 'w') as outfile:
                _dict_copy = dict(self)
                for k, v in _dict_copy.iteritems():
                    if issubclass(type(v), JPyon):
                        _dict_copy[k] = v._jpyon_filepath
                        
                if _dict_copy.has_key('_jpyon_filepath'):
                    del _dict_copy['_jpyon_filepath']
                    
                json.dump(_dict_copy, outfile, sort_keys = True, indent = 4,
                    ensure_ascii=False)
                    
    def read(self):
        if self.has_key('_jpyon_parent'):
            return self
        else:
            self = parseJson(self['_jpyon_filepath'])
            return self
            
class JPyon(object):
    def __init__(self, filepath):
        self._jpyon_filepath = filepath
        if os.path.isfile(self._jpyon_filepath):
            self.__dict__ = JDict( self._jpyon_filepath, parseJson(filepath) )
        else:
            self.__dict__ = JDict( self._jpyon_filepath, self.__dict__ )
        
    def __setattr__(self, name, value):
        super(JPyon, self).__setattr__(name, value)
        if hasattr(self.__dict__, 'write'):
            self.__dict__.write()
            
    def __delattr__(self, name):
        super(JPyon, self).__delattr__(name)
        if hasattr(self.__dict__, 'write'):
            self.__dict__.write()
            
def parseJson(filepath):
    with open(filepath, 'r') as infile:
        jsonData = json.load(infile) 
    return jsonData