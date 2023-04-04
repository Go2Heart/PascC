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
            print(item["type"].generate(id) + ';')

        for ids in program.var_idlist:
            item = self.symboltable.getItem(ids[0])
            # print(item)
            print(item["type"].generate(*ids) + ';')

        for subprogram in program.subprogram_list:
            self.symboltable.recover_function()
            self.SubProgramGenerate(subprogram)

        print("int main()")
        print("{")
        print(' ' * 4 + "return 0;")
        print("}")

        self.symboltable.popblock()

    def SubProgramGenerate(self, subprogram):
        # 进入块
        self.depth += 1
        self.symboltable.pushblock()  # 进入到一个块中了，更新索引表

        self.symboltable.recover_const_var()

        item = self.symboltable.getItem(subprogram.name)
        print(item["type"].generate(subprogram.name, subprogram.parameter_idlist))

        print('{')
        for id in subprogram.const_idlist:
            item = self.symboltable.getItem(id)
            print(' ' * 4 * self.depth + item["type"].generate(id) + ';')

        for ids in subprogram.var_idlist:
            item = self.symboltable.getItem(ids[0])
            # print(item)
            print(' ' * 4 * self.depth + item["type"].generate(*ids) + ';')

        print('}')

        self.symboltable.popblock()
        self.depth -= 1
