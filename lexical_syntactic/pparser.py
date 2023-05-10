"""pparser is a module for parsing the output of the p command in Linux.

Typical usage example:
parser = PParser()
parser.parse(script)
"""
from distutils.log import debug
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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
    def __init__(self,lens):
        """init the parser"""
        self._lexer = Lexer()
        self.tokens = self._lexer.tokens
        self._yacc = yacc(module=self)
        self.Lexerror = False
        self.yaccerror = False
        self.errormes = []
        self.lens=lens

    precedence = (('left', 'ELSE'), ('left', 'LPAREN', 'LBRACK'), ('right',
                                                                   'ASSIGN'))#???
    def p_error(self, p):
        """error handler"""
        self.yaccerror = True
        if(p!=None):
            self.errormes.append("Line {1}: Syntax error '{0}'".format(p.value, p.lineno))
        else:
            self.errormes.append("Line {1}: Syntax error in the last word".format('',self.lens))
        # self._yacc.errok()
        # print("Syntax error at '%s'" % p.value, p.lineno, p.lexpos)

    def parse(self, script):
        """parse the script
        
        Args:
            script: the script to be parsed
        """
        renode = self._yacc.parse(script, lexer=self._lexer.get_lexer(),debug=False)
        if(self._lexer.errorFlag):
            self.Lexerror = True
            for me in self._lexer.errormes:
                print(me)
        return renode

    def p_program(self, p):
        """program : program_head SEMI program_body DOT"""
        p[0] = ASTNode(("program",p.lineno(2)), p[1], p[3])

    def p_wrong_program(self, p):
        """program : program_head SEMI program_body"""
        p[0] = ASTNode(("program"), p[1], p[3])
        self.yaccerror = True
        self.errormes.append("Line {0}: Syntax error ,lost symbol '.'".format(self.lens))

    def p_program_head(self, p):
        """program_head : PROGRAM ID 
                        | PROGRAM ID LPAREN idlist RPAREN"""

        if len(p) == 3:
            p[0] = ASTNode(("program_head", p[2]), None)
        elif len(p) == 6:
            p[0] = ASTNode(("program_head", p[2]), p[4])

    def p_idlist(self, p):
        """idlist : idlist COMMA ID
                  | ID"""
        if len(p) == 2:
            p[0] = ASTNode(("idlist"), ASTNode(("id", p[1],p.lineno(1))))
        elif len(p) == 4:
            p[0] = ASTNode(("idlist"), *p[1].childs, ASTNode(("id", p[3],p.lineno(3))))

    def p_wrong_idlist(self, p):
        """idlist : idlist error ID
                  | ID error"""
        if len(p) == 3:
            p[0] = ASTNode(("idlist"), ASTNode(("id", p[1])))
        elif len(p) == 4:
            p[0] = ASTNode(("idlist"), *p[1].childs, ASTNode(("id", p[3])))

    def p_program_body(self, p):
        """program_body : const_declarations type_declarations var_declarations subprogram_declarations compound_statement"""
        p[0] = ASTNode(("program_body"), p[1], p[2], p[3], p[4], p[5])
        
    def p_type_declarations(self, p):
        """type_declarations : TYPE type_declaration SEMI
                             | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("type_declarations"), *p[2])
        else:
            p[0] = None
            
    def p_type_declaration(self, p):
        """type_declaration : ID EQU type_define
                            | type_declaration SEMI ID EQU type_define"""
        if len(p) == 4:
            p[0] = [
                ASTNode(("type_declaration", ), ASTNode(("id", p[1],p.lineno(1))), p[3])
            ]
        elif len(p) == 6:
            p[0] = p[1] + [
                ASTNode(("type_declaration", ), ASTNode(("id", p[3],p.lineno(3))), p[5])
            ]

    def p_type_define(self, p):
        """type_define : simple_type
                    | array_type
                    | record_type"""
        p[0] = p[1]

    def p_simple_type(self, p):
        """simple_type : ID
                    | LPAREN ID DOTDOT ID RPAREN"""
        if len(p) == 2:
            p[0] = ASTNode(("simple_type", "ID"), p[1])
        else:
            p[0] = ASTNode(("simple_type", "range"), p[2], p[4])

    def p_array_type(self, p):
        """array_type : ARRAY LPAREN index_range RPAREN OF ID"""
        p[0] = ASTNode(("array_type", p[3]), p[6])

    def p_index_range(self, p):
        """index_range : simple_type DOTDOT simple_type"""
        p[0] = ASTNode(("index_range"), p[1], p[3])

    def p_record_type(self, p):
        """record_type : RECORD field_declarations END"""
        p[0] = ASTNode(("record_type"), *p[2])

    def p_field_declarations(self, p):
        """field_declarations : field_declaration SEMI
                            | field_declarations field_declaration SEMI"""
        if len(p) == 3:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_field_declaration(self, p):
        """field_declaration : ID COLON ID 
                            | ID COLON basic_type"""
        p[0] = ASTNode(("field_declaration", p[1]), p[3])


        
    
    def p_const_declarations(self, p):
        """const_declarations : CONST const_declaration SEMI
                              | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("const_declarations"), *p[2])
        else:
            p[0] = None

    def p_const_declaration(self, p):
        """const_declaration : ID EQU const_value 
                             | const_declaration SEMI ID EQU const_value"""
        if len(p) == 4:
            p[0] = [
                ASTNode(("const_declaration", ), ASTNode(("id", p[1],p.lineno(1))), p[3])
            ]
        elif len(p) == 6:
            p[0] = p[1] + [
                ASTNode(("const_declaration", ), ASTNode(("id", p[3],p.lineno(3))), p[5])
            ]

    def p_wrong_const_declaration(self, p):
        """const_declaration : ID EQU error ID
                             | const_declaration SEMI ID EQU error ID"""
        if len(p) == 5:
            p[0] = [
                ASTNode(("const_declaration", ), ASTNode(("id", p[1])), ASTNode(("string",'0')))
            ]
            #print(*p)
        elif len(p) == 7:
            p[0] = p[1] + [
                ASTNode(("const_declaration", ), ASTNode(("id", p[3])), ASTNode(("string",'0')))
            ]       

    def p_const_value(self, p):
        """const_value : ADDOP ICONST
                    | ICONST
                    | RCONST
                    | CCONST
                    | BCONST
                    | string"""
        # 进行了一个大改
        # 这里有一个需要注意的细节，应该先判断是不是boolean再判断是不是int，因为在python里bool是int的子类
        if len(p) == 3:
            p[0] = ASTNode(("integer", int(p[1] + str(p[2]))))
        elif isinstance(p[1], bool):
            p[0] = ASTNode(("boolean", p[1]))
        elif isinstance(p[1], int):
            p[0] = ASTNode(("integer", p[1]))
        elif isinstance(p[1], float):
            p[0] = ASTNode(("real", p[1]))
        elif isinstance(p[1], str):
            p[0] = ASTNode(("char", p[1]))
        elif isinstance(p[1], ASTNode):
            p[0] = p[1]

    def p_var_declarations(self, p):
        """var_declarations : VAR var_declaration SEMI
                            | empty"""
        if len(p) == 4:
            p[0] = ASTNode(("var_declarations"), *p[2])
        else:
            p[0] = None

    ''' def p_wrong_var_declarations(self, p):
        """var_declarations : var_declaration SEMI"""
        if len(p) == 3:
            p[0] = ASTNode(("var_declarations"), *p[1])
        else:
            p[0] = None'''#做不到恢复，会跟常量定义冲突

    def p_var_declaration(self, p):
        """var_declaration : idlist COLON type
                           | var_declaration SEMI idlist COLON type"""
        if len(p) == 4:
            p[0] = [ASTNode(("var_declaration"), *p[1].childs, p[3])]
        elif len(p) == 6:
            p[0] = p[1] + [ASTNode(("var_declaration"), *p[3].childs, p[5])]

    def p_type(self, p):
        """type : basic_type
                | ARRAY LBRACK period RBRACK OF basic_type
                | ID"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 7:
            p[0] = ASTNode(("array_type", p.lineno(1)), p[3], p[6])

    def p_basic_type(self, p):
        """basic_type : INTEGER
                      | REAL
                      | CHAR
                      | BOOLEAN
                      | TYPE_STRING"""
        # 多了一个STRING
        # TODO：string的代码生成
        p[0] = ASTNode((p[1], ))

    def p_my_period_part(self, p):
        """my_period_part : ADDOP ICONST
                          | ICONST
                          | CCONST
                          | ID"""
        if len(p) == 3:
            p[0] = ASTNode(("integer", int(p[1] + str(p[2]))))
        else:
            if isinstance(p[1], int):
                p[0] = ASTNode(("integer", p[1]))
            elif p[1].startswith('\''):
                p[0] = ASTNode(("char", p[1]))
            else:
                p[0]= ASTNode(('id',p[1],p.lineno(1)))

    def p_period(self, p):
        """period : my_period_part DOTDOT my_period_part
                  | period COMMA my_period_part DOTDOT my_period_part"""
        # 做了改动，让数组下标元素可以是负数、可以是字符
        # print(p[1],type(p[1]))
        if len(p) == 4:
            p[0] = ASTNode(("period"), p[1], p[3])
        elif len(p) == 6:
            p[0] = ASTNode(("period"), *p[1].childs, p[3], p[5])
        # TODO what if the period is not a const value?
        # ans：带上ID作为下标，语义分析检查

    def p_wrong_period(self, p):
        """period : RCONST
                  | period COMMA RCONST"""
        # 做了改动，让数组下标元素可以是负数、可以是字符
        self.yaccerror=True
        if len(p) == 2:
            p[0] = ASTNode(("period"), ASTNode(("integer", 0)), ASTNode(("integer", 1)))
            self.errormes.append("Line {1}: Syntax error in {0}".format(p[1],p.lineno(1)))
        elif len(p) == 4:
            p[0] = ASTNode(("period"), *p[1].childs, ASTNode(("integer", 0)), ASTNode(("integer", 1)))
            self.errormes.append("Line {1}: Syntax error in {0}".format(p[3],p.lineno(3)))

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
            p[0] = ASTNode(("procedure_head", p[2],p.lineno(2)), p[3])
        elif len(p) == 6:
            p[0] = ASTNode(("function_head", p[2],p.lineno(2)), p[3], p[5])

    def p_formal_parameter(self, p):
        """formal_parameter : LPAREN parameter_list RPAREN
                            | empty"""
        # test

        if len(p) == 4:
            p[0] = ASTNode(("formal_parameter"), p[2])
        else:
            p[0] = None

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

    def p_wrong_value_parameter(self, p):
        """value_parameter : idlist error basic_type"""
        p[0] = ASTNode(("value_parameter"), *p[1].childs, p[3])

    def p_subprogram_body(self, p):
        """subprogram_body : const_declarations var_declarations compound_statement"""
        p[0] = ASTNode(("subprogram_body"), p[1], p[2], p[3])

    def p_compound_statement(self, p):
        """compound_statement : BEGIN statement_list END"""
        p[0] = ASTNode(("compound_statement",), p[2])

    def p_statement_list(self, p):
        """statement_list : statement_list SEMI statement
                          | statement"""
        if len(p) == 4:
            p[0] = ASTNode(("statement_list"), *p[1].childs, p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("statement_list"), p[1])

    def p_statement(self, p):
        """statement : empty
                     | variable ASSIGN expression
                     | procedure_call
                     | compound_statement
                     | IF expression THEN statement else_part
                     | FOR ID ASSIGN expression TO expression DO statement
                     | READ LPAREN variable_list RPAREN
                     | WRITE LPAREN expression_list RPAREN
                     | READLN LPAREN variable_list RPAREN
                     | WRITELN LPAREN expression_list RPAREN"""
        # 删去了不可能归约的产生式 | ID ASSIGN expression，以免产生混淆
        if len(p) == 4:
            p[0] = ASTNode(("assignment_statement",p.lineno(2)), p[1], p[3])
        elif len(p) == 2:
            if isinstance(p[1], ASTNode):  # compound_statement,procedure_call
                p[0] = p[1]
            else:  # p[1] is None
                p[0] = ASTNode(("empty_statement",))
        elif len(p) == 6:
            p[0] = ASTNode(("if_statement",p.lineno(1)), p[2], p[4], p[5])
        elif len(p) == 9:
            p[0] = ASTNode(("for_statement",), ASTNode(("id", p[2],p.lineno(2))), p[4],
                           p[6], p[8])
        elif p[1].lower() == "read":
            p[0] = ASTNode(("read_statement",p.lineno(1)), p[3])
        elif p[1].lower() == "write":
            p[0] = ASTNode(("write_statement",), p[3])
        elif p[1].lower() == "readln":
            p[0] = ASTNode(("read_statement",), p[3], True)
        elif p[1].lower() == "writeln":
            p[0] = ASTNode(("write_statement",), p[3], True)

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
            p[0] = ASTNode(("variable",p.lineno(1)), ASTNode(("id", p[1],p.lineno(1))), p[2])
        else:
            p[0] = ASTNode(("variable",p.lineno(1)), ASTNode(("id", p[1],p.lineno(1))))

    def p_id_varpart(self, p):
        """id_varpart : LBRACK expression_list RBRACK
                      | DOT ID id_varpart
                      | empty"""
        if len(p) == 4 and p[1] == '[':
            p[0] = ASTNode(("id_varpart"), p[2])
        elif len(p) == 4 and p[1] == '.':
            p[0] = ASTNode(("id_varpart"), (p[1], p[2]))
       

    def p_procedure_call(self, p):
        """procedure_call : ID
                          | ID LPAREN expression_list RPAREN"""
        if len(p) == 2:
            p[0] = ASTNode(("procedure_call",p.lineno(1)), ASTNode(("id", p[1])))
        elif len(p) == 5:
            p[0] = ASTNode(("procedure_call",p.lineno(1)), ASTNode(("id", p[1])), p[3])

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
            p[0] = ASTNode(("expression",p.lineno(2)), p[1], p[2], p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("expression"), p[1])

    def p_simple_expression(self, p):
        """simple_expression : simple_expression ADDOP term
                                | simple_expression OROP term
                             | term"""
        if len(p) == 4:
            p[0] = ASTNode(("simple_expression",p.lineno(2)), p[1], p[2], p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("simple_expression"), p[1])

    def p_term(self, p):
        """term : term MULDIVANDOP factor
                | factor"""
        if len(p) == 4:
            p[0] = ASTNode(("term",p.lineno(2)), p[1], p[2], p[3])
        elif len(p) == 2:
            p[0] = ASTNode(("term"), p[1])

    def p_factor(self, p):
        """factor : const_value
                  | variable
                  | LPAREN expression RPAREN
                  | ID LPAREN expression_list RPAREN
                  | NOTOP factor
                  | ADDOP factor"""
        # 漏产生式了啊喂！ factor->(expression)
        if len(p) == 2:
            if p[1].type[0] == "variable":
                p[0] = ASTNode(("factor", "variable"), p[1])
            else:
                p[0] = ASTNode(("factor", "constant"), p[1])
        elif len(p) == 3:
            p[0] = ASTNode(("factor", 'factor',p.lineno(1)), p[1], p[2])
        elif len(p) == 4:
            p[0] = ASTNode(("factor", 'expression'), p[2])
        elif len(p) == 5:
            p[0] = ASTNode(("factor", 'function'), ASTNode(("id", p[1],p.lineno(1))), p[3])

    def p_string(self, p):
        """string : STRING"""
        p[0] = ASTNode(("string", p[1]))

    def p_empty(self, p):
        """empty :"""
        pass



if __name__ == "__main__":
    with open("./test/addons.pas", "r") as f:
        line = f.readlines()
        lens = len(line)
        test_parser = Parser(lens)
        f.seek(0)
        node = test_parser.parse(f.read())
    node.print()
    # node.print()
    # node.print(output_file=open("test/gcd.ast", "w", encoding='utf-8')
    # node.json_print(output_file=open("test/gcd_ast.json", "w", encoding='utf-8'))
    pass
