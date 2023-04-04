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
            self.type = self.childs[0].type  # TODO 类型计算，这里暂定为第一个表达式的类型
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
            self.type = self.childs[0].type  # TODO 类型计算，这里暂定为第一个表达式的类型
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
            self.type = self.childs[0].type  # TODO 类型计算，这里暂定为第一个表达式的类型
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
        if node.type[1] == 'constant':
            self.kind = 'constant'
            self.child_cnt = 1
            self.childs = [Constant(node.childs[0], symboltable, typestable)]
            self.operator = None
        elif node.type[1] == 'variable':
            self.kind = 'variable'
            self.child_cnt = 1
            self.childs = [Variable(node.childs[0], symboltable, typestable)]
            self.operator = None
        elif node.type[1] == 'factor':
            self.kind = 'factor'
            self.child_cnt = 1
            self.childs = [Factor(node.childs[1], symboltable, typestable)]
            self.operator = node.childs[0]
            # '-' | 'not'
        elif node.type[1] == 'expression':
            self.kind = 'expression'
            self.child_cnt = 1
            self.childs = [Expression(node.childs[0], symboltable, typestable)]
            self.operator = None
        elif node.type[1] == 'function':
            self.kind = 'function'
            self.child_cnt = 1
            self.childs = [Function(node, symboltable, typestable)]
            self.operator = None
        self.type = self.childs[0].type

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
        self.id = symboltable.getItem(
            node.childs[0].type[1])['actual_name']  # 大小写以声明时为准
        self.id_isvar = symboltable.getItem(self.id)['type'].name == 'var'
        self.id_period = None
        # print('---'+self.id)
        if len(node.childs) > 1:
            self.part_expression_list = [
                Expression(p, symboltable, typestable)
                for p in node.childs[1].childs[0].childs
            ]
            self.type = symboltable.getItem(self.id)['type'].type  # 元素类型
            self.id_period = symboltable.getItem(self.id)['type'].period  # 维数
        else:
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
