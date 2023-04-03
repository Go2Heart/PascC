import logging
import Statements
import SubPrograms


class Program(object):
    """program : program_head SEMI program_body DOT"""
    def __init__(self, node, symboltable, typestable):
        # 进入块
        symboltable.pushblock()  # 进入到一个块中了，符号表重定位

        # 程序名
        tmp = node.childs[0]  # tmp=('program_head', 'example')
        self.name = tmp.type[1]  # example
        logging.debug('program.name=' + self.name)

        # 参数表
        tmp = tmp.childs[0]  # tmp=idlist
        if tmp is None:
            self.parameter_idlist = []
        else:
            self.parameter_idlist = [x.type[1] for x in tmp.childs
                                     ]  # ['id1', 'id2', 'id3']
        logging.debug('program.parameter_idlist=' + str(self.parameter_idlist))

        # 将常量加入符号表
        self.const_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=const_declaration
                id = x.childs[0].type[1]  # id = 'id1'
                type = typestable.get_type(x)
                if symboltable.haveItem(id):
                    print("重复声明")
                else:
                    symboltable.insertItem(id, type, [], [])
                    self.const_idlist.append(id)
        logging.debug('program.const_idlist=' + str(self.const_idlist))

        # 将变量加入符号表
        self.var_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[1]  # tmp=var_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=var_declaration
                type = typestable.get_type(x.childs[-1])
                ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
                for id in ids:
                    if symboltable.haveItem(id):
                        print("重复声明")
                    else:
                        symboltable.insertItem(id, type, [], [])
                        self.var_idlist.append(id)
        logging.debug('program.var_idlist=' + str(self.var_idlist))

        # 将子程序加入符号表
        self.subprogram_list = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[2]  # tmp=subprogram_declarations
        for x in tmp.childs:  # x=subprogram
            id = x.childs[0].type[1]  # id = 'id1'
            type = typestable.get_type(x.childs[0])
            if symboltable.haveItem(id):
                print("重复声明")
            else:
                symboltable.insertItem(id, type, [], [])
                self.subprogram_list.append(
                    SubPrograms.SubProgram(x, symboltable, typestable))

                logging.debug('Program:SymbolTable')
                symboltable.print()

        # 处理语句块
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[3]  # tmp=compound_statement
        self.compound_statement = Statements.CompoundStatement(
            tmp, symboltable, typestable)

        # 退出块
        symboltable.popblock()  # 退出当前块，符号表重定位
