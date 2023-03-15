"""pparser is a module for parsing the output of the p command in Linux.

Typical usage example:
parser = PParser()
parser.parse(script)
"""
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ply.yacc import yacc
from plexer import Lexer
from ast_node import ASTNode


class Parser:
    """Parse the script and return the AST
    
    Attributes:
        _lexer: the lexer
        tokens: the tokens
        _yacc: the yacc parser
    """
    
    def __init__(self):
        """init the parser"""
        self._lexer = Lexer()
        self.tokens = self._lexer.tokens
        self._yacc = yacc(module=self)
        
    def parse(self, script):
        """parse the script
        
        Args:
            script: the script to be parsed
        """
        return self._yacc.parse(script, lexer=self._lexer.get_lexer())
        
    def p_program(self, p):
        """program : program_head SEMI program_body DOT"""
        p[0] = ASTNode(("program"), p[1], p[3])
    
    def p_program_head(self, p):
        """program_head : PROGRAM ID 
                        | PROGRAM ID LPAREN idlist RPAREN"""

        if len(p) == 3:
            p[0] = ASTNode(("program_head", p[2]))
        elif len(p) == 6:
            p[0] = ASTNode(("program_head", p[2]), p[4])
    
    def p_idlist(self, p):
        """idlist : idlist COMMA ID
                  | ID"""
        if len(p) == 2:
            p[0] = ASTNode(("idlist"), ASTNode(("id", p[1])))
        elif len(p) == 4:
            p[0] = ASTNode(("idlist"), *p[1].childs, ASTNode(("id", p[3])))
            
    def p_program_body(self, p):
        """program_body : const_declarations var_declarations subprogram_declarations """
        p[0] = ASTNode(("program_body"), p[1], p[2], p[3])
        
    def p_const_declarations(self, p):
        """const_declarations : CONST const_declaration SEMI
                              | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("const_declarations"), *p[2])
         
    def p_const_declaration(self, p):
        """const_declaration : ID EQU const_value 
                             | const_declaration SEMI ID EQU const_value"""
        if len(p) == 4:
            p[0] = [ASTNode(("const_declaration"), ASTNode(("id", p[1])), p[3])]
        elif len(p) == 6:
            p[0] = p[1] + [ASTNode(("const_declaration"), ASTNode(("id", p[3])), p[5])]
        
    def p_const_value(self, p):
        """const_value : ADDOP ICONST
                       | ICONST
                       | ID"""
        p[0] = ASTNode(("const_value", p[1]))
        
    def p_var_declarations(self, p):
        """var_declarations : VAR var_declaration SEMI
                            | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("var_declarations"), *p[2])
            
    def p_var_declaration(self, p):
        """var_declaration : idlist COLON type
                           | var_declaration SEMI idlist COLON type"""
        if len(p) == 4:
            p[0] = [ASTNode(("var_declaration"), *p[1].childs, p[3])]
        elif len(p) == 6:
            p[0] = p[1] + [ASTNode(("var_declaration"), *p[3].childs, p[5])]
            
    def p_type(self, p):
        """type : basic_type
                | ARRAY LBRACK period RBRACK OF basic_type"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 7:
            p[0] = ASTNode(("array_type"), p[3], p[6])
            
    def p_basic_type(self, p):
        """basic_type : INTEGER
                      | REAL
                      | CHAR
                      | STRING"""
        p[0] = ASTNode(("basic_type", p[1]))
    
    def p_period(self, p):
        """period : ICONST DOTDOT ICONST
                  | period COMMA ICONST DOTDOT ICONST"""
        if len(p) == 4:
            p[0] = ASTNode(("period"), ASTNode(("const_value", p[1])), ASTNode(("const_value", p[3])))
        elif len(p) == 6:
            p[0] = ASTNode(("period"), *p[1].childs, ASTNode(("const_value", p[3])), ASTNode(("const_value", p[5])))
        # TODO what if the period is not a const value?
        
    
    def p_empty(self, p):
        """empty :"""
        pass
    
    def p_error(self, p):
        """error handler"""
        print("Syntax error at '%s'" % p.value)
        
    
            
            

if __name__ == "__main__":
    parser = Parser()
    with open("test/test_parser.pas", "r") as f:
        node = parser.parse(f.read())
        f.close()
    node.print()
    
    