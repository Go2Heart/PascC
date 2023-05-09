import sys
from semantic.SymbolTable import SymbolTable  # 全局符号表
from semantic.Types import TypesTable  # 全局类型表
from lexical_syntactic import pparser  # 语法分析器
from semantic.Analyzer import Analyzer  # 语义分析器
from targetcode.CodeGenerater import CodeGenerater  # 代码生成器

import logging

logging.basicConfig(level=logging.DEBUG)


def test_write_1():
    """write/writeln语句"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_write_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_write_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_read_1():
    """read语句"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_read_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_read_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_head_file_1():
    """不含输入输出语句"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_head_file_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_head_file_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_head_file_2():
    """含输入输出语句"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_head_file_2.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_head_file_2.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_expression_1():
    """运算符和表达式"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_expression_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_expression_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_fun_refer_1():
    """函数调用和传参"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_fun_refer_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_fun_refer_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_const_var_define_1():
    """常量变量定义"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_const_var_define_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_const_var_define_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_announce_1():
    """函数/过程声明"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_announce_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_announce_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_array_1():
    """数组定义与引用"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_array_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_array_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_fun_no_arg_1():
    """函数的无参调用"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_fun_no_arg_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_fun_no_arg_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")


def test_generate_1():
    """综合测试"""
    test_symboltable = SymbolTable  # 全局符号表
    test_typestable = TypesTable  # 全局类型表

    test_analyzer = Analyzer(test_symboltable, test_typestable)  # 语义分析器
    test_generator = CodeGenerater(test_symboltable, test_typestable)  # 代码生成器
    Wrong = False
    out_file = open("./test_generate/test_generate_1.cpp", "a", encoding="utf-8")

    # sys.stdout = out_file
    with open("./test_generate/test_generate_1.pas", "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.seek(0)
        test_parser = pparser.Parser(lens)  # 语法分析器
        test_node = test_parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if (test_parser.Lexerror == True):
            Wrong = True
        if (test_parser.yaccerror == True):
            Wrong = True
            for item in test_parser.errormes:
                print(item)
        if (Wrong == False):
            test_node.print()
        if (Wrong == False):
            program = test_analyzer.analyse(test_node)  # 语义分析，得到语义语法树根节点
        if (not Wrong):
            test_generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if (Wrong == True):
        print("代码存在以上的问题，编译中止")
