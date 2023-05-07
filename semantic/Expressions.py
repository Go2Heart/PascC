import logging

from semantic.Types import IntegerType, BooleanType, RealType


class Expression(object):
    def __init__(self, node, symboltable, typestable):
        # node = expression
        self.name = 'expression'
        # node.print()
        if len(node.childs) == 3:
            self.child_cnt = 2
            self.childs = [
                SimpleExpression(node.childs[0], symboltable, typestable),
                SimpleExpression(node.childs[2], symboltable, typestable)
            ]
            self.operator = node.childs[1]
            # '=' | '<>' | '<' | '<=' | '>' | '>='
            typeA = self.childs[0].type.name
            if typeA=='const':
                typeA=self.childs[0].type.type.name
            typeB = self.childs[1].type.name
            if typeB=='const':
                typeB=self.childs[1].type.type.name
            if (typeA == 'integer' and typeB=='real') or (typeA=='real' and typeB=='integer'):
                print("WARNING: Line {0} : 隐式类型转换从 'integer' 到 'real'".format(node.type[1]))
            elif typeA!=typeB:
                print("Line {0} : 左右表达式不能进行大小比较".format(node.type[1]))
            self.type=BooleanType()
        else:
            self.child_cnt = 1
            self.childs = [
                SimpleExpression(node.childs[0], symboltable, typestable)
            ]
            self.operator = None
            self.type = self.childs[0].type

    def __str__(self):
        operator = self.operator
        if operator == '=':
            operator = '=='
        elif operator == '<>':
            operator = '!='
        if self.child_cnt == 1:
            return str(self.childs[0])
        else:
            return str(self.childs[0]) + ' ' + operator + ' ' + str(
                self.childs[1])


class SimpleExpression(object):
    def __init__(self, node, symboltable, typestable):
        # node = simple_expression
        self.name = 'simple_expression'
        if len(node.childs) == 3:
            self.child_cnt = 2
            self.childs = [
                SimpleExpression(node.childs[0], symboltable, typestable),
                Term(node.childs[2], symboltable, typestable)
            ]
            self.operator = node.childs[1]
            # '+' | '-' | 'or'

            typeA = self.childs[0].type.name
            if typeA=='const':
                typeA=self.childs[0].type.type.name
            typeB = self.childs[1].type.name
            if typeB=='const':
                typeB=self.childs[1].type.type.name
            if self.operator == 'or':
                if not (typeA == 'boolean' and typeB == 'boolean'):
                    print("Line {0} : OR运算的运算数不是boolean类型".format(node.type[1]))
                    self.type = BooleanType()
                else:
                    self.type = self.childs[0].type
            else:
                if typeA == 'integer' and typeB == 'real':
                    print("WARNING: Line {0} : 隐式类型转换从 'integer' 到 'real'".format(node.type[1]))
                    self.type = self.childs[1].type
                elif typeA == 'real' and typeB == 'integer':
                    print("WARNING: Line {0} : 隐式类型转换从 'integer' 到 'real'".format(node.type[1]))
                    self.type = self.childs[0].type
                elif (typeA == 'real' and typeB == 'real') or (typeA == 'integer' and typeB == 'integer'):
                    self.type = self.childs[0].type
                else:
                    print("Line {0} : 加减运算的运算数不是整数或者实数类型".format(node.type[1]))
                    self.type = RealType()



        else:
            self.child_cnt = 1
            self.childs = [Term(node.childs[0], symboltable, typestable)]
            self.operator = None
            self.type = self.childs[0].type

    def __str__(self):
        operator = self.operator
        if operator == 'or':
            operator = '||'
        if self.child_cnt == 1:
            return str(self.childs[0])
        else:
            return str(self.childs[0]) + ' ' + operator + ' ' + str(
                self.childs[1])


