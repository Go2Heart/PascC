"""pparser is a module for parsing the output of the p command in Linux.

Typical usage example:
parser = PParser()
parser.parse(script)
"""
import sys, os

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
        
    precedence = (
        ('left', 'ELSE'),
        ('left', 'LPAREN', 'LBRACK'),
        ('right', 'ASSIGN')
    )

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
        """program_body : const_declarations var_declarations subprogram_declarations compound_statement"""
        p[0] = ASTNode(("program_body"), p[1], p[2], p[3], p[4])

    def p_const_declarations(self, p):
        """const_declarations : CONST const_declaration SEMI
                              | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("const_declarations"), *p[2])

    def p_const_declaration(self, p):
        """const_declaration : ID EQU const_value 
                             | const_declaration SEMI ID EQU const_value"""
        if len(p) == 4:
            p[0] = [
                ASTNode(("const_declaration",), ASTNode(("id", p[1])), p[3])
            ]
        elif len(p) == 6:
            p[0] = p[1] + [
                ASTNode(("const_declaration",), ASTNode(("id", p[3])), p[5])
            ]

    def p_const_value(self, p):
        """const_value : ADDOP ICONST
                       | ICONST
                       | CCONST""" 
        if len(p) == 3:
            p[0] = ASTNode(("integer", p[1] + str(p[2])))
        else:
            if isinstance(p[1], int):
                p[0] = ASTNode(("integer", p[1]))
            else:
                p[0] = ASTNode(("char", p[1]))

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
            p[0] = ASTNode(("array_type",), p[3], p[6])

    def p_basic_type(self, p):
        """basic_type : INTEGER
                      | REAL
                      | CHAR
                      | STRING
                      | BOOLEAN"""
        p[0] = ASTNode((p[1],))

    def p_period(self, p):
        """period : ICONST DOTDOT ICONST
                  | period COMMA ICONST DOTDOT ICONST"""
        if len(p) == 4:
            p[0] = ASTNode(("period"), ASTNode(("const_value", p[1])),
                           ASTNode(("const_value", p[3])))
        elif len(p) == 6:
            p[0] = ASTNode(("period"), *p[1].childs,
                           ASTNode(("const_value", p[3])),
                           ASTNode(("const_value", p[5])))
        # TODO what if the period is not a const value?

    def p_subprogram_declarations(self, p):
        """subprogram_declarations : subprogram_declarations subprogram SEMI
                                   | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("subprogram_declarations"), *p[1].childs, p[2])
        elif len(p) == 2:
            p[0] = ASTNode(("subprogram_declarations"))

    def p_subprogram(self, p):
        """subprogram : subprogram_head SEMI subprogram_body"""
        p[0] = ASTNode(("subprogram"), p[1], p[3])

    def p_subprogram_head(self, p):
        """subprogram_head : PROCEDURE ID formal_parameter
                           | FUNCTION ID formal_parameter COLON basic_type"""
        if len(p) == 4:
            p[0] = ASTNode(("procedure_head", p[2]), p[3])
        elif len(p) == 6:
            p[0] = ASTNode(("function_head", p[2]), p[3], p[5])

    def p_formal_parameter(self, p):
        """formal_parameter : LPAREN parameter_list RPAREN
                            | empty"""
        # test

        if len(p) == 4:
            p[0] = ASTNode(("formal_parameter"), p[2])

    def p_parameter_list(self, p):
        """parameter_list : parameter_list SEMI parameter
                          | parameter"""
        if len(p) == 4:
            p[0] = ASTNode(("parameter_list"), *p[1].childs, p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("parameter_list"), p[1])

    def p_parameter(self, p):
        """parameter : var_parameter
                     | value_parameter"""
        p[0] = p[1]

    def p_var_parameter(self, p):
        """var_parameter : VAR value_parameter"""
        p[0] = ASTNode(("var_parameter"), p[2])

    def p_value_parameter(self, p):
        """value_parameter : idlist COLON basic_type"""
        p[0] = ASTNode(("value_parameter"), *p[1].childs, p[3])

    def p_subprogram_body(self, p):
        """subprogram_body : const_declarations var_declarations compound_statement"""
        p[0] = ASTNode(("subprogram_body"), p[1], p[2], p[3])

    def p_compound_statement(self, p):
        """compound_statement : BEGIN statement_list END"""
        p[0] = ASTNode(("compound_statement"), p[2])

    def p_statement_list(self, p):
        """statement_list : statement_list SEMI statement
                          | statement"""
        if len(p) == 4:
            p[0] = ASTNode(("statement_list"), *p[1].childs, p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("statement_list"), p[1])

    def p_statement(self, p):
        """statement : variable ASSIGN expression
                     | ID ASSIGN expression
                     | procedure_call
                     | compound_statement
                     | IF expression THEN statement else_part
                     | FOR ID ASSIGN expression TO expression DO statement
                     | READ LPAREN variable_list RPAREN
                     | WRITE LPAREN expression_list RPAREN"""
        if len(p) == 4:
            if isinstance(p[1], ASTNode):
                p[0] = ASTNode(("assignment_statement"), p[1],
                               p[3])
            else:
                p[0] = ASTNode(("assignment_statement"), ASTNode(("fun_id"), p[1]),
                           p[3])
        elif len(p) == 2:
            p[0] = p[1]
        elif len(p) == 6:
            p[0] = ASTNode(("if_statement"), p[2], p[4], p[5])
        elif len(p) == 9:
            p[0] = ASTNode(("for_statement"), ASTNode(("id", p[2])), p[4],
                           p[6], p[8])
        elif p[1].lower() == "read":
            p[0] = ASTNode(("read_statement"), p[3])
        elif p[1].lower() == "write":
            p[0] = ASTNode(("write_statement"), p[3])

    def p_variable_list(self, p):
        """variable_list : variable_list COMMA variable
                         | variable"""
        if len(p) == 4:
            p[0] = ASTNode(("variable_list"), *p[1].childs, p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("variable_list"), p[1])

    def p_variable(self, p):
        """variable : ID id_varpart"""
        if p[2] is not None:
            p[0] = ASTNode(("variable"), ASTNode(("id", p[1])), p[2])
        else:
            p[0] = ASTNode(("variable"), ASTNode(("id", p[1])))

    def p_id_varpart(self, p):
        """id_varpart : LBRACK expression RBRACK
                      | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("id_varpart"), p[2])

    def p_procedure_call(self, p):
        """procedure_call : ID
                          | ID LPAREN expression_list RPAREN"""
        if len(p) == 2:
            p[0] = ASTNode(("procedure_call"), ASTNode(("id", p[1])))
        elif len(p) == 5:
            p[0] = ASTNode(("procedure_call"), ASTNode(("id", p[1])), p[3])

    def p_else_part(self, p):
        """else_part : ELSE statement
                     | empty"""
        if len(p) == 3:
            p[0] = p[2]

    def p_expression_list(self, p):
        """expression_list : expression_list COMMA expression
                           | expression"""
        if len(p) == 4:
            p[0] = ASTNode(("expression_list"), *p[1].childs, p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("expression_list"), p[1])

    def p_expression(self, p):
        """expression : simple_expression RELOP simple_expression
                      | simple_expression EQU simple_expression
                      | simple_expression"""
        if len(p) == 4:
            p[0] = ASTNode(("expression"), p[1], p[2], p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("expression"), p[1])

    def p_simple_expression(self, p):
        """simple_expression : simple_expression ADDOP term
                             | term"""
        if len(p) == 4:
            p[0] = ASTNode(("simple_expression"), p[1], p[2], p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("simple_expression"), p[1])

    def p_term(self, p):
        """term : term MULDIVANDOP factor
                | factor"""
        if len(p) == 4:
            p[0] = ASTNode(("term"), p[1], p[2], p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("term"), p[1])

    def p_factor(self, p):
        """factor : number
                  | variable
                  | ID LPAREN expression_list RPAREN
                  | NOTOP factor
                  | ADDOP factor"""
        if len(p) == 2:
            p[0] = ASTNode(("factor"), p[1])
        elif len(p) == 5:
            p[0] = ASTNode(("factor"), ASTNode(("id", p[1])), p[3])
        elif len(p) == 3:
            p[0] = ASTNode(("factor"), p[1], p[2])

    def p_number(self, p):
        """number : ICONST
                  | RCONST"""
        p[0] = ASTNode(("number", p[1]))

    def p_empty(self, p):
        """empty :"""
        pass

    def p_error(self, p):
        """error handler"""
        print("Line {1}: Syntax error '{0}'".format(p.value, p.lineno))
        # print("Syntax error at '%s'" % p.value, p.lineno, p.lexpos)


if __name__ == "__main__":
    parser = Parser()
    with open("./test/gcd.pas", "r") as f:
        node = parser.parse(f.read())
        f.close()
    node.print(output_file=open("test/gcd.ast", "w"))
    # node.print(output_file=open("test/gcd.ast", "w", encoding='utf-8')
    # node.json_print(output_file=open("test/gcd_ast.json", "w", encoding='utf-8'))
    pass
