from src.lexical_syntactic.ast_node import ASTNode
from src.lexical_syntactic.pparser import Parser


def test_program_1():
    """整体程序结束后有多余内容"""
    test_parser = Parser()
    with open("./test_parse/test_program/single_error/test_program_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/single_error/test_program_1.ast", 'w', encoding='utf-8'))


def test_program_2():
    """主程序头尾部缺少分号"""
    test_parser = Parser()
    with open("./test_parse/test_program/single_error/test_program_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/single_error/test_program_2.ast", 'w', encoding='utf-8'))


def test_program_3():
    """程序结尾缺少点号"""
    test_parser = Parser()
    with open("./test_parse/test_program/single_error/test_program_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/single_error/test_program_3.ast", 'w', encoding='utf-8'))


def test_program_4():
    """主程序头书写错误"""
    test_parser = Parser()
    with open("./test_parse/test_program/single_error/test_program_4.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/single_error/test_program_4.ast", 'w', encoding='utf-8'))


def test_program_5():
    """主程序体书写错误,begin end 缺失"""
    test_parser = Parser()
    with open("./test_parse/test_program/single_error/test_program_5.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/single_error/test_program_5.ast", 'w', encoding='utf-8'))


def test_program_6():
    """程序头前有非法字符"""
    test_parser = Parser()
    with open("./test_parse/test_program/single_error/test_program_6.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/single_error/test_program_6.ast", 'w', encoding='utf-8'))


def test_program_c1():
    """主程序头前有非法记号，且后部缺失分号"""
    test_parser = Parser()
    with open("./test_parse/test_program/complex_error/test_program_c1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/complex_error/test_program_c1.ast", 'w', encoding='utf-8'))


def test_program_c2():
    """主程序头前有非法记号，且程序尾部缺失点号"""
    test_parser = Parser()
    with open("./test_parse/test_program/complex_error/test_program_c2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/complex_error/test_program_c2.ast", 'w', encoding='utf-8'))


def test_program_c3():
    """主程序头前包含非法记号，主程序体书写错误"""
    test_parser = Parser()
    with open("./test_parse/test_program/complex_error/test_program_c3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program/complex_error/test_program_c3.ast", 'w', encoding='utf-8'))


def test_program_head_1():
    """缺少左括号"""
    test_parser = Parser()
    with open("./test_parse/test_program_head/single_error/test_program_head_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program_head/single_error/test_program_head_1.ast", 'w',
                             encoding='utf-8'))


def test_program_head_2():
    """缺少右括号"""
    test_parser = Parser()
    with open("./test_parse/test_program_head/single_error/test_program_head_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program_head/single_error/test_program_head_2.ast", 'w',
                             encoding='utf-8'))


def test_program_head_3():
    """缺少主程序名"""
    test_parser = Parser()
    with open("./test_parse/test_program_head/single_error/test_program_head_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program_head/single_error/test_program_head_3.ast", 'w',
                             encoding='utf-8'))


def test_program_head_4():
    """主程序头全部缺失"""
    test_parser = Parser()
    with open("./test_parse/test_program_head/single_error/test_program_head_4.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program_head/single_error/test_program_head_4.ast", 'w',
                             encoding='utf-8'))


def test_program_head_5():
    """主程序头参数列表缺失"""
    test_parser = Parser()
    with open("./test_parse/test_program_head/single_error/test_program_head_5.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_program_head/single_error/test_program_head_5.ast", 'w',
                             encoding='utf-8'))


def test_const_decl_1():
    """常量定义缺失标识符"""
    test_parser = Parser()
    with open("./test_parse/test_const_decl/single_error/test_const_decl_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_const_decl/single_error/test_const_decl_1.ast", 'w',
                             encoding='utf-8'))


def test_const_decl_2():
    """常量定义缺失定义列表"""
    test_parser = Parser()
    with open("./test_parse/test_const_decl/single_error/test_const_decl_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_const_decl/single_error/test_const_decl_2.ast", 'w',
                             encoding='utf-8'))


def test_const_decl_3():
    """常量定义缺失定义列表"""
    test_parser = Parser()
    with open("./test_parse/test_const_decl/single_error/test_const_decl_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_const_decl/single_error/test_const_decl_3.ast", 'w',
                             encoding='utf-8'))


def test_const_decl_4():
    """常数初始化右值缺失"""
    test_parser = Parser()
    with open("./test_parse/test_const_decl/single_error/test_const_decl_4.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_const_decl/single_error/test_const_decl_4.ast", 'w',
                             encoding='utf-8'))


