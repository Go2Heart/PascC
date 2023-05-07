import Expressions


class Statement(object):
    def __init__(self, node, symboltable, typestable):
        self.information = None
        if node.type[0] == 'assignment_statement':
            self.information = AssignmentStatement(node, symboltable,
                                                   typestable)
        elif node.type[0] == 'compound_statement':
            self.information = CompoundStatement(node, symboltable, typestable)
        elif node.type[0] == 'procedure_call':
            self.information = ProcedureStatement(node, symboltable,
                                                  typestable)
        elif node.type[0] == 'empty_statement':
            self.information = EmptyStatement(node, symboltable, typestable)
        elif node.type[0] == 'if_statement':
            self.information = IfStatement(node, symboltable, typestable)
        elif node.type[0] == 'read_statement':
            self.information = ReadStatement(node, symboltable, typestable)
        elif node.type[0] == 'write_statement':
            self.information = WriteStatement(node, symboltable, typestable)
        elif node.type[0] == 'for_statement':
            self.information = ForStatement(node, symboltable, typestable)


class ProcedureStatement(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'procedure_statement'
        self.id = None
        self.expression_list=None
        symbol=symboltable.getItem(node.childs[0].type[1])

        if symbol is None:
            print("Line {0} : 标识符 '{1}' 不存在".format(node.type[1],node.childs[0].type[1]))
        else:
            self.id = symbol['actual_name']
            self.expression_list = []
            if len(node.childs) == 2:
                for parameter in node.childs[1].childs:
                    self.expression_list.append(
                        Expressions.Expression(parameter, symboltable, typestable))
            params=symbol['type'].params
            if len(self.expression_list)!= len(params):
                print("Line {0} : 过程 '{1}' 有{2}个参数，但对过程的引用有{3}个参数".format(node.type[1], node.childs[0].type[1],len(params),len(self.expression_list)))
            else:
                for idx,expression in enumerate(self.expression_list):
                    expression_type=expression.type.name
                    if expression_type=='const':
                        expression_type=expression.type.type.name
                    param_type=params[idx].type.name
                    if param_type=='const':
                        param_type=params[idx].type.type.name
                    if param_type=='real' and expression_type=='integer':
                        print("WARNING: Line {0} : 过程 '{1}' 的第{2}个参数的引用进行隐式类型转换从integer转到real".format(node.type[1], node.childs[0].type[1],
                                                                                  idx+1))
                    elif param_type!=expression_type:
                        print("Line {0} : 过程 '{1}' 的第{2}个参数是 '{3}' 类型，但实参是 '{4}' 类型".format(node.type[1],
                                                                                                      node.childs[
                                                                                                          0].type[1],
                                                                                                      idx+1,param_type,expression_type))

class CompoundStatement(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'compound_statement'
        self.statements = []
        now = node.childs[0]  # now = statement_list
        for statement in now.childs:
            self.statements.append(
                Statement(statement, symboltable, typestable))


class AssignmentStatement(object):
    def __init__(self, node, symboltable, typestable):
        # child[0] = variable,child[1] = expression
        self.name = 'assignment_statement'
        self.variable = Expressions.Variable(node.childs[0], symboltable,
                                             typestable)
        self.expression = Expressions.Expression(node.childs[1], symboltable,
                                                 typestable)
        item = symboltable.getItem(self.variable.id)
        if item is not None and item['type'].name == 'function':
            self.is_function = True
            # TODO:控制流检查
        else:
            self.is_function = False
        variable_type=self.variable.type.name

        if variable_type=='const':
            variable_type=self.variable.type.type.name
            print("Line {0} : const 变量不能被赋值".format(node.type[1]))
        expression_type=self.expression.type.name
        if expression_type=='const':
            expression_type=self.expression.type.type.name
        if variable_type=='real' and expression_type=='integer':
            print("WARNING: Line {0} : 隐式类型转换，从integer转换成real".format(node.type[1]))
        elif variable_type!= expression_type:
            print("Line {0} : 赋值两边类型不匹配".format(node.type[1]))


class EmptyStatement(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'empty_statement'


class IfStatement(object):
    def __init__(self, node, symboltable, typestable):
        # child[0]=expression,child[1]=statement,child[2]=else_part
        self.name = 'if_statement'
        self.if_expression = Expressions.Expression(node.childs[0],
                                                    symboltable, typestable)
        self.then_statement = Statement(node.childs[1], symboltable,
                                        typestable)
        expression_type=self.if_expression.type.name
        if expression_type=='const':
            expression_type=self.if_expression.type.type.name
        if expression_type!='boolean':
            print("Line {0} : IF语句的表达式不是boolean类型".format(node.type[1]))
        if node.childs[2] is not None:
            self.else_statement = Statement(node.childs[2], symboltable,
                                            typestable)
        else:
            self.else_statement = None

    pass


class ForStatement(object):
    def __init__(self, node, symboltable, typestable):
        # child[0]=id,child[1]=expression,child[2]=expression,child[3]=statement
        self.name = 'for_statement'
        self.start_expression = Expressions.Expression(node.childs[1],
                                                       symboltable, typestable)
        self.end_expression = Expressions.Expression(node.childs[2],
                                                     symboltable, typestable)
        self.statement = Statement(node.childs[3], symboltable, typestable)
        self.id=None
        symbol=symboltable.getItem(node.childs[0].type[1])
        if symbol is None:
            print("Line {0} : 标识符 '{1}' 不存在".format(node.childs[0].type[2],node.childs[0].type[1]))
        else:
            self.id = symboltable.getItem(node.childs[0].type[1])['actual_name']  # pascal大小写不敏感，故输出时以定义时为准
            id_type=symbol['type'].name
            if id_type=='const':
                id_type=symbol['type'].type.name
                print("Line {0} : const 变量不能被赋值".format(node.childs[0].type[2]))
            start_expression_type=self.start_expression.type.name
            end_expression_type=self.end_expression.type.name
            if start_expression_type=='const':
                start_expression_type = self.start_expression.type.type.name
            if end_expression_type=='const':
                end_expression_type = self.end_expression.type.type.name
            if id_type!= start_expression_type:
                print("Line {0} : 变量 '{1}' 是 '{2}' 类型，但起始范围是 '{3}' 类型".format(node.childs[0].type[2],self.id,id_type,start_expression_type))
            if id_type!= end_expression_type:
                print("Line {0} : 变量 '{1}' 是 '{2}' 类型，但起始范围是 '{3}' 类型".format(node.childs[0].type[2],self.id,id_type,end_expression_type))


class ReadStatement(object):
    def __init__(self, node, symboltable, typestable):
        # child[0]=variable_list
        self.name = 'read_statement'
        self.variable_list = [
            Expressions.Variable(p, symboltable, typestable)
            for p in node.childs[0].childs
        ]
        for variable in self.variable_list:
            if symboltable.getItem(variable.id)['type'].name == 'array':
                print("Line {0} : 变量 '{1}' 是数组，不能被读取".format(node.type[1],variable.id))
            if variable.type.name=='function':
                print("Line {0} : 变量 '{1}' 是函数，不能被读取".format(node.type[1], variable.id))
            if variable.type.name=='const':
                print("Line {0} : '{1}' 是 常量，不能被读取".format(node.type[1], variable.id))
        if len(node.childs) > 1:
            self.newline = True
        else:
            self.newline = False


class WriteStatement(object):
    def __init__(self, node, symboltable, typestable):
        # child[0]=expression_list
        self.name = 'write_statement'
        self.expression_list = [
            Expressions.Expression(p, symboltable, typestable)
            for p in node.childs[0].childs
        ]
        if len(node.childs) > 1:
            self.newline = True
        else:
            self.newline = False

    pass