class Term(object):
    def __init__(self, node, symboltable, typestable):
        # node = term
        self.name = 'term'
        if len(node.childs) == 3:
            self.child_cnt = 2
            self.childs = [
                Term(node.childs[0], symboltable, typestable),
                Factor(node.childs[2], symboltable, typestable)
            ]
            self.operator = node.childs[1]
            # '*' | '/' | 'div' | 'mod' | 'and'
            typeA = self.childs[0].type.name
            typeB = self.childs[1].type.name
            if self.operator=='div' or self.operator=='mod':
                if not(typeA=='integer' and typeB=='integer'):
                    if self.operator == 'div':
                        print("Line {0} : 整除的运算数不是整数类型".format(node.type[1]))
                    else:
                        print("Line {0} : 模运算的运算数不是整数类型".format(node.type[1]))
                    self.type=IntegerType()
                else:
                    self.type = self.childs[0].type
            elif self.operator=='and':
                if not(typeA=='boolean' and typeB=='boolean'):
                    print("Line {0} : AND运算的运算数不是boolean类型".format(node.type[1]))
                    self.type=BooleanType()
                else:
                    self.type = self.childs[0].type
            else:
                if typeA=='integer' and typeB=='real':
                    print("WARNING: Line {0} : 隐式类型转换从 'integer' 到 'real'".format(node.type[1]))
                    self.type=self.childs[1].type
                elif typeA=='real' and typeB=='integer':
                    print("WARNING: Line {0} : 隐式类型转换从 'integer' 到 'real'".format(node.type[1]))
                    self.type=self.childs[0].type
                elif (typeA=='real' and typeB=='real') or (typeA=='integer' and typeB=='integer'):
                    self.type = self.childs[0].type
                else:
                    print("Line {0} : 乘除运算的运算数不是整数或者实数类型".format(node.type[1]))
                    self.type=RealType()


        else:
            self.child_cnt = 1
            self.childs = [Factor(node.childs[0], symboltable, typestable)]
            self.operator = None
            self.type = self.childs[0].type

    def __str__(self):
        operator = self.operator
        if operator == 'div':
            operator = '/'
        elif operator == 'mod':
            operator = '%'
        elif operator == 'and':
            operator = '&&'
        if self.child_cnt == 1:
            return str(self.childs[0])
        else:
            return str(self.childs[0]) + ' ' + operator + ' ' + str(
                self.childs[1])


class Factor(object):
    def __init__(self, node, symboltable, typestable):
        # node = factor
        self.name = 'factor'
        self.kind = None
        self.type = None
        if node.type[1] == 'constant':
            self.kind = 'constant'
            self.child_cnt = 1
            self.childs = [Constant(node.childs[0], symboltable, typestable)]
            self.operator = None
            self.type=self.childs[0].type

        elif node.type[1] == 'variable':
            self.kind = 'variable'
            self.child_cnt = 1
            self.childs = [Variable(node.childs[0], symboltable, typestable)]
            self.operator = None
            self.type=self.childs[0].type
        elif node.type[1] == 'factor':
            self.kind = 'factor'
            self.child_cnt = 1
            self.childs = [Factor(node.childs[1], symboltable, typestable)]
            self.operator = node.childs[0]
            self.type=self.childs[0].type
            if self.operator=='not':
                if self.type.name!= 'boolean':
                    print("Line {0} : not 运算符不能对非boolean类型运算".format(node.type[2]))
                else :
                    pass
            else:
                if self.type.name != 'integer' and self.type.name!= 'real':
                    print("Line {0} : ADDOP 运算符不能对非整数实数类型运算".format(node.type[2]))
                else:
                    pass

            # '-' | 'not'
        elif node.type[1] == 'expression':
            self.kind = 'expression'
            self.child_cnt = 1
            self.childs = [Expression(node.childs[0], symboltable, typestable)]
            self.operator = None
            self.type = self.childs[0].type
        elif node.type[1] == 'function':
            self.kind = 'function'
            self.child_cnt = 1
            self.operator = None
            self.childs=None
            self.type=None
            func_name=node.childs[0].type[1]
            symbol=symboltable.getItem(func_name)
            if symbol is not None and symbol['type'].name == 'function':
                self.childs = [Function(node, symboltable, typestable)]
                self.type = self.childs[0].type
            else:
                print("Line {0} : 标识符 '{1}' 不是函数名".format(node.childs[0].type[2],func_name))

    def __str__(self):
        operator = self.operator
        if operator == 'not':
            operator = '!'
        ans = ""
        if self.operator is not None:
            ans = operator + ' '
        if self.kind == 'expression':
            ans += '('
        ans += str(self.childs[0])
        if self.kind == 'expression':
            ans += ')'
        return ans


