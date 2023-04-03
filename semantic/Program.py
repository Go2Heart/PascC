import sys, os
# 系统搜索路径加入当前路径和上一级路径，避免受到运行时目录的影响
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lexical_syntactic import pparser
from Types import Types
from SymbolTable import SymbolTable
import logging
import Statements
import SubPrograms

logging.basicConfig(level=logging.DEBUG)


class Program(object):
    """program : program_head SEMI program_body DOT"""
    def __init__(self, node):
        # 进入块
        SymbolTable.pushblock()  # 进入到一个块中了，符号表重定位

        # 程序名
        tmp = node.childs[0]  # tmp=('program_head', 'example')
        self.name = tmp.type[1]  # example
        logging.debug('program.name=' + self.name)

        # 参数表
        tmp = tmp.childs[0]  # tmp=idlist
        self.parameter_idlist = [x.type[1]
                                 for x in tmp.childs]  # ['id1', 'id2', 'id3']
        logging.debug('program.parameter_idlist=' + str(self.parameter_idlist))

        # 将常量加入符号表
        self.const_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        for x in tmp.childs:  # x=const_declaration
            id = x.childs[0].type[1]  # id = 'id1'
            type = Types.get_type(x)
            if SymbolTable.haveItem(id):
                print("重复声明")
            else:
                SymbolTable.insertItem(id, type, [], [])
                self.const_idlist.append(id)
        logging.debug('program.const_idlist=' + str(self.const_idlist))

        # 将变量加入符号表
        self.var_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[1]  # tmp=var_declarations
        for x in tmp.childs:  # x=var_declaration
            type = Types.get_type(x.childs[-1])
            ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
            for id in ids:
                if SymbolTable.haveItem(id):
                    print("重复声明")
                else:
                    SymbolTable.insertItem(id, type, [], [])
                    self.var_idlist.append(id)
        logging.debug('program.var_idlist=' + str(self.var_idlist))

        # 将子程序加入符号表
        self.subprogram_list = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[2]  # tmp=subprogram_declarations
        for x in tmp.childs:  # x=subprogram
            id = x.childs[0].type[1]  # id = 'id1'
            type = Types.get_type(x.childs[0])
            if SymbolTable.haveItem(id):
                print("重复声明")
            else:
                SymbolTable.insertItem(id, type, [], [])
                self.subprogram_list.append(SubProgram(x))

        SymbolTable.print()

        # 处理语句块
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[3]  # tmp=compound_statement
        self.compound_statement = 

        # 退出块
        SymbolTable.popblock()  # 退出当前块，符号表重定位



class SemanticAnalyzer(object):
    def init(self, node):
        self.node = node

    def ProgramAnalysis(self, node):
        """program : program_head SEMI program_body DOT"""


if __name__ == "__main__":
    parser = pparser.Parser()
    with open("./test/gcd.pas", "r") as f:
        node = parser.parse(f.read())
        f.close()
    a = Program(node)
    # node.print(output_file=open("test/gcd.ast", "w", encoding='utf-8')
    # node.json_print(output_file=open("test/gcd_ast.json", "w", encoding='utf-8'))
    pass
