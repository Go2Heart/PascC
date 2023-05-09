import logging
import Statements
import SubPrograms
from semantic.Types import StringType, VoidType, FunctionType, NoneType, FileType


class Program(object):

    """program : program_head SEMI program_body DOT"""
    def __init__(self, node, symboltable, typestable):
        self.ErrorFlag=False
        # 进入块
        symboltable.pushblock()  # 进入到一个块中了，符号表重定位


        # 程序名
        tmp = node.childs[0]  # tmp=('program_head', 'example')
        self.name = tmp.type[1]  # example

        logging.debug('program.name=' + self.name)
        lst=[]
        # 参数表
        tmp = tmp.childs[0]  # tmp=idlist
        if tmp is None:
            self.parameter_idlist = []
        else:
            self.parameter_idlist = [x.type[1] for x in tmp.childs
                                     ]  # ['id1', 'id2', 'id3']
        for param in self.parameter_idlist:
            if param==self.name:
                print('Line {0} : 主程序参数不能与主程序名同名'.format(node.type[1]))
                self.ErrorFlag=True
            else:
                symboltable.insertItem(param,FileType(),[],[])
                lst.append(FileType())
        symboltable.insertItem(self.name,FunctionType(VoidType(),lst),[],[])

        logging.debug('program.parameter_idlist=' + str(self.parameter_idlist))

        # 将常量加入符号表
        self.const_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[0]  # tmp=const_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=const_declaration
                id = x.childs[0].type[1]  # id = 'id1'
                lineno=x.childs[0].type[2]
                type = typestable.get_type(x)
                self.ErrorFlag |= type.ErrorFlag
                if symboltable.haveItem(id):
                    print("Line {0} : Const Variable ‘{1}’ 重复声明".format(lineno,id))
                    self.ErrorFlag=True
                else:
                    symboltable.insertItem(id, type, [], [])
                    self.const_idlist.append(id)
        logging.debug('program.const_idlist=' + str(self.const_idlist))

        # 将变量加入符号表
        self.var_idlist = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[1]  # tmp=var_declarations
        if tmp is not None:
            for x in tmp.childs:  # x=var_declaration
                type = typestable.get_type(x.childs[-1],symboltable,self.const_idlist)
                ids = [p.type[1] for p in x.childs if p.type[0] == 'id']
                linenos=[p.type[2] for p in x.childs if p.type[0] == 'id']
                tmp_ids = []
                self.ErrorFlag|=type.ErrorFlag
                for index,id in enumerate(ids):
                    if symboltable.haveItem(id):
                        print("Line {0} : Variable ‘{1}’ 重复声明".format(linenos[index],id))
                        self.ErrorFlag=True
                    else:
                        symboltable.insertItem(id, type, [], [])
                        tmp_ids.append(id)
                self.var_idlist.append(tmp_ids)
        logging.debug('program.var_idlist=' + str(self.var_idlist))

        # 将子程序加入符号表
        self.subprogram_list = []
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[2]  # tmp=subprogram_declarations
        for x in tmp.childs:  # x=subprogram
            id = x.childs[0].type[1]  # id = 'id1'
            type = typestable.get_type(x.childs[0])
            self.ErrorFlag|=type.ErrorFlag
            if symboltable.haveItem(id):
                print("Line {0} : Subprogram '{1}' 重复声明".format(x.childs[0].type[2],id))
                self.ErrorFlag=True
            else:
                symboltable.insertItem(id, type, [], [])
                self.subprogram_list.append(
                    SubPrograms.SubProgram(x, symboltable, typestable))
                for subprogram in self.subprogram_list:
                    self.ErrorFlag|=subprogram.ErrorFlag

                logging.debug('Program:SymbolTable')
                symboltable.print()

        # 处理语句块
        tmp = node.childs[1]  # tmp=program_body
        tmp = tmp.childs[3]  # tmp=compound_statement
        self.compound_statement = Statements.CompoundStatement(
            tmp, symboltable, typestable)
        self.ErrorFlag|=self.compound_statement.ErrorFlag

        # 退出块
        symboltable.popblock()  # 退出当前块，符号表重定位

