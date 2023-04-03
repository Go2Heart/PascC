import sys, os
# 系统搜索路径加入当前路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Program import Program


class Analyzer(object):
    def __init__(self, symboltable,  typestable):
        self.symboltable = symboltable
        self.typestable = typestable

    def analyse(self, node):
        return Program(node, self.symboltable, self.typestable)
