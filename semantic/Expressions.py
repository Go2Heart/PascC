import logging

from semantic.Types import IntegerType, BooleanType, RealType, NoneType, ConstType


class Expression(object):
    def __init__(self, node, symboltable, typestable):
        self.ErrorFlag=False
        self.is_complex_expression=False
        # node = expression
        self.name = 'expression'
        # node.print()
        if len(node.childs) == 3:
            self.is_complex_expression = True
            self.child_cnt = 2
            self.childs = [
                SimpleExpression(node.childs[0], symboltable, typestable),
                SimpleExpression(node.childs[2], symboltable, typestable)
            ]
            self.ErrorFlag|=self.childs[0].ErrorFlag
            self.ErrorFlag |= self.childs[1].ErrorFlag
            self.operator = node.childs[1]
            # '=' | '<>' | '<' | '<=' | '>' | '>='
            typeA = self.childs[0].type.name

            if typeA=='const' or typeA=='var':
                typeA=self.childs[0].type.type.name
            typeB = self.childs[1].type.name
            if typeB=='const' or typeB=='var':
                typeB=self.childs[1].type.type.name
            if (typeA == 'integer' and typeB=='real') or (typeA=='real' and typeB=='integer'):
                print("WARNING: Line {0} : 隐式类型转换从 'integer' 到 'real'".format(node.type[1]))
            elif typeA!=typeB:
                print("Line {0} : 左右表达式不能进行大小比较".format(node.type[1]))
                self.ErrorFlag=True
            self.type=BooleanType()
        else:
            self.child_cnt = 1
            self.childs = [
                SimpleExpression(node.childs[0], symboltable, typestable)
            ]
            self.is_complex_expression=self.childs[0].is_complex_expression
            self.operator = None
            self.type = self.childs[0].type
            self.ErrorFlag|=self.childs[0].ErrorFlag

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
        self.ErrorFlag=False
        self.is_complex_expression = False
        # node = simple_expression
        self.name = 'simple_expression'
        if len(node.childs) == 3:
            self.is_complex_expression = True
            self.child_cnt = 2
            self.childs = [
                SimpleExpression(node.childs[0], symboltable, typestable),
                Term(node.childs[2], symboltable, typestable)
            ]
            self.ErrorFlag |= self.childs[0].ErrorFlag
            self.ErrorFlag |= self.childs[1].ErrorFlag
            self.operator = node.childs[1]
            # '+' | '-' | 'or'

            typeA = self.childs[0].type.name
            if typeA=='const' or typeA=='var':
                typeA=self.childs[0].type.type.name
            typeB = self.childs[1].type.name
            if typeB=='const' or typeB=='var':
                typeB=self.childs[1].type.type.name

            if self.operator == 'or':
                if not (typeA == 'boolean' and typeB == 'boolean'):
                    print("Line {0} : OR运算的运算数不是boolean类型".format(node.type[1]))
                    self.ErrorFlag=True
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
                    self.ErrorFlag=True
                    self.type = RealType()



        else:
            self.child_cnt = 1
            self.childs = [Term(node.childs[0], symboltable, typestable)]
            self.is_complex_expression=self.childs[0].is_complex_expression
            self.ErrorFlag |= self.childs[0].ErrorFlag
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
        self.ErrorFlag=False
        self.is_complex_expression = False
        self.name = 'term'
        if len(node.childs) == 3:
            self.is_complex_expression = True
            self.child_cnt = 2
            self.childs = [
                Term(node.childs[0], symboltable, typestable),
                Factor(node.childs[2], symboltable, typestable)
            ]
            self.ErrorFlag |= self.childs[0].ErrorFlag
            self.ErrorFlag |= self.childs[1].ErrorFlag
            self.operator = node.childs[1]
            # '*' | '/' | 'div' | 'mod' | 'and'
            typeA = self.childs[0].type.name
            typeB = self.childs[1].type.name
            if typeA=='const' or typeA=='var':
                typeA=self.childs[0].type.type.name
            if typeB=='const' or typeB=='var':
                typeB=self.childs[1].type.type.name
            if self.operator=='div' or self.operator=='mod':
                if not(typeA=='integer' and typeB=='integer'):
                    if self.operator == 'div':
                        print("Line {0} : 整除的运算数不是整数类型".format(node.type[1]))
                        self.ErrorFlag=True
                    else:
                        print("Line {0} : 模运算的运算数不是整数类型".format(node.type[1]))
                        self.ErrorFlag=True
                    self.type=IntegerType()
                else:
                    self.type = self.childs[0].type
            elif self.operator=='and':
                if not(typeA=='boolean' and typeB=='boolean'):
                    print("Line {0} : AND运算的运算数不是boolean类型".format(node.type[1]))
                    self.ErrorFlag=True
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
                    self.ErrorFlag=True


        else:
            self.child_cnt = 1
            self.childs = [Factor(node.childs[0], symboltable, typestable)]
            self.is_complex_expression=self.childs[0].is_complex_expression
            self.ErrorFlag|=self.childs[0].ErrorFlag
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
        self.ErrorFlag=False
        self.is_complex_expression = False
        self.name = 'factor'
        self.kind = None
        self.type = NoneType()
        if node.type[1] == 'constant':
            self.kind = 'constant'
            self.child_cnt = 1
            self.childs = [Constant(node.childs[0], symboltable, typestable)]
            self.ErrorFlag=self.childs[0].ErrorFlag
            self.operator = None
            self.type=self.childs[0].type

        elif node.type[1] == 'variable':
            self.kind = 'variable'
            self.child_cnt = 1
            self.childs = [Variable(node.childs[0], symboltable, typestable)]
            self.ErrorFlag = self.childs[0].ErrorFlag
            self.operator = None
            self.type=self.childs[0].type
            if self.type.name=='function' :
                if len(self.type.params)!=0:
                    print('Line {0} : 函数引用缺少实参'.format(node.childs[0].type[1]))
                else:
                    self.type=self.type.type
        elif node.type[1] == 'factor':
            self.is_complex_expression=True
            self.kind = 'factor'
            self.child_cnt = 1
            self.childs = [Factor(node.childs[1], symboltable, typestable)]
            self.ErrorFlag = self.childs[0].ErrorFlag
            self.operator = node.childs[0]
            self.type=self.childs[0].type
            type_name=self.type.name
            if type_name=='var' or type_name=='const':
                type_name=self.type.type.name
            if self.operator=='not':
                if type_name!= 'boolean':
                    print("Line {0} : not 运算符不能对非boolean类型运算".format(node.type[2]))
                    self.ErrorFlag=True
                else :
                    pass
            else:
                if type_name != 'integer' and type_name!= 'real':
                    print("Line {0} : ADDOP 运算符不能对非整数实数类型运算".format(node.type[2]))
                    self.ErrorFlag=True
                else:
                    pass

            # '-' | 'not'
        elif node.type[1] == 'expression':
            self.kind = 'expression'
            self.child_cnt = 1
            self.childs = [Expression(node.childs[0], symboltable, typestable)]
            self.is_complex_expression|=self.childs[0].is_complex_expression
            self.ErrorFlag = self.childs[0].ErrorFlag
            self.operator = None
            self.type = self.childs[0].type
        elif node.type[1] == 'function':
            self.kind = 'function'
            self.child_cnt = 1
            self.operator = None
            self.childs=None
            self.type=NoneType()
            func_name=node.childs[0].type[1]
            symbol=symboltable.getItem(func_name)

            if symbol is not None and symbol['type'].name == 'function':
                self.childs = [Function(node, symboltable, typestable)]
                self.ErrorFlag = self.childs[0].ErrorFlag
                self.type = self.childs[0].type

            else:
                print("Line {0} : 标识符 '{1}' 不是函数名".format(node.childs[0].type[2],func_name))
                self.ErrorFlag=True

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
        self.is_complex_expression =False
        self.name = 'constant'
        # node.print()
        self.type = typestable.get_type(node)  # 常量类型
        # print("CONST!!!!!!!!!")
        # print(self.type.name)
        self.ErrorFlag=self.type.ErrorFlag
        self.val = node.type[1]
        self.type=ConstType(self.type,self.val)

    def __str__(self):
        return str(self.val)