def test_const_decl_5():
    """常数初始化等号缺失"""
    test_parser = Parser()
    with open("./test_parse/test_const_decl/single_error/test_const_decl_5.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_const_decl/single_error/test_const_decl_5.ast", 'w',
                             encoding='utf-8'))


def test_var_decl_1():
    """变量定义列表缺失"""
    test_parser = Parser()
    with open("./test_parse/test_var_decl/single_error/test_var_decl_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_var_decl/single_error/test_var_decl_1.ast", 'w',
                             encoding='utf-8'))


def test_var_decl_2():
    """变量定义类型声明缺失"""
    test_parser = Parser()
    with open("./test_parse/test_var_decl/single_error/test_var_decl_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_var_decl/single_error/test_var_decl_2.ast", 'w',
                             encoding='utf-8'))


def test_var_decl_3():
    """变量定义缺失分号"""
    test_parser = Parser()
    with open("./test_parse/test_var_decl/single_error/test_var_decl_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_var_decl/single_error/test_var_decl_3.ast", 'w',
                             encoding='utf-8'))


def test_var_decl_4():
    """变量定义缺失冒号"""
    test_parser = Parser()
    with open("./test_parse/test_var_decl/single_error/test_var_decl_4.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_var_decl/single_error/test_var_decl_4.ast", 'w',
                             encoding='utf-8'))


def test_var_decl_5():
    """变量定义缺失类型关键字"""
    test_parser = Parser()
    with open("./test_parse/test_var_decl/single_error/test_var_decl_5.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_var_decl/single_error/test_var_decl_5.ast", 'w',
                             encoding='utf-8'))


def test_type_1():
    """中括号不匹配"""
    test_parser = Parser()
    with open("./test_parse/test_type/single_error/test_type_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(output_file=open("./test_parse/test_type/single_error/test_type_1.ast", 'w', encoding='utf-8'))


def test_type_2():
    """缺失OF关键字"""
    test_parser = Parser()
    with open("./test_parse/test_type/single_error/test_type_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(output_file=open("./test_parse/test_type/single_error/test_type_2.ast", 'w', encoding='utf-8'))


def test_type_3():
    """数组元素类型不存在"""
    test_parser = Parser()
    with open("./test_parse/test_type/single_error/test_type_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(output_file=open("./test_parse/test_type/single_error/test_type_3.ast", 'w', encoding='utf-8'))


def test_type_4():
    """数组类型定义缺失不完整"""
    test_parser = Parser()
    with open("./test_parse/test_type/single_error/test_type_4.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(output_file=open("./test_parse/test_type/single_error/test_type_4.ast", 'w', encoding='utf-8'))


def test_period_1():
    """缺少逗号"""
    test_parser = Parser()
    with open("./test_parse/test_period/single_error/test_period_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_period/single_error/test_period_1.ast", 'w', encoding='utf-8'))


def test_period_2():
    """缺少双点号"""
    test_parser = Parser()
    with open("./test_parse/test_period/single_error/test_period_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_period/single_error/test_period_2.ast", 'w', encoding='utf-8'))


def test_subprogram_decl_1():
    """子程序体尾缺少分号"""
    test_parser = Parser()
    with open("./test_parse/test_subprogram_decl/single_error/test_subprogram_decl_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_subprogram_decl/single_error/test_subprogram_decl_1.ast", 'w',
                             encoding='utf-8'))


def test_subprogram_head_1():
    """函数名缺失"""
    test_parser = Parser()
    with open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_1.ast", 'w',
                             encoding='utf-8'))


def test_subprogram_head_2():
    """参数声明缺少冒号"""
    test_parser = Parser()
    with open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_2.ast", 'w',
                             encoding='utf-8'))


def test_subprogram_head_3():
    """参数声明缺少类型关键字"""
    test_parser = Parser()
    with open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_3.ast", 'w',
                             encoding='utf-8'))


def test_subprogram_head_4():
    """不完整的函数头"""
    test_parser = Parser()
    with open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_4.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_4.ast", 'w',
                             encoding='utf-8'))


def test_subprogram_head_5():
    """不完整的过程头"""
    test_parser = Parser()
    with open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_5.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_subprogram_head/single_error/test_subprogram_head_5.ast", 'w',
                             encoding='utf-8'))


def test_formal_parameter_1():
    """不完整的形参列表"""
    test_parser = Parser()
    with open("./test_parse/test_parameter/single_error/test_formal_parameter_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_parameter/single_error/test_formal_parameter_1.ast", 'w',
                             encoding='utf-8'))


def test_formal_parameter_2():
    """括号缺失"""
    test_parser = Parser()
    with open("./test_parse/test_parameter/single_error/test_formal_parameter_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_parameter/single_error/test_formal_parameter_2.ast", 'w',
                             encoding='utf-8'))


