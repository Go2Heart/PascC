from src.lexical_syntactic.plexer import Lexer



def test_lexer():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex.pas')
    a=test_lexer.token()
    print(a)
    assert a is not None

'''行长度超限'''
def test_1():
    test_lexer= Lexer()
    test_lexer.load_file('./test_lex/test_lex_1.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_1.out', 'w', encoding='utf-8'))

'''标识符过长'''
def test_2():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_2.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_2.out', 'w', encoding='utf-8'))

'''非法字符'''
def test_3():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_3.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_3.out', 'w', encoding='utf-8'))

'''读取字符常量时遇到文件尾EOF'''
def test_4():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_4.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_4.out', 'w', encoding='utf-8'))

'''读取的字符常量为空'''
def test_5():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_5.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_5.out', 'w', encoding='utf-8'))

'''读取的字符常量不只一个字符'''
def test_6():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_6.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_6.out', 'w', encoding='utf-8'))

'''读取字符常量先遇到换行符而不是单引号'''
def test_7():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_7.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_7.out', 'w', encoding='utf-8'))

'''读取多行注释时遇到文件尾'''
def test_8():
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex_8.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex_8.out', 'w', encoding='utf-8'))

def test_c1():
    pass