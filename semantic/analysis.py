import sys

sys.path.append('..')
from lexical_syntactic import parser
import Types
import SymbolTable


class Program(object):
    """program : program_head SEMI program_body DOT"""
    def __init__(self, node):
        tmp = node.childs[0]  # tmp=('program_head', 'example')
        self.name = tmp[1]  # example
        tmp = tmp.childs[0]  # tmp=idlist
        self.parameter_idlist = [x.second
                                 for x in tmp.childs]  # ['id1', 'id2', 'id3']
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        self.const_idlist = []
        for x in tmp.childs:  # x=const_declaration
            id = x.childs[0].second  # id = 'id1'
            val = x.childs[1].second  # val = 123
            SymbolTable


class SemanticAnalyzer(object):
    def init(self, node):
        self.node = node

    def ProgramAnalysis(self, node):
        """program : program_head SEMI program_body DOT"""
