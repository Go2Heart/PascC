class BasicTypes(object):  # 每个静态成员代表一个基本类型
    interger = 'integer'
    real = 'real'
    boolean = 'boolean'
    char = 'char'
    void = 'void'
    string = 'string'


class ArrayType(object):  # 每个实例代表一个数组类型
    def __init__(self, period,
                 type):  # 根据ast_node.py,node.childs=(period, type)
        self.period = period  # 数组各维度下标范围（起始，终止）：二元组列表
        self.type = type  # 数组元素类型

    def __str__(self):
        ans = str(self.type)
        for pair in self.period:
            ans += '[' + str(pair[0]) + ',' + str(pair[1]) + ']'
        return ans


# TODO 记录类型
class RecordType(object):  # 每个实例代表一个记录类型
    def __init__(self, fields):
        self.fields = fields  # （子成员变量名，类型）：二元组列表


# TODO 指针类型
class PointerType(object):  # 每个实例代表一个指针类型
    def __init__(self, type):
        self.type = type # 指针指向的类型


class FunctionType(object):  # 每个实例代表一个函数类型
    def __init__(self, type, params):
        self.type = type  # 返回值类型
        self.params = params  # 参数列表（是否传引用，类型）：二元组列表

    def __str__(self):
        ans = str(self.type)
        ans += '('
        first = True
        for pair in self.params:
            if first:
                first = False
            else:
                ans += ','
            if pair[0]:
                ans += 'var '
            ans += str(pair[1])
        ans += ')'
        return ans

class ConstType(object):  # 每个实例代表一个常量类型
    def __init__(self, type, value):
        self.type = type
        self.value = value
class Types(object):
    types = {  # 类型名和类型实例的对应关系
        'integer': BasicTypes.interger,
        'real': BasicTypes.real,
        'boolean': BasicTypes.boolean,
        'char': BasicTypes.char,
        'void': BasicTypes.void,
        'string': BasicTypes.string
    }  # 遇到type用户自定义类型时，需要在这里添加

    # 获取一个node的类型
    def get_type(cls, node):
        if node.type[0] in cls.types.keys(
        ):  # 基本类型/自定义类型。basic_type -> INTEGER | REAL | CHAR | STRING | BOOLEAN
            return cls.types[node.type[0]]
        elif node.type[0] == 'array_type':
            # 数组类型。type -> ARRAY LBRACK period RBRACK OF basic_type
            now = node.childs[0]  # now = period
            lst = []
            for i in range(0, len(now.childs), 2):
                lst.append(
                    (now.childs[i].type[1], now.childs[i + 1].type[1]))

            now = node.childs[1]  # now = basic_type
            return ArrayType(lst, cls.get_type(now))
        elif node.type[0] == 'function_head' or node.type[
                0] == 'procedure_head':
            # 子程序类型。subprogram_head subprogram_head -> PROCEDURE ID formal_parameter
            #                                              | FUNCTION ID formal_parameter COLON basic_type
            if node.type[0] == 'function_head':
                now = node.childs[1]  # now = basic_type
                return_type = cls.get_type(now)
            elif node.type[0] == 'procedure_head':
                return_type = BasicTypes.void
            now = node.childs[0]
            # now = formal_parameter.formal_parameter -> LPAREN parameter_list RPAREN
            now = now.childs[0]
            # now = parameter_list.parameter_list -> parameter_list SEMI parameter | parameter
            lst = []
            for x in now.childs:  # x = value_parameter/variable_parameter
                var_flag = False
                if x.type == 'variable_parameter':
                    var_flag = True
                    x = x.childs[0]
                # value_parameter -> idlist COLON basic_type
                tmp_type = cls.get_type(x.childs[-1])
                for i in range(len(x.childs) - 1):
                    lst.append((var_flag, tmp_type))
            return FunctionType(return_type, lst)
        elif node.type[0] == 'const_declaration':
            type = cls.types[node.childs[1].type[0]]  # type = 'integer'
            val = node.childs[1].type[1]  # val = 123
            return ConstType(type, val)
        elif node.type[0] == 'record_type':
            pass  # TODO

    # TODO 用户自定义类型，需要添加到types里
    def build_type(cls, node):
        pass
