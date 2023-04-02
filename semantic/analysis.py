import sys

sys.path.append('..')
from lexical_syntactic import parser
import Types

class SemanticAnalyzer(object):
    def init(self, node):
        self.node = node

    def ProgramAnalysis(self, node):
        
