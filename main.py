from ast import parse
from semantic.SymbolTable import SymbolTable  # 全局符号表
from semantic.Types import TypesTable  # 全局类型表
from lexical_syntactic import pparser  # 语法分析器
from semantic.Analyzer import Analyzer  # 语义分析器
from targetcode.CodeGenerater import CodeGenerater  # 代码生成器
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    symboltable = SymbolTable  # 全局符号表
    typestable = TypesTable  # 全局类型表

    analyzer = Analyzer(symboltable, typestable)  # 语义分析器
    generator = CodeGenerater(symboltable, typestable)  # 代码生成器
    input = input("请输入测试文件名：")
    Wrong = False
    #route1="D:/code/PascC/test/test_cases/test_parse/test_period/single_error/test_period_2.pas"
    route="test/"+input+".pas"
    with open(route, "r", encoding='utf-8') as f:
        line = f.readlines()
        lens = len(line)
        f.close()
    parser = pparser.Parser(lens)  # 语法分析器
    with open(route, "r", encoding='utf-8') as f:
        node = parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        if(parser.Lexerror==True):
            Wrong = True
        if(parser.yaccerror==True):
            Wrong = True
            for item in parser.errormes:
                print(item)
        if(Wrong==False):
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
    pass
