from src.lexical_syntactic.plexer import Lexer


def test_lexer():
    '''综合正确性测试 quicksort'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/test_lex.pas')
    test_lexer.scan(output_file=open('./test_lex/test_lex.out', 'w', encoding='utf-8'))


def test_1():
    '''行长度超限'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_1.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_1.out', 'w', encoding='utf-8'))


def test_2():
    '''标识符过长'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_2.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_2.out', 'w', encoding='utf-8'))


def test_3():
    '''非法字符'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_3.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_3.out', 'w', encoding='utf-8'))


def test_4():
    '''读取字符常量时遇到文件尾EOF'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_4.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_4.out', 'w', encoding='utf-8'))


def test_5():
    '''读取的字符常量为空'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_5.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_5.out', 'w', encoding='utf-8'))


def test_6():
    '''读取的字符常量不只一个字符'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_6.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_6.out', 'w', encoding='utf-8'))


def test_7():
    '''读取字符常量先遇到换行符而不是单引号'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_7.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_7.out', 'w', encoding='utf-8'))


def test_8():
    '''读取多行注释时遇到文件尾'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/single_error/test_lex_8.pas')
    test_lexer.scan(output_file=open('./test_lex/single_error/test_lex_8.out', 'w', encoding='utf-8'))


def test_c1():
    '''标识符过长+非法字符'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/complex_error/test_lex_c1.pas')
    test_lexer.scan(output_file=open('./test_lex/complex_error/test_lex_c1.out', 'w', encoding='utf-8'))


def test_c2():
    '''读取字符为空+读取字符常量遇到文件尾'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/complex_error/test_lex_c2.pas')
    test_lexer.scan(output_file=open('./test_lex/complex_error/test_lex_c2.out', 'w', encoding='utf-8'))


def test_c3():
    '''读取字符遇到换行+注释遇到文件尾'''
    test_lexer = Lexer()
    test_lexer.load_file('./test_lex/complex_error/test_lex_c3.pas')
    test_lexer.scan(output_file=open('./test_lex/complex_error/test_lex_c3.out', 'w', encoding='utf-8'))
