import logging

from lexical_syntactic import pparser  # 语法分析器
from semantic.Analyzer import Analyzer  # 语义分析器
from semantic.SymbolTable import SymbolTable  # 全局符号表
from semantic.Types import TypesTable  # 全局类型表

logging.basicConfig(level=logging.DEBUG)


def test_var_refer_1():
    """变量未定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_var_refer/test_var_refer_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_var_refer_2():
    """引用主程序名"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_var_refer/test_var_refer_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_var_refer_3():
    """在子过程的定义中错误地引用了该子过程名 """
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_var_refer/test_var_refer_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_var_refer_4():
    """在子过程外错误地引用了子过程名 """
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_var_refer/test_var_refer_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_1():
    """递归调用，正确的程序"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_2():
    """递归调用，错误的程序，缺少实参"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_3():
    """在子函数外出现对函数名的左值引用"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_4():
    """在子函数外函数调用缺少实参"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_5():
    """函数调用未定义，标识符名不是函数"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_5.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_6():
    """函数调用参数个数不对，类型不匹配"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_6.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_7():
    """函数调用表达式无法作为实参"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_7.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_8():
    """函数调用实参无法被引用调用的情况(不能是常量、不能是复杂表达式，只能是简单变量或数组元素)"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_8.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_9():
    """函数调用引用参数需类型强一致，即不支持任何类型转换"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_9.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_refer_10():
    """将函数单独作为一条语句"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_refer/test_fun_refer_10.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_wrong_refer_1():
    """左值引用主程序参数"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_wrong_refer/test_wrong_refer_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_wrong_refer_2():
    """右值引用主程序参数"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_wrong_refer/test_wrong_refer_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_array_refer_1():
    """左值不带下标引用数组"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_array_refer/test_array_refer_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_array_refer_2():
    """符号表中记录的不是数组"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_array_refer/test_array_refer_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_array_refer_3():
    """数组下标维数不对"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_array_refer/test_array_refer_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_array_refer_4():
    """数组下标类型检查和越界检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_array_refer/test_array_refer_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_type_check_1():
    """repeat、while、if语句的条件表达式的类型检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_type_check/test_type_check_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_type_check_2():
    """for语句的start end表达式的类型检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_type_check/test_type_check_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_type_check_3():
    """for语句把函数、过程、主程序、函数参数、字符当做循环变量以及循环变量未定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_type_check/test_type_check_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_type_check_4():
    """赋值语句相关类型检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_type_check/test_type_check_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_1():
    """将非过程作为过程调用，或者过程未定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_2():
    """exit语句相关检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_3():
    """read语句相关检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_4():
    """read,write语句至少包括一个实参"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_5():
    """writeln可以不带参数"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_5.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_6():
    """过程调用时实参与形参的对应检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_6.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_7():
    """过程调用时表达式无法作为实参"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_7.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_8():
    """过程调用时常量、常量标识符、复杂表达式、数组名不能作为引用参数"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_8.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_prod_refer_9():
    """过程调用时引用参数必须保证类型强一致"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_prod_refer/test_prod_refer_9.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_define_1():
    """子程序名已定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_define/test_fun_define_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_fun_define_2():
    """缺少返回值语句"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_fun_define/test_fun_define_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_var_define_1():
    """变量重定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_var_define/test_var_define_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_var_define_2():
    """数组定义下界比上界大"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_var_define/test_var_define_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_const_define_1():
    """常量重定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_const_define/test_const_define_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_const_define_2():
    """常量传播与常量表达式的计算"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_const_define/test_const_define_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_const_define_3():
    """常量左值引用"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_const_define/test_const_define_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_expression_check_1():
    """关系运算符类型检查"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_expression_check/test_expression_check_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_expression_check_2():
    """not、and、or运算符"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_expression_check/test_expression_check_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_expression_check_3():
    """+、-、*、/、minus"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_expression_check/test_expression_check_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_expression_check_4():
    """div、mod"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_expression_check/test_expression_check_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_expression_check_5():
    """/、div、mod的除0错误，常数表达式的计算"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_expression_check/test_expression_check_5.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_program_1():
    """主程序名与库程序同名"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_program/test_program_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_program_2():
    """主程序参数与库程序同名"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_program/test_program_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_program_3():
    """主程序参数与主程序同名"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_program/test_program_3.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_program_4():
    """常量、变量、参数等与库函数、主程序名、主程序参数同名"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_program/test_program_4.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)


def test_semantic():
    """正确性测试"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)
    with open("./test_semantic/test_semantic_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)
        test_node = test_parser.parse(f.read())
        test_analyzer.analyse(test_node)