class VariablePart(object):
    def __init__(self,node, type, lineno, id_name,symboltable, typestable):
        self.name = 'variable_part'
        self.mode=None 
        self.pre_type=None
        self.type = None
        self.ErrorFlag = False
        self.id=id_name
        while type.name == 'type':
            type=type.type
        # print(type)
        # node.print()
        self.variable_part = None
        # node.print()
        if node is not None:
            self.mode=node.type[0]
            if type.name != 'array' and type.name !='record':
                print("Line {0} : 标识符 '{1}' 不是数组/记录，不能有索引".format(lineno, id_name))
                self.ErrorFlag = True
                self.type = type
            elif self.mode == 'array':
                self.pre_type = type.type  # 元素类型
                self.type = self.pre_type
                self.id_period = type.period
                self.part_expression_list = [
                        Expression(p, symboltable, typestable)
                        for p in node.childs[0].childs
                    ]
                for expression in self.part_expression_list:
                    self.ErrorFlag|=expression.ErrorFlag
                if node.childs[1] is not None:
                    self.variable_part = VariablePart(node.childs[1],self.pre_type,lineno,id_name,symboltable,typestable)
                    self.type = self.variable_part.type
                logging.debug('Array Dimension '+str(len(self.id_period)))
                logging.debug('expression list length ' + str(len(self.part_expression_list)))
                if len(self.id_period)!=len(self.part_expression_list):
                    print("Line {0} : 数组 '{1}' 的维数是{2}，但对数组的引用有{3}维".format(lineno,self.id,len(self.id_period),len(self.part_expression_list)))
                    self.ErrorFlag=True
                else:
                    for idx,pair in enumerate(self.id_period):
                        cur_type=pair[0][0]
                        cur_expression_type=self.part_expression_list[idx].type.name
                        if cur_expression_type=='const':
                            cur_expression_type=self.part_expression_list[idx].type.type.name
                        if cur_type != cur_expression_type:
                            print("Line {0} : 数组 '{1}' 的第{2}维是'{3}'类型，但对该维的引用是'{4}'类型".format(lineno, self.id,idx,cur_type,cur_expression_type))
                            self.ErrorFlag=True
            elif self.mode == 'record':
                self.id = node.childs[0]
                self.pre_type = type.fields[self.id] # 元素类型
                self.type = self.pre_type
                # print(self.pre_type)
                if node.childs[1] is not None:
                    self.variable_part = VariablePart(node.childs[1],self.pre_type,lineno,id_name,symboltable,typestable)
                    self.type = self.variable_part.type
        
        
    def __str__(self):
        ans = ''
        if self.mode == 'array':
            if self.part_expression_list is not None:
                for i in range(len(self.part_expression_list)):
                    ans += '[(' + str(
                        self.part_expression_list[i]) + ') - ' + str(
                            self.id_period[i][0][1]) + ']'
        elif self.mode == 'record':
            ans += '.' + self.id
        if self.variable_part is not None:
            ans += str(self.variable_part)
        return ans