class Constant(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'constant'
        # node.print()
        self.type = typestable.get_type(node)  # 常量类型
        self.val = node.type[1]

    def __str__(self):
        return str(self.val)


class Variable(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'variable'
        # node.print()
        symbol=symboltable.getItem(node.childs[0].type[1])
        if symbol is None:
            print("Line {0} : 标识符 '{1}' 不存在".format(node.childs[0].type[2],node.childs[0].type[1]))
        else:
            self.id = symboltable.getItem(
                node.childs[0].type[1])['actual_name']  # 大小写以声明时为准
            lineno=node.childs[0].type[2]
            self.id_isvar = symboltable.getItem(self.id)['type'].name == 'var'
            self.id_period = None
            # print('---'+self.id)
            if len(node.childs) > 1:
                if symboltable.getItem(self.id)['type'].name != 'array':
                    print("Line {0} : 标识符 '{1}' 不是数组，不能有下标索引".format(node.childs[0].type[2], node.childs[0].type[1]))
                else:
                    self.type = symboltable.getItem(self.id)['type'].type  # 元素类型
                    self.id_period = symboltable.getItem(self.id)['type'].period
                    self.part_expression_list = [
                            Expression(p, symboltable, typestable)
                            for p in node.childs[1].childs[0].childs
                        ]
                    logging.debug('Array Dimension '+str(len(self.id_period)))
                    logging.debug('expression list length ' + str(len(self.part_expression_list)))
                    if len(self.id_period)!=len(self.part_expression_list):
                        print("Line {0} : 数组 '{1}' 的维数是{2}，但对数组的引用只有{3}维".format(lineno,self.id,len(self.id_period),len(self.part_expression_list)))
                    else:
                        for idx,pair in enumerate(self.id_period):
                            cur_type=pair[0][0]
                            cur_expression_type=self.part_expression_list[idx].type.name
                            if cur_type != cur_expression_type:
                                print("Line {0} : 数组 '{1}' 的第{2}维是'{3}'类型，但对该维的引用是'{4}'类型".format(lineno, self.id,idx,cur_type,cur_expression_type))

            else:
                if symboltable.getItem(self.id)['type'].name == 'array':
                    print("Line {0} : 标识符 '{1}' 是数组，需要有下标索引".format(node.childs[0].type[2], node.childs[0].type[1]))
                self.part_expression_list = None
                self.type = symboltable.getItem(self.id)['type']

    def __str__(self):
        ans = self.id
        if self.id_isvar:
            ans = '(*' + ans + ')'
        if self.part_expression_list is not None:
            for i in range(len(self.part_expression_list)):
                ans += '[(' + str(
                    self.part_expression_list[i]) + ') - (' + str(
                        self.id_period[i][0][1]) + ')]'
        return ans


class Function(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'function'
        item = symboltable.getItem(node.childs[0].type[1])
        self.id = item['actual_name']  # 大小写以声明时为准
        # 函数名不需要考虑引用
        self.expression_list = [
            Expression(p, symboltable, typestable)
            for p in node.childs[1].childs
        ]
        params_type=item['type'].params
        if len(self.expression_list)!= len(params_type):
            print("Line {0} : 函数 '{1}' 的参数列表有{2}个参数，对函数的引用有{3}个参数".format(node.childs[0].type[2],self.id,len(params_type),len(self.expression_list)))
        else:
            for idx,expression in enumerate(self.expression_list):
                expression_type=expression.type.name
                if expression_type=='const':
                    expression_type=expression.type.type.name
                param_type=params_type[idx].type.name

                if param_type=='real' and expression_type=='integer':
                    print(
                        "WARNING: Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是real类型，将引用中的int隐式转换为real类型".format(node.childs[0].type[2],
                                                                                                self.id, idx))
                elif expression_type!= param_type:
                    print("Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是'{3}'类型，对函数的引用中的该参数是'{4}'类型".format(node.childs[0].type[2], self.id,idx,
                                                                                   param_type,
                                                                                   expression_type))

        self.isvar_list = [p.name == 'var'
                           for p in item['type'].params]  # 布尔数组，表示每个参数是否是var
        self.type = symboltable.getItem(self.id)['type'].type  # 返回值类型

    def __str__(self):
        ans = self.id + '('
        for i in range(len(self.expression_list)):
            if self.isvar_list[i]:
                ans += '&('
            ans += str(self.expression_list[i])
            if self.isvar_list[i]:
                ans += ')'
            if i != len(self.expression_list) - 1:
                ans += ', '
        ans += ')'
        return ans
