class Item(object):
    def __init__(self, name, value):
        pass


class SymbolTable(object):
    def __init__(self):
        self._table = {}

    def setitem(self, name, value):
        self._table[name] = value

    def getitem(self, name):
        return self._table[name]

    def contains(self, name):
        return name in self._table
