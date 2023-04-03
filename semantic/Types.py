class IntegerType(object):
    def __init__(self):
        self.name = 'integer'

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class RealType(object):
    def __init__(self):
        self.name = 'real'

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class BooleanType(object):
    def __init__(self):
        self.name = 'boolean'

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class CharType(object):
    def __init__(self):
        self.name = 'char'

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class VoidType(object):
    def __init__(self):
        self.name = 'void'

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class StringType(object):
    def __init__(self):
        self.name = 'string'

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class ArrayType(object):  # 每个实例代表一个数组类型
    def __init__(self, period,
                 type):  # 根据ast_node.py,node.childs=(period, type)
        self.name = 'array'
        self.period = period  # 数组各维度下标范围（起始，终止）：二元组列表
        # 起始和终止又分别是二元组。形如('integer', 1)。既包括类型又包括值。
        self.type = type  # 数组元素类型

    def __str__(self):
        ans = str(self.type)
        for pair in self.period:
            ans += '[' + str(pair[0][1]) + ',' + str(pair[1][1]) + ']'
            # 输出是不输出数组下标的类型
            # pair[0][0]为下标类型，pair[0][1]为下标值
        return ans

    def __repr__(self):
        return str(self)


# TODO 记录类型
class RecordType(object):  # 每个实例代表一个记录类型
    def __init__(self, fields):
        self.fields = fields  # （子成员变量名，类型）：二元组列表


# TODO 指针类型
class PointerType(object):  # 每个实例代表一个指针类型
    def __init__(self, type):
        self.type = type  # 指针指向的类型


class FunctionType(object):  # 每个实例代表一个函数类型
    def __init__(self, type, params):
        self.name = 'function'
        self.type = type  # 返回值类型
        self.params = params  # 参数列表。二元组（是否传引用，类型）：二元组列表

    def __str__(self):
        ans = str(self.type)
        ans += '('
        first = True
        for p in self.params:
            if first:
                first = False
            else:
                ans += ','
            ans += str(p)
        ans += ')'
        return ans

    def __repr__(self):
        return str(self)


class ConstType(object):  # 每个实例代表一个常量类型
    def __init__(self, type, value):
        self.name = 'const'
        self.type = type
        self.value = value

    def __str__(self):
        return 'const ' + str(self.type)

    def __repr__(self):
        return str(self)


class ReferenceType(object):  # 每个实例代表一个引用传参类型
    def __init__(self, type):
        self.name = 'var'
        self.type = type

    def __str__(self):
        return 'var ' + str(self.type)

    def __repr__(self):
        return str(self)
        

class Types(object):
    types = {  # 类型名和类型实例的对应关系
        'integer': IntegerType(),
        'real': RealType(),
        'boolean': BooleanType(),
        'char': CharType(),
        'void': VoidType(),
        'string': StringType()
    }  # 遇到type用户自定义类型时，需要在这里添加F

    # 基于node提取类型
    @classmethod
    def get_type(cls, node):
        if node.type[0] in cls.types.keys(
        ):  # 基本类型/自定义类型。basic_type -> INTEGER | REAL | CHAR | STRING | BOOLEAN
            return cls.types[node.type[0]]
        elif node.type[0] == 'array_type':
            # 数组类型。type -> ARRAY LBRACK period RBRACK OF basic_type
            now = node.childs[0]  # now = period
            lst = []
            for i in range(0, len(now.childs), 2):
                lst.append((now.childs[i].type, now.childs[i + 1].type))

            now = node.childs[1]  # now = basic_type
            return ArrayType(lst, cls.get_type(now))
        elif node.type[0] == 'function_head' or node.type[
                0] == 'procedure_head':
            # 子程序类型。subprogram_head subprogram_head -> PROCEDURE ID formal_parameter
            #                   
            if node.type[0] == 'function_head':
                now = node.childs[1]  # now = basic_type
                return_type = cls.get_type(now)
            elif node.type[0] == 'procedure_head':
                return_type = VoidType()
            lst = []
            now = node.childs[0]
            # now = formal_parameter.formal_parameter -> LPAREN parameter_list RPAREN
            if now is not None:
                now = now.childs[0]
                # now = parameter_list.parameter_list -> parameter_list SEMI parameter | parameter
                for x in now.childs:  # x = value_parameter/var_parameter
                    var_flag = False
                    _x = x
                    if _x.type == 'var_parameter':
                        var_flag = True
                        _x = _x.childs[0]
                    # value_parameter -> idlist COLON basic_type
                    tmp_type = cls.get_type(_x.childs[-1])
                    if var_flag:
                        tmp_type = ReferenceType(tmp_type)
                    for i in range(len(_x.childs) - 1):
                        lst.append(tmp_type)
            return FunctionType(return_type, lst)
        elif node.type[0] == 'const_declaration':
            type = cls.types[node.childs[1].type[0]]  # type = 'integer'
            val = node.childs[1].type[1]  # val = 123
            return ConstType(type, val)
        elif node.type[0] == 'record_type':
            pass  # TODO

    # TODO 用户自定义类型，需要添加到types里
    @classmethod
    def build_type(cls, node):
        pass
