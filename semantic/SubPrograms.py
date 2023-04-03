from lexical_syntactic import pparser
from Types import Types
from SymbolTable import SymbolTable
import logging
import Statements
import SubPrograms


class SubProgram(object):
    """subprogram : subprogram_head SEMI subprogram_body"""
    def __init__(self, node):
        SymbolTable.pushblock()  # 进入到一个块中了，符号表重定位

        # 子程序名
        tmp = node.childs[0]  # tmp=('procedure_head', 'gcd1')
        self.name = tmp.type[1]  # example
        logging.debug('subprogram.name=' + self.name)

        # 参数表
        self.parameter_idlist = []
        tmp = tmp.childs[0]
        # now = formal_parameter.formal_parameter -> LPAREN parameter_list RPAREN
        if tmp is not None:
            tmp = tmp.childs[0]
            # now = parameter_list.parameter_list -> parameter_list SEMI parameter | parameter
            param_types = SymbolTable.getItem(self.name)["type"].params
            cnt = 0
            for i in range(len(tmp.childs)):  
                # x = value_parameter/variable_parameter
                x = tmp.childs[i]
                if x.type == 'var_parameter':
                    x = x.childs[0]
                ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
                for id in ids:
                    type = param_types[cnt]
                    cnt += 1
                    if SymbolTable.haveItem(id):
                        print("重复声明")
                    else:
                        SymbolTable.insertItem(id, type, [], [])
                        self.parameter_idlist.append(id)

        logging.debug('subprogram.parameter_idlist=' + str(self.parameter_idlist))

        # 将常量加入符号表
        self.const_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=const_declaration
                id = x.childs[0].type[1]  # id = 'id1'
                type = Types.get_type(x)
                if SymbolTable.haveItem(id):
                    print("重复声明")
                else:
                    SymbolTable.insertItem(id, type, [], [])
                    self.const_idlist.append(id)
        logging.debug('subprogram.const_idlist=' + str(self.const_idlist))

        # 将变量加入符号表
        self.var_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[1]  # tmp=var_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=var_declaration
                type = Types.get_type(x.childs[-1])
                ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
                for id in ids:
                    if SymbolTable.haveItem(id):
                        print("重复声明")
                    else:
                        SymbolTable.insertItem(id, type, [], [])
                        self.var_idlist.append(id)
        logging.debug('subprogram.var_idlist=' + str(self.var_idlist))

        # 将子程序加入符号表。暂时没有这个语法，所以注释掉
        # self.subprogram_list = []
        # tmp = node.childs[1]  # tmp=program_body
        # tmp = tmp.childs[2]  # tmp=subprogram_declarations
        # for x in tmp.childs:  # x=subprogram
        #     id = x.childs[0].type[1]  # id = 'id1'
        #     type = Types.get_type(x.childs[0])
        #     if SymbolTable.haveItem(id):
        #         print("重复声明")
        #     else:
        #         SymbolTable.insertItem(id, type, [], [])
        #         self.subprogram_list.append(SubPrograms.SubProgram(x))

        logging.debug('SubProgram:SymbolTable')
        SymbolTable.print()

        # 处理语句块
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[-1]  # tmp=compound_statement
        self.compound_statement = Statements.CompoundStatement(tmp)

        # 退出块
        SymbolTable.popblock()  # 退出当前块，符号表重定位


if __name__ == "__main__":
    parser = pparser.Parser()
    with open("./test/gcd.pas", "r") as f:
        node = parser.parse(f.read())
        f.close()
    a = Program(node)
    # node.print(output_file=open("test/gcd.ast", "w", encoding='utf-8')
    # node.json_print(output_file=open("test/gcd_ast.json", "w", encoding='utf-8'))
    pass