class Variable(object):
    def __init__(self, node, symboltable, typestable):
        self.is_complex_expression = False
        self.name = 'variable'
        self.id=node.childs[0].type[1]
        self.ErrorFlag=False
        self.type=NoneType()
        # node.print()
        self.variable_part = None
        symbol=symboltable.getItem(node.childs[0].type[1])
        if symbol is None:
            print("Line {0} : 标识符 '{1}' 不存在".format(node.childs[0].type[2],node.childs[0].type[1]))
            self.ErrorFlag=True
        else:
            self.id = symboltable.getItem(
                node.childs[0].type[1])['actual_name']  # 大小写以声明时为准
            lineno=node.childs[0].type[2]
            self.id_isvar = symboltable.getItem(self.id)['type'].name == 'var'
            self.id_period = None
            if len(node.childs) > 1:
                type=symboltable.getItem(self.id)['type']
                if type.name == 'var':
                    type=type.type
                self.variable_part = VariablePart(node.childs[1],type,lineno,node.childs[0].type[1],symboltable,typestable)
                self.ErrorFlag|=self.variable_part.ErrorFlag
                # print(self.type)
                self.type = self.variable_part.type
                # print(self.type)
            else:
                if symboltable.getItem(self.id)['type'].name == 'array':
                    print("Line {0} : 标识符 '{1}' 是数组，但对它的引用没有下标索引".format(node.childs[0].type[2], node.childs[0].type[1]))
                    self.ErrorFlag=True
                elif symboltable.getItem(self.id)['type'].name == 'type':
                    if symboltable.getItem(self.id)['type'].type.name == 'array':
                        print("Line {0} : 标识符 '{1}' 是数组，但对它的引用没有下标索引".format(node.childs[0].type[2], node.childs[0].type[1]))
                    elif symboltable.getItem(self.id)['type'].type.name == 'record':
                        print("Line {0} : 标识符 '{1}' 是记录，但对它的引用没有成员索引".format(node.childs[0].type[2], node.childs[0].type[1]))
                    self.ErrorFlag=True
                self.part_expression_list = None
                self.type = symboltable.getItem(self.id)['type']

    def __str__(self):
        ans = self.id 
        if self.id_isvar:
            ans = '(*' + ans + ')'
        if self.variable_part is not None:
            ans = ans + str(self.variable_part)
        return ans


