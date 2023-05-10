""" Stub modules for each
"""
import json
import objtyping

class Token:
    def __init__(self, type, data, len, pos):
        self.type = type
        self.data = data
        self.len  = len
        self.pos  = pos

class ASTNode:
    def __init__(self):
        self.type: str
        self.childs: list[ASTNode]

class StubParser:
    """STUB for semantic tree"""
    def __init__(self):
        self._node = None
    def get_node(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            json_obj = json.loads(f.read())
        self._node = objtyping.from_primitive(json_obj, ASTNode)
        return self._node
class StubLexer:
    """STUB for AST"""
    def get_tokens(self,path):
        tokens = []
        with open(path, 'r', encoding='utf-8') as f:
            raw_tokens = f.readlines()
        for line in raw_tokens:
            infos = line[9:line.rfind(')')].split(',')
            tokens.append(Token(infos[0],infos[1], infos[2], infos[3]))
        return tokens
    pass


if __name__ == '__main__':
    lex_test = StubLexer()
    lex_test.get_tokens('bubble.out')
    # jsonRead = StubParser()
    # typed_obj =jsonRead.get_node("test/gcd_ast.json")
    # d_l_obj = objtyping.to_primitive(typed_obj)
    # json.dump(d_l_obj, open("test/gcd_ast_test.json",'w',encoding='utf-8'),indent=4)
    pass