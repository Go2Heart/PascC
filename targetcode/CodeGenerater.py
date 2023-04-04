class CodeGenerater(object):
    # 基于 符号表symboltable，类型表typestable，根节点program进行代码生成
    def __init__(self, symboltable, typestable):
        self.symboltable = symboltable
        self.typestable = typestable
        self.depth = 0

    def ProgramGenerate(self, program):

        # 索引块初始化
        self.symboltable.setIndexStack()

        # 进入块
        self.symboltable.pushblock()  # 进入到一个块中了，更新索引表

        print("#include<stdio.h>")
        self.symboltable.recover_const_var()

        for id in program.const_idlist:
            item = self.symboltable.getItem(id)
            print(item["type"].generate(False, id) + ';')

        for ids in program.var_idlist:
            item = self.symboltable.getItem(ids[0])
            # print(item)
            print(item["type"].generate(False, *ids) + ';')

        for subprogram in program.subprogram_list:
            self.symboltable.recover_function()
            self.SubProgramGenerate(subprogram)

        print("int main()")
        print("{")
        self.depth += 1
        self.CompoundGenerate(program.compound_statement)
        print(' ' * 4 * self.depth + "return 0;")
        self.depth -= 1
        print("}")

        self.symboltable.popblock()

    def SubProgramGenerate(self, subprogram):
        # 进入块
        self.symboltable.pushblock()  # 进入到一个块中了，更新索引表

        self.symboltable.recover_const_var()

        item = self.symboltable.getItem(subprogram.name)
        print(item["type"].generate(False, subprogram.name,
                                    subprogram.parameter_idlist))

        print('{')
        self.depth += 1
        for id in subprogram.const_idlist:
            item = self.symboltable.getItem(id)
            print(' ' * 4 * self.depth + item["type"].generate(False, id) + ';')

        for ids in subprogram.var_idlist:
            item = self.symboltable.getItem(ids[0])
            # print(item)
            print(' ' * 4 * self.depth + item["type"].generate(False, *ids) + ';')

        self.CompoundGenerate(subprogram.compound_statement)
        self.depth -= 1
        print('}')

        self.symboltable.popblock()

    def StatementGenerate(self, statement):
        if statement.information.name == 'compound_statement':
            print(' ' * 4 * self.depth + '{')
            self.depth += 1
            self.CompoundGenerate(statement.information)
            self.depth -= 1

            print(' ' * 4 * self.depth + '}')

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

    def CompoundGenerate(self, compoundstatement):
        for statement in compoundstatement.statements:
            self.StatementGenerate(statement)

    def AssignmentGenerate(self, assignmentstatement):
        if assignmentstatement.is_function:
            print(' ' * 4 * self.depth + 'return ' +
                  str(assignmentstatement.expression) + ';')
        else:
            print(' ' * 4 * self.depth + str(assignmentstatement.variable) +
                  ' = ' + str(assignmentstatement.expression) + ';')

    def EmptyGenerate(self, statement):
        print(' ' * 4 * self.depth + ';')
        pass

    def IfGenerate(self, statement):
        print(' ' * 4 * self.depth + 'if (' + str(statement.if_expression) +
              ')')
        if statement.then_statement.information.name == 'compound_statement':
            self.StatementGenerate(statement.then_statement)
        else:
            self.depth += 1
            self.StatementGenerate(statement.then_statement)
            self.depth -= 1
        if statement.else_statement:
            print(' ' * 4 * self.depth + 'else')
            if statement.else_statement.information.name == 'compound_statement':
                self.StatementGenerate(statement.else_statement)
            else:
                self.depth += 1
                self.StatementGenerate(statement.else_statement)
                self.depth -= 1

    def ForGenerate(self, forstatement):
        print(' ' * 4 * self.depth + 'for (' + str(forstatement.id) + ' = ' +
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
            ans += p.type.print_type
        ans += '"'
        for p in readstatement.variable_list:
            ans += ', &' + str(p)
        ans += ');'
        print(' ' * 4 * self.depth + ans)
        return ans

    def WriteGenerate(self, printstatement):
        ans = 'printf("'
        for p in printstatement.expression_list:
            ans += p.type.print_type
            if printstatement.newline:
                ans += '\\n'
        ans += '"'
        for p in printstatement.expression_list:
            ans += ', ' + str(p)
        ans += ');'
        print(' ' * 4 * self.depth + ans)
        return ans