class Function(object):
    def __init__(self, node, symboltable, typestable):
        self.is_complex_expression = False
        self.ErrorFlag=False
        self.name = 'function'
        item = symboltable.getItem(node.childs[0].type[1])
        self.id = item['actual_name']  # 大小写以声明时为准
        # 函数名不需要考虑引用
        self.expression_list = [
            Expression(p, symboltable, typestable)
            for p in node.childs[1].childs
        ]
        for expression in self.expression_list:
            self.ErrorFlag|=expression.ErrorFlag
        self.isvar_list = [p.name == 'var'
                           for p in item['type'].params]  # 布尔数组，表示每个参数是否是var
        self.type = symboltable.getItem(self.id)['type'].type  # 返回值类型
        params_type=item['type'].params
        if len(self.expression_list)!= len(params_type):
            print("Line {0} : 函数 '{1}' 的参数列表有{2}个参数，对函数的引用有{3}个参数".format(node.childs[0].type[2],self.id,len(params_type),len(self.expression_list)))
            self.ErrorFlag=True
        else:
            for idx,expression in enumerate(self.expression_list):
                is_var=False
                is_expression_type_const=False
                expression_type=expression.type.name
                if expression_type=='const' or expression_type=='var':
                    if expression_type=='const':
                        is_expression_type_const=True
                    expression_type=expression.type.type.name

                if params_type[idx].name=='var':
                    param_type=params_type[idx].type.name
                    is_var=True
                else:
                    param_type=params_type[idx].name
                # print(idx)
                # print(expression.is_complex_expression)
                if is_var and expression.is_complex_expression:
                    print(
                        "Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是var，实参不能是复杂表达式".format(
                            node.childs[0].type[2],
                            self.id, idx + 1))
                    self.ErrorFlag=True
                if is_var and is_expression_type_const:
                    print(
                        "Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是var，实参不能是常量".format(
                            node.childs[0].type[2],
                            self.id, idx + 1))
                    self.ErrorFlag=True
                elif is_var:
                    if expression_type != param_type:
                        print("Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是'{3}'类型，对函数的引用中的该参数是'{4}'类型".format(
                            node.childs[0].type[2], self.id, idx + 1,
                            param_type,
                            expression_type))
                        self.ErrorFlag=True
                else:


                    if param_type=='real' and expression_type=='integer':
                        print(
                            "WARNING: Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是real类型，将引用中的int隐式转换为real类型".format(node.childs[0].type[2],
                                                                                                    self.id, idx+1))
                    elif expression_type!= param_type:
                        print("Line {0} : 函数 '{1}' 的参数列表中的第{2}个参数是'{3}'类型，对函数的引用中的该参数是'{4}'类型".format(node.childs[0].type[2], self.id,idx+1,
                                                                                       param_type,
                                                                                       expression_type))
                        self.ErrorFlag=True



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
