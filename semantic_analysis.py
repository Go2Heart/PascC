import pparser


class BasicTypes(object):
    interger = 'integer'
    real = 'real'
    boolean = 'boolean'
    char = 'char'
    void = 'void'
    string = 'string'


class ArrayType(object):

    def __init__(self, period, type):  # node.childs=(period, type)
        self.period = period
        self.type = type


# TODO 记录类型
class RecordType(object):

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size


# TODO 函数类型(认为过程类型返回void)
class FunctionType(object):

    def __init__(self, name, type, params, size):
        self.name = name
        self.type = type
        self.params = params
        self.size = size


class Types(object):
    types = {
        'integer': BasicTypes.interger,
        'real': BasicTypes.real,
        'boolean': BasicTypes.boolean,
        'char': BasicTypes.char,
        'void': BasicTypes.void,
        'string': BasicTypes.string
    }  # 遇到type用户自定义类型时，需要在这里添加

    # 获取一个node的类型
    def get_type(cls, node):
        if node.type[0] in cls.types.keys():
            return cls.types[node.type[0]]
        elif node.type[0] == 'array_type':
            now = node.childs[0]
            lst = []
            for i in range(0, len(now.children), 2):
                lst.append(
                    (now.children[i].type[1], now.children[i + 1].type[1]))

            now = node.childs[1]
            return ArrayType(lst, cls.get_type(now.type))
        elif node.type[0] == 'record_type':
            pass  # TODO
        elif node.type[0] == 'subprogram':
            pass  # TODO

    # TODO 用户自定义类型，需要添加到types里
    def build_type(cls,node):
        pass 


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


class SemanticAnalyzer(object):

    def init(self, parser):
        self.parser = parser

    def analyze(self, script):
        node = self.parser.parse(script)

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Number(self, node):
        node.value = float(node.value)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        self.visit(node.expr)
