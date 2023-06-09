import logging
import Statements


class SubProgram(object):
    """subprogram : subprogram_head SEMI subprogram_body"""
    def __init__(self, node, symboltable, typestable,type):
        self.ErrorFlag=False
        symboltable.pushblock()  # 进入到一个块中了，符号表重定位
        symboltable.insertItem(node.childs[0].type[1],type,[],[])
        id = node.childs[0].type[1]  # id = 'id1'
        return_type=typestable.get_type(node.childs[0]).type.name
        type = typestable.get_type(node.childs[0])
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
            param_types = symboltable.getItem(self.name)["type"].params #参数类型列表
            cnt = 0
            for i in range(len(tmp.childs)):
                # x = value_parameter/variable_parameter
                x = tmp.childs[i]
                if x.type == 'var_parameter':
                    x = x.childs[0]
                ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
                linenos=[p.type[2] for p in x.childs if p.type[0] == 'id']
                for id in ids:
                    type = param_types[cnt]  # 之前求函数类型的时候已经存过一次了
                    if symboltable.haveItem(id):
                        print("Line {0} : 参数 '{1}' 重复声明".format(linenos[cnt],id))
                        self.ErrorFlag=True
                    else:
                        symboltable.insertItem(id, type, [], [])
                        self.parameter_idlist.append(id)
                    cnt += 1


        logging.debug('subprogram.parameter_idlist=' +
                      str(self.parameter_idlist))

        # 将常量加入符号表
        self.const_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=const_declaration
                id = x.childs[0].type[1]  # id = 'id1'
                lineno = x.childs[0].type[2]
                type = typestable.get_type(x)
                self.ErrorFlag|=type.ErrorFlag
                if symboltable.haveItem(id):
                    print("Line {0} : Const Variable ‘{1}’ 重复声明".format(lineno, id))
                    self.ErrorFlag=True
                else:
                    symboltable.insertItem(id, type, [], [])
                    self.const_idlist.append(id)
        logging.debug('subprogram.const_idlist=' + str(self.const_idlist))

        # 将变量加入符号表
        self.var_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[1]  # tmp=var_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=var_declaration
                type = typestable.get_type(x.childs[-1])
                self.ErrorFlag|=type.ErrorFlag
                ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
                linenos = [p.type[2] for p in x.childs if p.type[0] == 'id']
                tmp_ids = []
                for index, id in enumerate(ids):
                    if symboltable.haveItem(id):
                        print("Line {0} : Variable ‘{1}’ 重复声明".format(linenos[index], id))
                        self.ErrorFlag=True
                    else:
                        symboltable.insertItem(id, type, [], [])
                        tmp_ids.append(id)
                self.var_idlist.append(tmp_ids)
        logging.debug('subprogram.var_idlist=' + str(self.var_idlist))

        # TODO :将子程序加入符号表。暂时没有这个语法，所以先注释掉
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
        symboltable.print()

        # 处理语句块
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[-1]  # tmp=compound_statement
        self.compound_statement = Statements.CompoundStatement(tmp, symboltable, typestable,node.childs[0].type[1])
        self.ErrorFlag|=self.compound_statement.ErrorFlag
        if (not self.compound_statement.ReturnFlag) and return_type!='void':
            print("Line {0} : 函数 '{1}' 没有返回值语句".format(node.childs[0].type[2],node.childs[0].type[1]))
            self.ErrorFlag=True
        # 退出块
        symboltable.popblock()  # 退出当前块，符号表重定位
