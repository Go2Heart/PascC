class CodeGenerater(object):
    # 基于 符号表symboltable，类型表typestable，根节点program进行代码生成
    def __init__(self, symboltable, typestable, output=None):
        self.symboltable = symboltable
        self.typestable = typestable
        self.depth = 0
        self.output = output

    def print(self, ss):
        """选择性输出到文件"""
        if self.output:
            self.output.write(ss+'\n')
            print(ss)
        else:
            print(ss)

    def ProgramGenerate(self, program):

        # 索引块初始化
        self.symboltable.setIndexStack()

        # 进入块
        self.symboltable.pushblock()  # 进入到一个块中了，更新索引表
        self.symboltable.recover_const_var()
        self.symboltable.recover_function()

        self.print("#include<stdio.h>")
        self.symboltable.recover_const_var()

        for type in program.typelist:
            self.print(type.type_generate()+';')

        for id in program.const_idlist:
            item = self.symboltable.getItem(id)
            self.print(item["type"].generate(False, id) + ';')

        for ids in program.var_idlist:
            item = self.symboltable.getItem(ids[0])
            # self.print(item)
            self.print(item["type"].generate(False, *ids) + ';')

        for subprogram in program.subprogram_list:
            self.symboltable.recover_function()
            self.SubProgramGenerate(subprogram)

        self.print("int main()")
        self.print("{")
        self.depth += 1
        self.CompoundGenerate(program.compound_statement)
        self.print(' ' * 4 * self.depth + "return 0;")
        self.depth -= 1
        self.print("}")

        self.symboltable.popblock()

    def SubProgramGenerate(self, subprogram):
        # 进入块
        self.symboltable.pushblock()  # 进入到一个块中了，更新索引表
        self.symboltable.recover_function()
        self.symboltable.recover_const_var()

        item = self.symboltable.getItem(subprogram.name)
        # print(subprogram.name=='fun')
        # print("!!!!!!!!")
        # self.symboltable.print()
        # print(item)
        self.print(item["type"].generate(False, subprogram.name,
                                    subprogram.parameter_idlist))

        self.print('{')
        self.depth += 1
        for id in subprogram.const_idlist:
            item = self.symboltable.getItem(id)
            self.print(' ' * 4 * self.depth + item["type"].generate(False, id) + ';')

        for ids in subprogram.var_idlist:
            item = self.symboltable.getItem(ids[0])
            # self.print(item)
            self.print(' ' * 4 * self.depth + item["type"].generate(False, *ids) + ';')

        self.CompoundGenerate(subprogram.compound_statement)
        self.depth -= 1
        self.print('}')

        self.symboltable.popblock()

    def StatementGenerate(self, statement):
        if statement.information.name == 'compound_statement':
            self.print(' ' * 4 * self.depth + '{')
            self.depth += 1
            self.CompoundGenerate(statement.information)
            self.depth -= 1

            self.print(' ' * 4 * self.depth + '}')

        elif statement.information.name == 'assignment_statement':
            self.AssignmentGenerate(statement.information)
        elif statement.information.name == 'empty_statement':
            self.EmptyGenerate(statement.information)
        elif statement.information.name == 'if_statement':
            self.IfGenerate(statement.information)
        elif statement.information.name == 'for_statement':
            self.ForGenerate(statement.information)
        elif statement.information.name == 'read_statement':
            self.ReadGenerate(statement.information)
        elif statement.information.name == 'write_statement':
            self.WriteGenerate(statement.information)
        elif statement.information.name == 'procedure_statement':
            self.ProcedureGenerate(statement.information)
        elif statement.information.name == 'while_statement':
            self.WhileGenerate(statement.information)
        elif statement.information.name == 'repeat_statement':
            self.RepeatGenerate(statement.information)

    def CompoundGenerate(self, compoundstatement):
        for statement in compoundstatement.statements:
            self.StatementGenerate(statement)

    def ProcedureGenerate(self, procedurestatement):
        ans = ' ' * 4 * self.depth + str(procedurestatement.id) + '('
        first = True
        for expression in procedurestatement.expression_list:
            if first:
                first = False
            else:
                ans += ', '
            ans += str(expression)
        ans += ');'
        self.print(ans)

    def AssignmentGenerate(self, assignmentstatement):
        if assignmentstatement.is_function:
            self.print(' ' * 4 * self.depth + 'return ' +
                  str(assignmentstatement.expression) + ';')
        else:
            self.print(' ' * 4 * self.depth + str(assignmentstatement.variable) +
                  ' = ' + str(assignmentstatement.expression) + ';')

    def EmptyGenerate(self, statement):
        # self.print(' ' * 4 * self.depth + ';')
        # 空语句直接不输出比较好看
        pass

    def IfGenerate(self, statement):
        self.print(' ' * 4 * self.depth + 'if (' + str(statement.if_expression) +
              ')')
        if statement.then_statement.information.name == 'compound_statement':
            self.StatementGenerate(statement.then_statement)
        else:
            self.depth += 1
            self.StatementGenerate(statement.then_statement)
            self.depth -= 1
        if statement.else_statement:
            self.print(' ' * 4 * self.depth + 'else')
            if statement.else_statement.information.name == 'compound_statement':
                self.StatementGenerate(statement.else_statement)
            else:
                self.depth += 1
                self.StatementGenerate(statement.else_statement)
                self.depth -= 1

    def ForGenerate(self, forstatement):
        self.print(' ' * 4 * self.depth + 'for (' + str(forstatement.id) + ' = ' +
              str(forstatement.start_expression) + '; ' +
              str(forstatement.id) + ' <= ' +
              str(forstatement.end_expression) + '; ' + str(forstatement.id) +
              '++)')
        if forstatement.statement.information.name == 'compound_statement':
            self.StatementGenerate(forstatement.statement)
        else:
            self.depth += 1
            self.StatementGenerate(forstatement.statement)
            self.depth -= 1

    def ReadGenerate(self, readstatement):
        ans = 'scanf("'
        for p in readstatement.variable_list:
            type = p.type
            while type.name == 'type':
                type = type.type
            ans += type.print_type
        ans += '"'
        for p in readstatement.variable_list:
            ans += ', &' + str(p)
        ans += ');'
        self.print(' ' * 4 * self.depth + ans)
        return ans

    def WriteGenerate(self, printstatement):
        ans = 'printf("'
        for p in printstatement.expression_list:
            type = p.type
            while type.name == 'type':
                type = type.type
            ans += type.print_type
        if printstatement.newline:
            ans += '\\n'
        ans += '"'
        for p in printstatement.expression_list:
            ans += ', ' + str(p)
        ans += ');'
        self.print(' ' * 4 * self.depth + ans)
        return ans
    
    def WhileGenerate(self, whilestatement):
        self.print(' ' * 4 * self.depth + 'while (' + str(whilestatement.expression) +
              ')')
        if whilestatement.statement.information.name == 'compound_statement':
            self.StatementGenerate(whilestatement.statement)
        else:
            self.depth += 1
            self.StatementGenerate(whilestatement.statement)
            self.depth -= 1
    
    def RepeatGenerate(self, repeatstatement):
        self.print(' ' * 4 * self.depth + 'do')
        self.depth += 1
        for statement in repeatstatement.statement_list:
            self.StatementGenerate(statement)
        self.depth -= 1
        self.print(' ' * 4 * self.depth + 'while (!(' + str(repeatstatement.expression) + '));')
