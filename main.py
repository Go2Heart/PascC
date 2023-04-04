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

    parser = pparser.Parser()  # 语法分析器
    analyzer = Analyzer(symboltable, typestable)  # 语义分析器
    generator = CodeGenerater(symboltable, typestable)  # 代码生成器
    with open("test/test_parser.pas", "r") as f:
        node = parser.parse(f.read())  # 语法分析，得到抽象语法树根节点
        node.print()
        program = analyzer.analyse(node)  # 语义分析，得到语义语法树根节点
        generator.ProgramGenerate(program)  # 代码生成
        f.close()
    # node.print(output_file=open("test/gcd.ast", "w", encoding='utf-8')
    # node.json_print(output_file=open("test/gcd_ast.json", "w", encoding='utf-8'))
    pass
