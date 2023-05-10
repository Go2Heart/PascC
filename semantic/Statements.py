import Expressions
from semantic.SymbolTable import IndexStack
from semantic.Types import NoneType


class Statement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag=False
        self.ReturnFlag=False
        self.information = None
        if node.type[0] == 'assignment_statement':
            self.information = AssignmentStatement(node, symboltable,
                                                   typestable,function_id)
        elif node.type[0] == 'compound_statement':
            self.information = CompoundStatement(node, symboltable, typestable,function_id)
        elif node.type[0] == 'procedure_call':
            self.information = ProcedureStatement(node, symboltable,
                                                  typestable,function_id)
        elif node.type[0] == 'empty_statement':
            self.information = EmptyStatement(node, symboltable, typestable,function_id)
        elif node.type[0] == 'if_statement':
            self.information = IfStatement(node, symboltable, typestable,function_id)
        elif node.type[0] == 'read_statement':
            self.information = ReadStatement(node, symboltable, typestable,function_id)
        elif node.type[0] == 'write_statement':
            self.information = WriteStatement(node, symboltable, typestable,function_id)
        elif node.type[0] == 'for_statement':
            self.information = ForStatement(node, symboltable, typestable,function_id)
        self.ErrorFlag=self.information.ErrorFlag
        self.ReturnFlag|=self.information.ReturnFlag


class ProcedureStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag=False
        self.ReturnFlag = False
        self.name = 'procedure_statement'
        self.id = None
        self.expression_list=None
        symbol=symboltable.getItem(node.childs[0].type[1])

        if symbol is None:
            print("Line {0} : 标识符 '{1}' 不存在".format(node.type[1],node.childs[0].type[1]))
            self.ErrorFlag=True
        else:
            if symbol['type'].name!='function':
                print("Line {0} : 标识符 '{1}' 不是函数名".format(node.type[1],node.childs[0].type[1]))
                self.ErrorFlag=True
            elif symbol['type'].type.name!='void':
                print("Line {0} : 标识符 '{1}' 不是过程，不能被未引用调用".format(node.type[1], node.childs[0].type[1]))
                self.ErrorFlag = True
            else:

                self.id = symbol['actual_name']
                self.expression_list = []
                if len(node.childs) == 2:
                    for parameter in node.childs[1].childs:
                        self.expression_list.append(
                            Expressions.Expression(parameter, symboltable, typestable))
                    for expression in self.expression_list:
                            self.ErrorFlag|=expression.ErrorFlag
                params=symbol['type'].params
                if len(self.expression_list)!= len(params):
                    print("Line {0} : 过程 '{1}' 有{2}个参数，但对过程的引用有{3}个参数".format(node.type[1], node.childs[0].type[1],len(params),len(self.expression_list)))
                    self.ErrorFlag=True
                else:
                    for idx,expression in enumerate(self.expression_list):
                        is_var=False
                        is_expression_type_const=False
                        expression_type=expression.type.name
                        # print(idx)
                        # print(expression_type)
                        if expression_type=='const' or expression_type=='var':
                            if expression_type=='const':
                                is_expression_type_const=True
                            expression_type=expression.type.type.name

                        if params[idx].name=='var' or params[idx].name=='const':
                            if params[idx].name=='var':
                                is_var=True
                            param_type=params[idx].type.name
                        else:
                            param_type=params[idx].name
                        # print(is_var)
                        # print(is_expression_type_const)
                        if is_var and is_expression_type_const:
                            print("Line {0} : 过程 '{1}' 的第{2}个参数是var，实参不能是常量".format(node.type[1],
                                                                                                node.childs[0].type[1],
                                                                                                idx + 1))

                        if is_var:
                            if param_type != expression_type:
                                print("Line {0} : 过程 '{1}' 的第{2}个参数是 '{3}' 类型，但实参是 '{4}' 类型".format(node.type[1],
                                                                                                    node.childs[0].type[
                                                                                                        1],
                                                                                                    idx + 1, param_type,
                                                                                                    expression_type))
                                self.ErrorFlag = True
                        else:

                            if param_type=='real' and expression_type=='integer':
                                print("WARNING: Line {0} : 过程 '{1}' 的第{2}个参数的引用进行隐式类型转换从integer转到real".format(node.type[1], node.childs[0].type[1],
                                                                                          idx+1))
                            elif param_type!=expression_type:
                                print("Line {0} : 过程 '{1}' 的第{2}个参数是 '{3}' 类型，但实参是 '{4}' 类型".format(node.type[1],node.childs[0].type[1],
                                                                                                              idx+1,param_type,expression_type))
                                self.ErrorFlag=True

class CompoundStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag=False
        self.ReturnFlag = False
        self.name = 'compound_statement'
        self.statements = []
        now = node.childs[0]  # now = statement_list
        for statement in now.childs:
            self.statements.append(
                Statement(statement, symboltable, typestable,function_id))
        for statement in self.statements:
            self.ErrorFlag |=statement.ErrorFlag
            self.ReturnFlag|=statement.ReturnFlag

class AssignmentStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag = False
        self.ReturnFlag = False
        # child[0] = variable,child[1] = expression
        self.name = 'assignment_statement'
        self.variable = Expressions.Variable(node.childs[0], symboltable,
                                             typestable)
        self.ErrorFlag |=self.variable.ErrorFlag
        self.expression = Expressions.Expression(node.childs[1], symboltable,
                                                 typestable)
        self.ErrorFlag|=self.expression.ErrorFlag
        item = symboltable.getItem(self.variable.id)
        if item is not None and item['type'].name == 'function':
            self.is_function = True
            # TODO:控制流检查
            if function_id != self.variable.id:
                print("Line {0} : 在函数 '{1}' 外不能将函数名作为左值".format(node.childs[0].type[1],self.variable.id))
                self.ErrorFlag=True
            else:
                self.ReturnFlag=True

            # print("???????????????")
            # print(item['block'])
            # print(IndexStack.topblock())
        else:
            self.is_function = False
        variable_type=self.variable.type.name
        if variable_type=='function':
            variable_type=self.variable.type.type.name

        if variable_type=='const':
            variable_type=self.variable.type.type.name
            print("Line {0} : const 变量不能被赋值".format(node.type[1]))
            self.ErrorFlag = True
        expression_type=self.expression.type.name
        if expression_type=='const':
            expression_type=self.expression.type.type.name
        if variable_type=='real' and expression_type=='integer':
            print("WARNING: Line {0} : 隐式类型转换，从integer转换成real".format(node.type[1]))
        elif variable_type!= expression_type:
            print("Line {0} : 赋值两边类型不匹配".format(node.type[1],variable_type,expression_type))
            self.ErrorFlag = True


class EmptyStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag = False
        self.ReturnFlag = False
        self.name = 'empty_statement'


class IfStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag = False
        self.ReturnFlag = False
        # child[0]=expression,child[1]=statement,child[2]=else_part
        self.name = 'if_statement'
        self.if_expression = Expressions.Expression(node.childs[0],
                                                    symboltable, typestable)
        self.ErrorFlag |=self.if_expression.ErrorFlag
        self.then_statement = Statement(node.childs[1], symboltable,
                                        typestable,function_id)
        self.ErrorFlag|=self.then_statement.ErrorFlag
        self.ReturnFlag|=self.then_statement.ReturnFlag
        expression_type=self.if_expression.type.name
        if expression_type=='const':
            expression_type=self.if_expression.type.type.name
        if expression_type!='boolean':
            print("Line {0} : IF语句的表达式不是boolean类型".format(node.type[1]))
            self.ErrorFlag=True
        if node.childs[2] is not None:
            self.else_statement = Statement(node.childs[2], symboltable,
                                            typestable,function_id)
            self.ErrorFlag|=self.else_statement.ErrorFlag
            self.ReturnFlag|=self.else_statement.ReturnFlag
        else:
            self.else_statement = None

    pass


class ForStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag = False
        self.ReturnFlag = False
        # child[0]=id,child[1]=expression,child[2]=expression,child[3]=statement
        self.name = 'for_statement'
        self.start_expression = Expressions.Expression(node.childs[1],
                                                       symboltable, typestable)
        self.ErrorFlag |= self.start_expression.ErrorFlag
        self.end_expression = Expressions.Expression(node.childs[2],
                                                     symboltable, typestable)
        self.ErrorFlag|=self.end_expression.ErrorFlag
        self.statement = Statement(node.childs[3], symboltable, typestable,function_id)
        self.ErrorFlag|=self.statement.ErrorFlag
        self.ReturnFlag|=self.statement.ReturnFlag
        self.id=None
        symbol=symboltable.getItem(node.childs[0].type[1])
        if symbol is None:
            print("Line {0} : 标识符 '{1}' 不存在".format(node.childs[0].type[2],node.childs[0].type[1]))
            self.ErrorFlag=True
        else:
            self.id = symboltable.getItem(node.childs[0].type[1])['actual_name']  # pascal大小写不敏感，故输出时以定义时为准
            id_type=symbol['type'].name
            if id_type=='const':
                id_type=symbol['type'].type.name
                print("Line {0} : const 变量不能被赋值".format(node.childs[0].type[2]))
                self.ErrorFlag=True
            start_expression_type=self.start_expression.type.name
            end_expression_type=self.end_expression.type.name
            if start_expression_type=='const':
                start_expression_type = self.start_expression.type.type.name
            if end_expression_type=='const':
                end_expression_type = self.end_expression.type.type.name
            if id_type!= start_expression_type:
                print("Line {0} : 变量 '{1}' 是 '{2}' 类型，但起始范围是 '{3}' 类型".format(node.childs[0].type[2],self.id,id_type,start_expression_type))
                self.ErrorFlag=True
            if id_type!= end_expression_type:
                print("Line {0} : 变量 '{1}' 是 '{2}' 类型，但终止范围是 '{3}' 类型".format(node.childs[0].type[2],self.id,id_type,end_expression_type))
                self.ErrorFlag=True


class ReadStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag = False
        self.ReturnFlag = False
        # child[0]=variable_list
        self.name = 'read_statement'
        self.variable_list = [
            Expressions.Variable(p, symboltable, typestable)
            for p in node.childs[0].childs
        ]
        for variable in self.variable_list:
            self.ErrorFlag|=variable.ErrorFlag
        for variable in self.variable_list:
            if variable.type.name == 'array':
                print("Line {0} : 变量 '{1}' 是数组，不能被读取".format(node.type[1],variable.id))
                self.ErrorFlag=True
            if variable.type.name=='function':
                print("Line {0} : 变量 '{1}' 是函数，不能被读取".format(node.type[1], variable.id))
                self.ErrorFlag=True
            if variable.type.name=='const':
                print("Line {0} : '{1}' 是 常量，不能被读取".format(node.type[1], variable.id))
                self.ErrorFlag=True
            if variable.type.name=='file':
                print("Line {0} : '{1}' 是 文件类型，不能被读取".format(node.type[1], variable.id))
                self.ErrorFlag=True
        if len(node.childs) > 1:
            self.newline = True
        else:
            self.newline = False


class WriteStatement(object):
    def __init__(self, node, symboltable, typestable,function_id=None):
        self.ErrorFlag=False
        self.ReturnFlag = False
        # child[0]=expression_list
        self.name = 'write_statement'
        self.expression_list = [
            Expressions.Expression(p, symboltable, typestable)
            for p in node.childs[0].childs
        ]
        for expression in self.expression_list:
            self.ErrorFlag|=expression.ErrorFlag
        if len(node.childs) > 1:
            self.newline = True
        else:
            self.newline = False

    pass