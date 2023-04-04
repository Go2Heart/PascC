import Expressions


class Statement(object):
    def __init__(self, node, symboltable, typestable):
        self.information = None
        if node.type == 'assignment_statement':
            self.information = AssignmentStatement(node, symboltable,
                                                   typestable)
        elif node.type == 'compound_statement':
            self.information = CompoundStatement(node, symboltable, typestable)
        elif node.type == 'empty_statement':
            self.information = EmptyStatement(node, symboltable, typestable)
        elif node.type == 'if_statement':
            self.information = IfStatement(node, symboltable, typestable)
        elif node.type == 'for_statement':
            self.information = ForStatement(node, symboltable, typestable)
        elif node.type == 'read_statement':
            self.information = ReadStatement(node, symboltable, typestable)
        elif node.type == 'write_statement':
            self.information = WriteStatement(node, symboltable, typestable)


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
        else:
            self.is_function = False


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
        self.id = node.childs[0].type[1]
        self.start_expression = Expressions.Expression(node.childs[1],
                                                       symboltable, typestable)
        self.end_expression = Expressions.Expression(node.childs[2],
                                                     symboltable, typestable)
        self.statement = Statement(node.childs[3], symboltable, typestable)


class ReadStatement(object):
    def __init__(self, node, symboltable, typestable):
        # child[0]=variable_list
        self.name = 'read_statement'
        self.variable_list = [
            Expressions.Variable(p, symboltable, typestable)
            for p in node.childs[0].childs
        ]
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