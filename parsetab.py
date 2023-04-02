
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDOP ARRAY ASSIGN BCONST BEGIN BOOLEAN CCONST CHAR COLON COMMA CONST DO DOT DOTDOT DOWNTO ELSE END EOF EQU FOR FORWARD FUNCTION ICONST ID IF INOP INTEGER LBRACK LCURL LPAREN MULDIVANDOP NOTOP OF OROP PROCEDURE PROGRAM RBRACK RCONST RCURL READ REAL RECORD RELOP RPAREN SEMI SET STRING THEN TO TYPE VAR WHILE WITH WRITEprogram : program_head SEMI program_body DOTprogram_head : PROGRAM ID \n                        | PROGRAM ID LPAREN idlist RPARENidlist : idlist COMMA ID\n                  | IDprogram_body : const_declarations var_declarations subprogram_declarations compound_statementconst_declarations : CONST const_declaration SEMI\n                              | emptyconst_declaration : ID EQU const_value \n                             | const_declaration SEMI ID EQU const_valueconst_value : ADDOP ICONST\n                       | ICONST\n                       | IDvar_declarations : VAR var_declaration SEMI\n                            | emptyvar_declaration : idlist COLON type\n                           | var_declaration SEMI idlist COLON typetype : basic_type\n                | ARRAY LBRACK period RBRACK OF basic_typebasic_type : INTEGER\n                      | REAL\n                      | CHAR\n                      | STRING\n                      | BOOLEANperiod : ICONST DOTDOT ICONST\n                  | period COMMA ICONST DOTDOT ICONSTsubprogram_declarations : subprogram_declarations subprogram SEMI\n                                   | emptysubprogram : subprogram_head SEMI subprogram_bodysubprogram_head : PROCEDURE ID formal_parameter\n                           | FUNCTION ID formal_parameter COLON basic_typeformal_parameter : LPAREN parameter_list RPAREN\n                            | emptyparameter_list : parameter_list SEMI parameter\n                          | parameterparameter : var_parameter\n                     | value_parametervar_parameter : VAR value_parametervalue_parameter : idlist COLON basic_typesubprogram_body : const_declarations var_declarations compound_statementcompound_statement : BEGIN statement_list ENDstatement_list : statement_list SEMI statement\n                          | statementstatement : variable ASSIGN expression\n                     | ID ASSIGN expression\n                     | procedure_call\n                     | compound_statement\n                     | IF expression THEN statement else_part\n                     | FOR ID ASSIGN expression TO expression DO statement\n                     | READ LPAREN variable_list RPAREN\n                     | WRITE LPAREN expression_list RPARENvariable_list : variable_list COMMA variable\n                         | variablevariable : ID id_varpartid_varpart : LBRACK expression RBRACK\n                      | emptyprocedure_call : ID\n                          | ID LPAREN expression_list RPARENelse_part : ELSE statement\n                     | emptyexpression_list : expression_list COMMA expression\n                           | expressionexpression : simple_expression RELOP simple_expression\n                      | simple_expression EQU simple_expression\n                      | simple_expressionsimple_expression : simple_expression ADDOP term\n                             | termterm : term MULDIVANDOP factor\n                | factorfactor : number\n                  | variable\n                  | ID LPAREN expression_list RPAREN\n                  | NOTOP factor\n                  | ADDOP factornumber : ICONST\n                  | RCONSTempty :'
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,11,],[0,-1,]),'SEMI':([2,5,15,21,25,28,30,36,37,39,42,43,45,46,47,53,56,57,59,60,61,62,63,65,66,70,73,75,77,78,79,80,81,83,84,88,90,92,96,97,98,99,107,110,117,118,119,120,124,127,129,130,131,132,133,134,137,139,140,141,143,145,150,152,153,156,157,161,163,167,],[4,-2,23,33,-3,41,52,-13,-9,-12,67,-43,-57,-46,-47,-77,-16,-18,-20,-21,-22,-23,-24,-11,-41,-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,-29,-30,-33,-10,-42,-44,-45,-74,-73,142,-35,-36,-37,-17,-58,-55,-77,-63,-64,-66,-68,-50,-51,-40,-32,-38,-31,-48,-60,-72,-34,-39,-59,-19,-49,]),'ID':([3,8,10,13,23,24,26,29,31,32,33,48,49,64,67,68,69,71,72,76,82,86,87,91,103,104,105,106,108,109,111,121,128,138,142,151,154,165,],[5,16,17,17,35,36,40,45,53,54,17,81,85,36,45,81,81,81,81,81,81,114,81,17,45,81,81,81,81,81,81,17,81,114,17,45,81,45,]),'CONST':([4,52,],[8,8,]),'VAR':([4,7,9,23,52,89,91,142,],[-77,13,-8,-7,-77,13,121,121,]),'BEGIN':([4,7,9,12,14,19,20,23,29,33,41,52,67,89,103,116,151,165,],[-77,-77,-8,-77,-15,29,-28,-7,29,-14,-27,-77,29,-77,29,29,29,29,]),'PROCEDURE':([4,7,9,12,14,19,20,23,33,41,],[-77,-77,-8,-77,-15,31,-28,-7,-14,-27,]),'FUNCTION':([4,7,9,12,14,19,20,23,33,41,],[-77,-77,-8,-77,-15,32,-28,-7,-14,-27,]),'LPAREN':([5,45,50,51,53,54,81,],[10,71,86,87,91,91,109,]),'DOT':([6,27,66,],[11,-6,-41,]),'EQU':([16,35,70,73,75,77,78,79,80,81,83,84,107,110,129,133,134,153,],[24,64,-54,-56,105,-67,-69,-70,-71,-77,-75,-76,-74,-73,-55,-66,-68,-72,]),'RPAREN':([17,18,40,59,60,61,62,63,70,73,75,77,78,79,80,81,83,84,100,101,107,110,112,113,114,115,117,118,119,120,129,131,132,133,134,135,143,149,153,155,156,157,],[-5,25,-4,-20,-21,-22,-23,-24,-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,127,-62,-74,-73,137,-53,-77,139,141,-35,-36,-37,-55,-63,-64,-66,-68,153,-38,-61,-72,-52,-34,-39,]),'COMMA':([17,18,22,40,55,70,73,75,77,78,79,80,81,83,84,100,101,107,110,112,113,114,115,122,125,129,131,132,133,134,135,149,153,155,160,166,],[-5,26,26,-4,26,-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,128,-62,-74,-73,138,-53,-77,128,26,147,-55,-63,-64,-66,-68,128,-61,-72,-52,-25,-26,]),'COLON':([17,22,40,54,55,92,93,122,141,],[-5,34,-4,-77,94,-33,123,144,-32,]),'ADDOP':([24,48,64,68,69,70,71,72,73,75,76,77,78,79,80,81,82,83,84,87,104,105,106,107,108,109,110,111,128,129,131,132,133,134,153,154,],[38,76,38,76,76,-54,76,76,-56,106,76,-67,-69,-70,-71,-77,76,-75,-76,76,76,76,76,-74,76,76,-73,76,76,-55,106,106,-66,-68,-72,76,]),'ICONST':([24,38,48,64,68,69,71,72,76,82,87,95,104,105,106,108,109,111,128,147,148,154,164,],[39,65,83,39,83,83,83,83,83,83,83,126,83,83,83,83,83,83,83,159,160,83,166,]),'IF':([29,67,103,151,165,],[48,48,48,48,48,]),'FOR':([29,67,103,151,165,],[49,49,49,49,49,]),'READ':([29,67,103,151,165,],[50,50,50,50,50,]),'WRITE':([29,67,103,151,165,],[51,51,51,51,51,]),'ARRAY':([34,94,],[58,58,]),'INTEGER':([34,94,123,144,158,],[59,59,59,59,59,]),'REAL':([34,94,123,144,158,],[60,60,60,60,60,]),'CHAR':([34,94,123,144,158,],[61,61,61,61,61,]),'STRING':([34,94,123,144,158,],[62,62,62,62,62,]),'BOOLEAN':([34,94,123,144,158,],[63,63,63,63,63,]),'END':([42,43,45,46,47,66,70,73,75,77,78,79,80,81,83,84,97,98,99,107,110,127,129,130,131,132,133,134,137,139,150,152,153,161,167,],[66,-43,-57,-46,-47,-41,-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,-42,-44,-45,-74,-73,-58,-55,-77,-63,-64,-66,-68,-50,-51,-48,-60,-72,-59,-49,]),'ASSIGN':([44,45,70,73,85,129,],[68,69,-54,-56,111,-55,]),'ELSE':([45,46,47,66,70,73,75,77,78,79,80,81,83,84,98,99,107,110,127,129,130,131,132,133,134,137,139,150,152,153,161,167,],[-57,-46,-47,-41,-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,-44,-45,-74,-73,-58,-55,151,-63,-64,-66,-68,-50,-51,-48,-60,-72,-59,-49,]),'LBRACK':([45,58,81,114,],[72,95,72,72,]),'NOTOP':([48,68,69,71,72,76,82,87,104,105,106,108,109,111,128,154,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'RCONST':([48,68,69,71,72,76,82,87,104,105,106,108,109,111,128,154,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'MULDIVANDOP':([70,73,77,78,79,80,81,83,84,107,110,129,133,134,153,],[-54,-56,108,-69,-70,-71,-77,-75,-76,-74,-73,-55,108,-68,-72,]),'RELOP':([70,73,75,77,78,79,80,81,83,84,107,110,129,133,134,153,],[-54,-56,104,-67,-69,-70,-71,-77,-75,-76,-74,-73,-55,-66,-68,-72,]),'THEN':([70,73,74,75,77,78,79,80,81,83,84,107,110,129,131,132,133,134,153,],[-54,-56,103,-65,-67,-69,-70,-71,-77,-75,-76,-74,-73,-55,-63,-64,-66,-68,-72,]),'RBRACK':([70,73,75,77,78,79,80,81,83,84,102,107,110,125,129,131,132,133,134,153,160,166,],[-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,129,-74,-73,146,-55,-63,-64,-66,-68,-72,-25,-26,]),'TO':([70,73,75,77,78,79,80,81,83,84,107,110,129,131,132,133,134,136,153,],[-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,-74,-73,-55,-63,-64,-66,-68,154,-72,]),'DO':([70,73,75,77,78,79,80,81,83,84,107,110,129,131,132,133,134,153,162,],[-54,-56,-65,-67,-69,-70,-71,-77,-75,-76,-74,-73,-55,-63,-64,-66,-68,-72,165,]),'DOTDOT':([126,159,],[148,164,]),'OF':([146,],[158,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_head':([0,],[2,]),'program_body':([4,],[6,]),'const_declarations':([4,52,],[7,89,]),'empty':([4,7,12,45,52,53,54,81,89,114,130,],[9,14,20,73,9,92,92,73,14,73,152,]),'var_declarations':([7,89,],[12,116,]),'const_declaration':([8,],[15,]),'idlist':([10,13,33,91,121,142,],[18,22,55,122,122,122,]),'subprogram_declarations':([12,],[19,]),'var_declaration':([13,],[21,]),'compound_statement':([19,29,67,103,116,151,165,],[27,47,47,47,140,47,47,]),'subprogram':([19,],[28,]),'subprogram_head':([19,],[30,]),'const_value':([24,64,],[37,96,]),'statement_list':([29,],[42,]),'statement':([29,67,103,151,165,],[43,97,130,161,167,]),'variable':([29,48,67,68,69,71,72,76,82,86,87,103,104,105,106,108,109,111,128,138,151,154,165,],[44,80,44,80,80,80,80,80,80,113,80,44,80,80,80,80,80,80,80,155,44,80,44,]),'procedure_call':([29,67,103,151,165,],[46,46,46,46,46,]),'type':([34,94,],[56,124,]),'basic_type':([34,94,123,144,158,],[57,57,145,157,163,]),'id_varpart':([45,81,114,],[70,70,70,]),'expression':([48,68,69,71,72,87,109,111,128,154,],[74,98,99,101,102,101,101,136,149,162,]),'simple_expression':([48,68,69,71,72,87,104,105,109,111,128,154,],[75,75,75,75,75,75,131,132,75,75,75,75,]),'term':([48,68,69,71,72,87,104,105,106,109,111,128,154,],[77,77,77,77,77,77,77,77,133,77,77,77,77,]),'factor':([48,68,69,71,72,76,82,87,104,105,106,108,109,111,128,154,],[78,78,78,78,78,107,110,78,78,78,78,134,78,78,78,78,]),'number':([48,68,69,71,72,76,82,87,104,105,106,108,109,111,128,154,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'subprogram_body':([52,],[88,]),'formal_parameter':([53,54,],[90,93,]),'expression_list':([71,87,109,],[100,115,135,]),'variable_list':([86,],[112,]),'parameter_list':([91,],[117,]),'parameter':([91,142,],[118,156,]),'var_parameter':([91,142,],[119,119,]),'value_parameter':([91,121,142,],[120,143,120,]),'period':([95,],[125,]),'else_part':([130,],[150,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_head SEMI program_body DOT','program',4,'p_program','pparser.py',38),
  ('program_head -> PROGRAM ID','program_head',2,'p_program_head','pparser.py',42),
  ('program_head -> PROGRAM ID LPAREN idlist RPAREN','program_head',5,'p_program_head','pparser.py',43),
  ('idlist -> idlist COMMA ID','idlist',3,'p_idlist','pparser.py',51),
  ('idlist -> ID','idlist',1,'p_idlist','pparser.py',52),
  ('program_body -> const_declarations var_declarations subprogram_declarations compound_statement','program_body',4,'p_program_body','pparser.py',59),
  ('const_declarations -> CONST const_declaration SEMI','const_declarations',3,'p_const_declarations','pparser.py',63),
  ('const_declarations -> empty','const_declarations',1,'p_const_declarations','pparser.py',64),
  ('const_declaration -> ID EQU const_value','const_declaration',3,'p_const_declaration','pparser.py',69),
  ('const_declaration -> const_declaration SEMI ID EQU const_value','const_declaration',5,'p_const_declaration','pparser.py',70),
  ('const_value -> ADDOP ICONST','const_value',2,'p_const_value','pparser.py',77),
  ('const_value -> ICONST','const_value',1,'p_const_value','pparser.py',78),
  ('const_value -> ID','const_value',1,'p_const_value','pparser.py',79),
  ('var_declarations -> VAR var_declaration SEMI','var_declarations',3,'p_var_declarations','pparser.py',83),
  ('var_declarations -> empty','var_declarations',1,'p_var_declarations','pparser.py',84),
  ('var_declaration -> idlist COLON type','var_declaration',3,'p_var_declaration','pparser.py',89),
  ('var_declaration -> var_declaration SEMI idlist COLON type','var_declaration',5,'p_var_declaration','pparser.py',90),
  ('type -> basic_type','type',1,'p_type','pparser.py',97),
  ('type -> ARRAY LBRACK period RBRACK OF basic_type','type',6,'p_type','pparser.py',98),
  ('basic_type -> INTEGER','basic_type',1,'p_basic_type','pparser.py',105),
  ('basic_type -> REAL','basic_type',1,'p_basic_type','pparser.py',106),
  ('basic_type -> CHAR','basic_type',1,'p_basic_type','pparser.py',107),
  ('basic_type -> STRING','basic_type',1,'p_basic_type','pparser.py',108),
  ('basic_type -> BOOLEAN','basic_type',1,'p_basic_type','pparser.py',109),
  ('period -> ICONST DOTDOT ICONST','period',3,'p_period','pparser.py',113),
  ('period -> period COMMA ICONST DOTDOT ICONST','period',5,'p_period','pparser.py',114),
  ('subprogram_declarations -> subprogram_declarations subprogram SEMI','subprogram_declarations',3,'p_subprogram_declarations','pparser.py',122),
  ('subprogram_declarations -> empty','subprogram_declarations',1,'p_subprogram_declarations','pparser.py',123),
  ('subprogram -> subprogram_head SEMI subprogram_body','subprogram',3,'p_subprogram','pparser.py',130),
  ('subprogram_head -> PROCEDURE ID formal_parameter','subprogram_head',3,'p_subprogram_head','pparser.py',134),
  ('subprogram_head -> FUNCTION ID formal_parameter COLON basic_type','subprogram_head',5,'p_subprogram_head','pparser.py',135),
  ('formal_parameter -> LPAREN parameter_list RPAREN','formal_parameter',3,'p_formal_parameter','pparser.py',142),
  ('formal_parameter -> empty','formal_parameter',1,'p_formal_parameter','pparser.py',143),
  ('parameter_list -> parameter_list SEMI parameter','parameter_list',3,'p_parameter_list','pparser.py',150),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','pparser.py',151),
  ('parameter -> var_parameter','parameter',1,'p_parameter','pparser.py',158),
  ('parameter -> value_parameter','parameter',1,'p_parameter','pparser.py',159),
  ('var_parameter -> VAR value_parameter','var_parameter',2,'p_var_parameter','pparser.py',163),
  ('value_parameter -> idlist COLON basic_type','value_parameter',3,'p_value_parameter','pparser.py',167),
  ('subprogram_body -> const_declarations var_declarations compound_statement','subprogram_body',3,'p_subprogram_body','pparser.py',171),
  ('compound_statement -> BEGIN statement_list END','compound_statement',3,'p_compound_statement','pparser.py',175),
  ('statement_list -> statement_list SEMI statement','statement_list',3,'p_statement_list','pparser.py',179),
  ('statement_list -> statement','statement_list',1,'p_statement_list','pparser.py',180),
  ('statement -> variable ASSIGN expression','statement',3,'p_statement','pparser.py',187),
  ('statement -> ID ASSIGN expression','statement',3,'p_statement','pparser.py',188),
  ('statement -> procedure_call','statement',1,'p_statement','pparser.py',189),
  ('statement -> compound_statement','statement',1,'p_statement','pparser.py',190),
  ('statement -> IF expression THEN statement else_part','statement',5,'p_statement','pparser.py',191),
  ('statement -> FOR ID ASSIGN expression TO expression DO statement','statement',8,'p_statement','pparser.py',192),
  ('statement -> READ LPAREN variable_list RPAREN','statement',4,'p_statement','pparser.py',193),
  ('statement -> WRITE LPAREN expression_list RPAREN','statement',4,'p_statement','pparser.py',194),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','pparser.py',209),
  ('variable_list -> variable','variable_list',1,'p_variable_list','pparser.py',210),
  ('variable -> ID id_varpart','variable',2,'p_variable','pparser.py',217),
  ('id_varpart -> LBRACK expression RBRACK','id_varpart',3,'p_id_varpart','pparser.py',224),
  ('id_varpart -> empty','id_varpart',1,'p_id_varpart','pparser.py',225),
  ('procedure_call -> ID','procedure_call',1,'p_procedure_call','pparser.py',230),
  ('procedure_call -> ID LPAREN expression_list RPAREN','procedure_call',4,'p_procedure_call','pparser.py',231),
  ('else_part -> ELSE statement','else_part',2,'p_else_part','pparser.py',238),
  ('else_part -> empty','else_part',1,'p_else_part','pparser.py',239),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','pparser.py',244),
  ('expression_list -> expression','expression_list',1,'p_expression_list','pparser.py',245),
  ('expression -> simple_expression RELOP simple_expression','expression',3,'p_expression','pparser.py',252),
  ('expression -> simple_expression EQU simple_expression','expression',3,'p_expression','pparser.py',253),
  ('expression -> simple_expression','expression',1,'p_expression','pparser.py',254),
  ('simple_expression -> simple_expression ADDOP term','simple_expression',3,'p_simple_expression','pparser.py',261),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression','pparser.py',262),
  ('term -> term MULDIVANDOP factor','term',3,'p_term','pparser.py',269),
  ('term -> factor','term',1,'p_term','pparser.py',270),
  ('factor -> number','factor',1,'p_factor','pparser.py',277),
  ('factor -> variable','factor',1,'p_factor','pparser.py',278),
  ('factor -> ID LPAREN expression_list RPAREN','factor',4,'p_factor','pparser.py',279),
  ('factor -> NOTOP factor','factor',2,'p_factor','pparser.py',280),
  ('factor -> ADDOP factor','factor',2,'p_factor','pparser.py',281),
  ('number -> ICONST','number',1,'p_number','pparser.py',290),
  ('number -> RCONST','number',1,'p_number','pparser.py',291),
  ('empty -> <empty>','empty',0,'p_empty','pparser.py',295),
]
