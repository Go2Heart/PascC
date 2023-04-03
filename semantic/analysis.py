import sys

sys.path.append('..')
from lexical_syntactic import parser
from Types import Types
from SymbolTable import SymbolTable


class Program(object):
    """program : program_head SEMI program_body DOT"""
    def __init__(self, node):
        # 进入块
        SymbolTable.pushblock()  # 进入到一个块中了，符号表重定位

        # 程序名
        tmp = node.childs[0]  # tmp=('program_head', 'example')
        self.name = tmp[1]  # example

        # 参数表
        tmp = tmp.childs[0]  # tmp=idlist
        self.parameter_idlist = [x[1]
                                 for x in tmp.childs]  # ['id1', 'id2', 'id3']

        # 将常量加入符号表
        self.const_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        for x in tmp.childs:  # x=const_declaration
            id = x.childs[0][1]  # id = 'id1'
            type = Types.get_type(x)
            SymbolTable.insertItem(id, type, [], [])
            self.const_idlist.append(id)

        # 将变量加入符号表
        self.var_idlist = []
        
        # 将子程序加入符号表

        # 处理语句块

        # 退出块
        SymbolTable.popblock()  # 退出当前块，符号表重定位


class SemanticAnalyzer(object):
    def init(self, node):
        self.node = node

    def ProgramAnalysis(self, node):
        """program : program_head SEMI program_body DOT"""
