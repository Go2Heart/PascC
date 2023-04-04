"""lexer module for the compiler
Lexer class is the main class for the lexer, being able to tokenize a string of PASCAL code
"""
import sys,os
from ply.lex import lex

class Lexer:
    """Lexer class 
    
    Attributes:
        _lexer: the ply lexer object
        _input: the input target
    """
    keywords = {
        'program' : 'PROGRAM',
        'const' : 'CONST',
        'type' : 'TYPE',
        'array' : 'ARRAY',
        'set' : 'SET',
        'of' : 'OF',
        'record' : 'RECORD',
        'var' : 'VAR',
        'forward' : 'FORWARD',
        'function' : 'FUNCTION',
        'procedure' : 'PROCEDURE',
        'integer' : 'INTEGER',
        'longint' : 'INTEGER',
        'real' : 'REAL',
        'boolean' : 'BOOLEAN',
        'char' : 'CHAR',
        'begin' : 'BEGIN',
        'end' : 'END',
        'if' : 'IF',
        'then' : 'THEN',
        'else' : 'ELSE',
        'while' : 'WHILE',
        'do' : 'DO',
        'for' : 'FOR',
        'downto' : 'DOWNTO',
        'to' : 'TO',
        'with' : 'WITH',
        'read' : 'READ',
        'write' : 'WRITE',
        'readln' : 'READLN',
        'writeln' : 'WRITELN',
        'in' : 'INOP',
        'not' : 'NOTOP',
        'or' : 'OROP'
    }
    
    tokens = [
        'ID', 'ICONST', 'RCONST', 'BCONST', 'CCONST', 'RELOP',
        'ADDOP', 'STRING', 'LPAREN', 'RPAREN', 'SEMI', 'DOT', 'COMMA',
        'EQU', 'COLON', 'LBRACK', 'RBRACK', 'ASSIGN', 'DOTDOT',
        'EOF', 'LCURL', 'RCURL', 'MULDIVANDOP'
    ] + list(keywords.values())
    
    t_EOF = r'EOF'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_RELOP = r'>=|<=|<>|>|<'
    t_ADDOP = r'\+|\-'
    t_DOT = r'\.'
    t_LCURL = r'{'
    t_RCURL = r'}'
    t_LBRACK = r'\['
    t_RBRACK = r'\]'
    t_SEMI = r';'
    t_ASSIGN = r':='
    t_DOTDOT = r'\.\.'
    t_COMMA = r','
    t_EQU = r'='
    t_COLON = r':'
    
    t_ignore = ' \t'
    
    def __init__(self):
        """init the lexer
        
        Attributes:
            _lexer: the lexer object
            _input: the input target
        """
        self._lexer = lex(module=self)
        self._input = None
        
    def get_lexer(self):
        """get the lexer object
        
        Returns:
            the lexer object
        """
        return self._lexer
    
    def load_string(self, input):
        """load a string as the input target
        
        Args:
            input: the input string
        """
        self._input = input
        self._lexer.input(input)
        self._lexer.lineno = 1
    
    def load_file(self, path):
        """load a file as the input target
        
        Args:
            path: the file path
        """
        self._input = None
        with open(path, 'r', encoding='utf8') as f:
            self._input = f.read()
        if not self._input:
            print(f'Failed to load file {path}')
            return
        self._lexer.input(self._input)
        self._lexer.lineno = 1

    def token(self):
        """get the next token
        
        Returns:
            the next token
        """
        if not self._input:
            raise Exception('No input target')
        return self._lexer.token()
    
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        # t.lexer.lexpos = 0
        pass

    def t_ignore_COMMENT_MULTI(self,t):
        r'{[^}]*|\n*}'
        t.lexer.lineno += t.value.count('\n')
        pass

    def t_MULDIVANDOP(self,t):
        r'and|div|mod|\*|\/'
        t.value = str(t.value)
        t.type = 'MULDIVANDOP'
        return t

    def t_RCONST(self,t):
        r'([1-9][0-9]*|0)*\.(0|[0-9]*[1-9][0-9]*)((e|E)(\+|-)?[0-9]+)?|[0-9]+(e|E)(\+|-)?[0-9]+|0H([a-fA-F1-9]+[a-fA-F1-9]*)*\.[0-9]*[1-9a-fA-F][a-fA-F0-9]*|0B[1]+\.[0-1]*[1][0-1]*'
        t.value = float(t.value)
        t.type = 'RCONST'
        return t

    def t_ICONST_2(self,t):
        r'0H[a-fA-F1-9][a-fA-F0-9]*'
        t.value = int(str(t.value)[2:], 16)
        t.type = 'ICONST'
        return t

    def t_ICONST_3(self,t):
        r'0B1[0-1]*'
        t.value = int(str(t.value)[2:], 2)
        t.type = 'ICONST'
        return t

    def t_ICONST_1(self,t):
        r'0|[1-9][0-9]*'
        t.value = int(t.value)
        t.type = 'ICONST'
        return t

    def t_BCONST(self,t):
        r'TRUE|FALSE'
        t.value = bool(t.value)
        t.type = 'BCONST'
        return t

    def t_CCONST(self,t):
        r'\'([ -~]|\\n|\\f|\\t|\\r|\\b|\\v)\''
        t.value = str(t.value) # 不修改为[1:-1]
        t.type = 'CCONST'
        t.lexer.lineno += t.value.count('\n') 
        return t

    def t_STRING(self,t):
        r"'([^']|\\\\|\\'|\\n|\\t)*'" 
        t.value = '"'+str(t.value[1:-1])+'"' # 不修改为[1:-1]
        t.type = 'STRING'
        t.lexer.lineno += t.value.count('\n')
        return t

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if t.value.lower() in self.keywords.keys():
            t.value = t.value.lower()
        t.type = self.keywords.get(t.value, 'ID')
        return t

    def t_error(self,t):
        global errorFlag
        print("Line {1}: Illegal character '{0}'".format(t.value[0], t.lineno))
        t.lexer.skip(1)
        errorFlag = True
    
    def find_column(input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
        
    def scan(self, output_file=None):
        """scan the input string
        
        Args:
            input: the input string
        """
        while True:
            token = self.token()
            if not token:
                break
            print(token)
            if output_file:
                output_file.write(str(token) + '\n')
        
if __name__ == '__main__':
    lexer = Lexer()
    lexer.load_file('test/qsort.pas')
    lexer.scan(output_file=open('test/qsort.out', 'w',encoding='utf-8'))
    