import os
from ast import parse
from semantic.SymbolTable import SymbolTable  # 全局符号表
from semantic.Types import TypesTable  # 全局类型表
from lexical_syntactic import pparser  # 语法分析器
from semantic.Analyzer import Analyzer  # 语义分析器
from targetcode.CodeGenerater import CodeGenerater  # 代码生成器
import logging
import sys

if __name__ == "__main__":
    '''
    定义命令行参数：
    -d : 输出语法树
    argv[0]: 输入文件名
    argv[1]: 输出文件名
    '''
    debug_flag = False
    output_file = None

    if len(sys.argv)<2 or len(sys.argv) >4:
        print("Help:\n -d Debug\n input_filepath output_filepath\n")
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-d':
            print("Help:\n -d Debug\n input_filepath output_filepath\n Input Filepath Not Found\n")
            sys.exit(1)
        else:
            input = sys.argv[1]
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-d':
            debug_flag = True
            input=sys.argv[2]
        else:
            input = sys.argv[1]
            output_file = sys.argv[2]
    elif len(sys.argv)==4 and sys.argv[1]=='-d':
        debug_flag=True
        input = sys.argv[2]
        output_file = sys.argv[3]
    else:
        print("Help:\n -d Debug\n input_filepath output_filepath\n")
        sys.exit(1)

    if output_file :
        output = open(output_file, 'w', encoding='utf-8')
    else:
        output = None
    if debug_flag:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    symboltable = SymbolTable  # 全局符号表
    typestable = TypesTable  # 全局类型表

    analyzer = Analyzer(symboltable, typestable)  # 语义分析器
    generator = CodeGenerater(symboltable, typestable, output)  # 代码生成器
    # input = input("请输入测试文件名：")
    Wrong = False
    #route1="D:/code/PascC/test/test_cases/test_parse/test_period/single_error/test_period_2.pas"
    # route="test/"+input+".pas"
    with open(input, "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        parser = pparser.Parser(lens)  # 语法分析器
        f.seek(0)
        node = parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if(parser.Lexerror==True):
            Wrong = True
        if(parser.yaccerror==True):
            Wrong = True
            for item in parser.errormes:
                print(item)
        if(Wrong==False and debug_flag == True):
            node.print()
        if(Wrong==False):
            program = analyzer.analyse(node)  # 语义分析，得到语义语法树根节点
            if program.ErrorFlag==True:
                Wrong=True
        if(not Wrong):
            generator.ProgramGenerate(program)  # 代码生成
        f.close()
    if(Wrong == True):
        print("代码存在以上的问题，编译中止")
    # node.print(output_file=open("test/gcd.ast", "w", encoding='utf-8')
    # node.json_print(output_file=open("test/gcd_ast.json", "w", encoding='utf-8'))
    # os.system("pause")