def test_parameter_list_1():
    """缺少分号"""
    test_parser = Parser()
    with open("./test_parse/test_parameter/single_error/test_parameter_list_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_parameter/single_error/test_formal_parameter_1.ast", 'w',
                             encoding='utf-8'))


def test_var_parameter_1():
    """缺少参数内容"""
    test_parser = Parser()
    with open("./test_parse/test_parameter/single_error/test_var_parameter_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_parameter/single_error/test_var_parameter_1.ast", 'w',
                             encoding='utf-8'))


def test_value_parameter_1():
    """缺少冒号"""
    test_parser = Parser()
    with open("./test_parse/test_parameter/single_error/test_value_parameter_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_parameter/single_error/test_value_parameter_1.ast", 'w',
                             encoding='utf-8'))


def test_value_parameter_2():
    """缺少类型关键字"""
    test_parser = Parser()
    with open("./test_parse/test_parameter/single_error/test_value_parameter_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_parameter/single_error/test_value_parameter_2.ast", 'w',
                             encoding='utf-8'))


def test_compound_statement_1():
    """缺少END关键字"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_compound_statement_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_compound_statement_1.ast", 'w',
                             encoding='utf-8'))


def test_statement_list_1():
    """缺少分号"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_statement_list_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_statement_list_1.ast", 'w',
                             encoding='utf-8'))


def test_if_statement_1():
    """缺少Then关键字"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_if_statement_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_if_statement_1.ast", 'w',
                             encoding='utf-8'))


def test_for_statement_1():
    """缺少赋值号"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_for_statement_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_for_statement_1.ast", 'w',
                             encoding='utf-8'))


def test_for_statement_2():
    """缺少to关键字"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_for_statement_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_for_statement_2.ast", 'w',
                             encoding='utf-8'))


def test_for_statement_3():
    """缺少do关键字"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_for_statement_3.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_for_statement_3.ast", 'w',
                             encoding='utf-8'))


def test_while_statement_1():
    """缺少do关键字"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_while_statement_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_while_statement_1.ast", 'w',
                             encoding='utf-8'))


def test_repeat_statement_1():
    """缺少until关键字"""
    test_parser = Parser()
    with open("./test_parse/test_statement/single_error/test_repeat_statement_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_statement/single_error/test_repeat_statement_1.ast", 'w',
                             encoding='utf-8'))


def test_id_varpart_1():
    """中括号不匹配"""
    test_parser = Parser()
    with open("./test_parse/test_id_varpart/single_error/test_id_varpart_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_id_varpart/single_error/test_id_varpart_1.ast", 'w', encoding='utf-8'))


def test_id_varpart_2():
    """数组下标不完整"""
    test_parser = Parser()
    with open("./test_parse/test_id_varpart/single_error/test_id_varpart_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_id_varpart/single_error/test_id_varpart_2.ast", 'w', encoding='utf-8'))


def test_procedure_call_1():
    """缺少括号"""
    test_parser = Parser()
    with open("./test_parse/test_procedure_call/single_error/test_procedure_call_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_procedure_call/single_error/test_procedure_call_1.ast", 'w',
                             encoding='utf-8'))


def test_expression_list_1():
    """缺少逗号"""
    test_parser = Parser()
    with open("./test_parse/test_expression/single_error/test_expression_list_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_expression/single_error/test_expression_list_1.ast", 'w',
                             encoding='utf-8'))


def test_simple_expression_1():
    """缺少操作数"""
    test_parser = Parser()
    with open("./test_parse/test_expression/single_error/test_simple_expression_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_expression/single_error/test_simple_expression_1.ast", 'w',
                             encoding='utf-8'))


def test_term_1():
    """缺少操作数"""
    test_parser = Parser()
    with open("./test_parse/test_term/single_error/test_term_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_term/single_error/test_term_1.ast", 'w',
                             encoding='utf-8'))


def test_factor_1():
    """括号不匹配"""
    test_parser = Parser()
    with open("./test_parse/test_factor/single_error/test_factor_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_factor/single_error/test_factor_1.ast", 'w',
                             encoding='utf-8'))


def test_factor_2():
    """函数调用列表缺失"""
    test_parser = Parser()
    with open("./test_parse/test_factor/single_error/test_factor_2.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print(
            output_file=open("./test_parse/test_factor/single_error/test_factor_2.ast", 'w',
                             encoding='utf-8'))


def test_parse():
    test_parser = Parser()
    with open("./test_lex/single_error/test_lex_1.pas", "r") as f:
        test_node = test_parser.parse(f.read())
        test_node.print()

    # assert test_node is not None
