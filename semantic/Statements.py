class CompoundStatement(object):
    def __init__(self, node, symboltable, typestable):
        self.name = 'compound_statement'
        self.statements = []
        now = node.childs[0]  # now = statement_list
        for statement in now.childs:
            if statement.type == 'assignment_statement':
                self.statements.append(AssignmentStatement(statement))
            elif statement.type == 'empty_statement':
                self.statements.append(EmptyStatement(statement))
            elif statement.type == 'if_statement':
                self.statements.append(IfStatement(statement))
            elif statement.type == 'for_statement':
                self.statements.append(ForStatement(statement))
            elif statement.type == 'read_statement':
                self.statements.append(ReadStatement(statement))
            elif statement.type == 'write_statement':
                self.statements.append(WriteStatement(statement))


class AssignmentStatement(object):
    def __init__(self, node):
        # child[0] = variable,child[1]=expression
        self.name = 'assignment_statement'
    pass


class EmptyStatement(object):
    def __init__(self, node):
        self.name = 'empty_statement'
    pass


class IfStatement(object):
    def __init__(self, node):
        # child[0]=expression,child[1]=statement,child[2]=else_part
        self.name = 'if_statement'
    pass


class ForStatement(object):
    def __init__(self, node):
        # child[0]=id,child[1]=expression,child[2]=expression,child[3]=statement
        self.name = 'for_statement'
    pass


class ReadStatement(object):
    def __init__(self, node):
        # child[0]=variable_list
        self.name = 'read_statement'
    pass


class WriteStatement(object):
    def __init__(self, node):
        # child[0]=expression_list
        self.name = 'write_statement'
    pass