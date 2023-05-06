
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftELSEleftLPARENLBRACKrightASSIGNADDOP ARRAY ASSIGN BCONST BEGIN BOOLEAN CCONST CHAR COLON COMMA CONST DO DOT DOTDOT DOWNTO ELSE END EOF EQU FOR FORWARD FUNCTION ICONST ID IF INOP INTEGER INTEGER LBRACK LCURL LPAREN MULDIVANDOP NOTOP OF OROP PROCEDURE PROGRAM RBRACK RCONST RCURL READ READLN REAL RECORD RELOP RPAREN SEMI SET STRING THEN TO TYPE TYPE_STRING VAR WHILE WITH WRITE WRITELNprogram : program_head SEMI program_body DOTprogram_head : PROGRAM ID \n                        | PROGRAM ID LPAREN idlist RPARENidlist : idlist COMMA ID\n                  | IDidlist : idlist error ID\n                  | ID errorprogram_body : const_declarations var_declarations subprogram_declarations compound_statementconst_declarations : CONST const_declaration SEMI\n                              | emptyconst_declaration : ID EQU const_value \n                             | const_declaration SEMI ID EQU const_valueconst_declaration : ID EQU error ID\n                             | const_declaration SEMI ID EQU error IDconst_value : ADDOP ICONST\n                    | ICONST\n                    | RCONST\n                    | CCONST\n                    | BCONST\n                    | stringvar_declarations : VAR var_declaration SEMI\n                            | emptyvar_declaration : idlist COLON type\n                           | var_declaration SEMI idlist COLON typetype : basic_type\n                | ARRAY LBRACK period RBRACK OF basic_typebasic_type : INTEGER\n                      | REAL\n                      | CHAR\n                      | BOOLEAN\n                      | TYPE_STRINGmy_period_part : ADDOP ICONST\n                          | ICONST\n                          | CCONST\n                          | IDperiod : my_period_part DOTDOT my_period_part\n                  | period COMMA my_period_part DOTDOT my_period_partsubprogram_declarations : subprogram_declarations subprogram SEMI\n                                   | emptysubprogram : subprogram_head SEMI subprogram_bodysubprogram_head : PROCEDURE ID formal_parameter\n                           | FUNCTION ID formal_parameter COLON basic_typeformal_parameter : LPAREN parameter_list RPAREN\n                            | emptyparameter_list : parameter_list SEMI parameter\n                          | parameterparameter : var_parameter\n                     | value_parametervar_parameter : VAR value_parametervalue_parameter : idlist COLON basic_typevalue_parameter : idlist error basic_typesubprogram_body : const_declarations var_declarations compound_statementcompound_statement : BEGIN statement_list ENDstatement_list : statement_list SEMI statement\n                          | statementstatement : empty\n                     | variable ASSIGN expression\n                     | procedure_call\n                     | compound_statement\n                     | IF expression THEN statement else_part\n                     | FOR ID ASSIGN expression TO expression DO statement\n                     | READ LPAREN variable_list RPAREN\n                     | WRITE LPAREN expression_list RPAREN\n                     | READLN LPAREN variable_list RPAREN\n                     | WRITELN LPAREN expression_list RPARENvariable_list : variable_list COMMA variable\n                         | variablevariable : ID id_varpartid_varpart : LBRACK expression_list RBRACK\n                      | emptyprocedure_call : ID\n                          | ID LPAREN expression_list RPARENelse_part : ELSE statement\n                     | emptyexpression_list : expression_list COMMA expression\n                           | expressionexpression : simple_expression RELOP simple_expression\n                      | simple_expression EQU simple_expression\n                      | simple_expressionsimple_expression : simple_expression ADDOP term\n                                | simple_expression OROP term\n                             | termterm : term MULDIVANDOP factor\n                | factorfactor : const_value\n                  | variable\n                  | LPAREN expression RPAREN\n                  | ID LPAREN expression_list RPAREN\n                  | NOTOP factor\n                  | ADDOP factorstring : STRINGempty :'
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,11,],[0,-1,]),'SEMI':([2,5,15,21,26,30,31,32,38,41,42,43,44,45,46,50,51,52,54,55,58,64,67,68,70,71,72,73,74,76,77,78,79,82,84,85,86,87,89,92,95,100,102,104,108,110,111,112,117,118,122,134,135,136,137,141,148,149,150,151,152,153,154,155,158,160,161,163,164,165,166,167,169,172,177,178,179,180,184,185,186,190,192,194,196,],[4,-2,23,35,-3,49,-92,63,-11,-16,-17,-18,-19,-20,-91,79,-55,-56,-58,-59,-71,-92,-23,-25,-27,-28,-29,-30,-31,-13,-15,-53,-92,-79,-82,-84,-85,-86,-92,-68,-70,-40,-41,-44,-12,-54,-57,-92,-90,-15,-89,168,-46,-47,-48,-24,-14,-92,-77,-78,-80,-81,-83,-87,-72,-69,-62,-63,-64,-65,-52,-43,-49,-42,-60,-92,-74,-88,-45,-50,-51,-73,-26,-92,-61,]),'ID':([3,8,10,13,23,27,28,31,33,34,35,39,56,57,79,80,83,88,90,93,94,96,97,98,99,103,107,109,112,113,114,115,116,119,121,123,138,159,162,168,171,174,175,178,181,193,194,],[5,16,17,17,37,47,48,58,64,65,17,76,89,91,58,89,89,89,89,89,89,129,89,129,89,17,147,148,58,89,89,89,89,89,89,89,17,89,129,17,48,147,147,58,89,147,58,]),'CONST':([4,63,],[8,8,]),'VAR':([4,7,9,23,63,101,103,168,],[-92,13,-10,-9,-92,13,138,138,]),'BEGIN':([4,7,9,12,14,19,20,23,31,35,49,63,79,101,112,133,178,194,],[-92,-92,-10,-92,-22,31,-39,-9,31,-21,-38,-92,31,-92,31,31,31,31,]),'PROCEDURE':([4,7,9,12,14,19,20,23,35,49,],[-92,-92,-10,-92,-22,33,-39,-9,-21,-38,]),'FUNCTION':([4,7,9,12,14,19,20,23,35,49,],[-92,-92,-10,-92,-22,34,-39,-9,-21,-38,]),'LPAREN':([5,56,58,59,60,61,62,64,65,80,83,88,89,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[10,88,93,96,97,98,99,103,103,88,88,88,121,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'DOT':([6,29,78,],[11,-8,-53,]),'EQU':([16,37,41,42,43,44,45,46,82,84,85,86,87,89,92,95,117,118,122,152,153,154,155,160,180,],[24,75,-16,-17,-18,-19,-20,-91,114,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,-80,-81,-83,-87,-69,-88,]),'RPAREN':([17,18,25,41,42,43,44,45,46,47,48,70,71,72,73,74,82,84,85,86,87,89,92,95,117,118,120,122,124,125,127,128,129,130,131,132,134,135,136,137,150,151,152,153,154,155,156,160,169,180,182,183,184,185,186,],[-5,26,-7,-16,-17,-18,-19,-20,-91,-4,-6,-27,-28,-29,-30,-31,-79,-82,-84,-85,-86,-92,-68,-70,-90,-15,155,-89,158,-76,161,-67,-92,163,164,165,167,-46,-47,-48,-77,-78,-80,-81,-83,-87,180,-69,-49,-88,-75,-66,-45,-50,-51,]),'COMMA':([17,18,22,25,41,42,43,44,45,46,47,48,66,82,84,85,86,87,89,92,95,117,118,122,124,125,126,127,128,129,130,131,132,139,142,145,146,147,150,151,152,153,154,155,156,160,176,180,182,183,189,195,],[-5,27,27,-7,-16,-17,-18,-19,-20,-91,-4,-6,27,-79,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,159,-76,159,162,-67,-92,159,162,159,27,174,-33,-34,-35,-77,-78,-80,-81,-83,-87,159,-69,-32,-88,-75,-66,-36,-37,]),'error':([17,18,22,24,25,47,48,66,75,139,],[25,28,28,39,-7,-4,-6,28,109,171,]),'COLON':([17,22,25,47,48,65,66,104,105,139,167,],[-5,36,-7,-4,-6,-92,106,-44,140,170,-43,]),'ADDOP':([24,41,42,43,44,45,46,56,75,80,82,83,84,85,86,87,88,89,90,92,93,94,95,97,99,107,113,114,115,116,117,118,119,121,122,123,150,151,152,153,154,155,159,160,174,175,180,181,193,],[40,-16,-17,-18,-19,-20,-91,83,40,83,115,83,-82,-84,-85,-86,83,-92,83,-68,83,83,-70,83,83,144,83,83,83,83,-90,-15,83,83,-89,83,115,115,-80,-81,-83,-87,83,-69,144,144,-88,83,144,]),'ICONST':([24,40,56,75,80,83,88,90,93,94,97,99,107,113,114,115,116,119,121,123,144,159,174,175,181,193,],[41,77,41,41,41,118,41,41,41,41,41,41,145,41,41,41,41,41,41,41,176,41,145,145,41,145,]),'RCONST':([24,56,75,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'CCONST':([24,56,75,80,83,88,90,93,94,97,99,107,113,114,115,116,119,121,123,159,174,175,181,193,],[43,43,43,43,43,43,43,43,43,43,43,146,43,43,43,43,43,43,43,43,146,146,43,146,]),'BCONST':([24,56,75,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'STRING':([24,56,75,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'IF':([31,79,112,178,194,],[56,56,56,56,56,]),'FOR':([31,79,112,178,194,],[57,57,57,57,57,]),'READ':([31,79,112,178,194,],[59,59,59,59,59,]),'WRITE':([31,79,112,178,194,],[60,60,60,60,60,]),'READLN':([31,79,112,178,194,],[61,61,61,61,61,]),'WRITELN':([31,79,112,178,194,],[62,62,62,62,62,]),'END':([31,41,42,43,44,45,46,50,51,52,54,55,58,78,79,82,84,85,86,87,89,92,95,110,111,112,117,118,122,149,150,151,152,153,154,155,158,160,161,163,164,165,177,178,179,180,190,194,196,],[-92,-16,-17,-18,-19,-20,-91,78,-55,-56,-58,-59,-71,-53,-92,-79,-82,-84,-85,-86,-92,-68,-70,-54,-57,-92,-90,-15,-89,-92,-77,-78,-80,-81,-83,-87,-72,-69,-62,-63,-64,-65,-60,-92,-74,-88,-73,-92,-61,]),'ARRAY':([36,106,],[69,69,]),'INTEGER':([36,106,140,170,171,187,],[70,70,70,70,70,70,]),'REAL':([36,106,140,170,171,187,],[71,71,71,71,71,71,]),'CHAR':([36,106,140,170,171,187,],[72,72,72,72,72,72,]),'BOOLEAN':([36,106,140,170,171,187,],[73,73,73,73,73,73,]),'TYPE_STRING':([36,106,140,170,171,187,],[74,74,74,74,74,74,]),'MULDIVANDOP':([41,42,43,44,45,46,84,85,86,87,89,92,95,117,118,122,152,153,154,155,160,180,],[-16,-17,-18,-19,-20,-91,119,-84,-85,-86,-92,-68,-70,-90,-15,-89,119,119,-83,-87,-69,-88,]),'RELOP':([41,42,43,44,45,46,82,84,85,86,87,89,92,95,117,118,122,152,153,154,155,160,180,],[-16,-17,-18,-19,-20,-91,113,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,-80,-81,-83,-87,-69,-88,]),'OROP':([41,42,43,44,45,46,82,84,85,86,87,89,92,95,117,118,122,150,151,152,153,154,155,160,180,],[-16,-17,-18,-19,-20,-91,116,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,116,116,-80,-81,-83,-87,-69,-88,]),'THEN':([41,42,43,44,45,46,81,82,84,85,86,87,89,92,95,117,118,122,150,151,152,153,154,155,160,180,],[-16,-17,-18,-19,-20,-91,112,-79,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,-77,-78,-80,-81,-83,-87,-69,-88,]),'ELSE':([41,42,43,44,45,46,52,54,55,58,78,82,84,85,86,87,89,92,95,111,112,117,118,122,149,150,151,152,153,154,155,158,160,161,163,164,165,177,178,179,180,190,194,196,],[-16,-17,-18,-19,-20,-91,-56,-58,-59,-71,-53,-79,-82,-84,-85,-86,-92,-68,-70,-57,-92,-90,-15,-89,178,-77,-78,-80,-81,-83,-87,-72,-69,-62,-63,-64,-65,-60,-92,-74,-88,-73,-92,-61,]),'RBRACK':([41,42,43,44,45,46,82,84,85,86,87,89,92,95,117,118,122,125,126,142,145,146,147,150,151,152,153,154,155,160,176,180,182,189,195,],[-16,-17,-18,-19,-20,-91,-79,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,-76,160,173,-33,-34,-35,-77,-78,-80,-81,-83,-87,-69,-32,-88,-75,-36,-37,]),'TO':([41,42,43,44,45,46,82,84,85,86,87,89,92,95,117,118,122,150,151,152,153,154,155,157,160,180,],[-16,-17,-18,-19,-20,-91,-79,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,-77,-78,-80,-81,-83,-87,181,-69,-88,]),'DO':([41,42,43,44,45,46,82,84,85,86,87,89,92,95,117,118,122,150,151,152,153,154,155,160,180,191,],[-16,-17,-18,-19,-20,-91,-79,-82,-84,-85,-86,-92,-68,-70,-90,-15,-89,-77,-78,-80,-81,-83,-87,-69,-88,194,]),'ASSIGN':([53,58,91,92,95,160,],[80,-92,123,-68,-70,-69,]),'NOTOP':([56,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'LBRACK':([58,69,89,129,],[94,107,94,94,]),'DOTDOT':([143,145,146,147,176,188,],[175,-33,-34,-35,-32,193,]),'OF':([173,],[187,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_head':([0,],[2,]),'program_body':([4,],[6,]),'const_declarations':([4,63,],[7,101,]),'empty':([4,7,12,31,58,63,64,65,79,89,101,112,129,149,178,194,],[9,14,20,52,95,9,104,104,52,95,14,52,95,179,52,52,]),'var_declarations':([7,101,],[12,133,]),'const_declaration':([8,],[15,]),'idlist':([10,13,35,103,138,168,],[18,22,66,139,139,139,]),'subprogram_declarations':([12,],[19,]),'var_declaration':([13,],[21,]),'compound_statement':([19,31,79,112,133,178,194,],[29,55,55,55,166,55,55,]),'subprogram':([19,],[30,]),'subprogram_head':([19,],[32,]),'const_value':([24,56,75,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[38,86,108,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'string':([24,56,75,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'statement_list':([31,],[50,]),'statement':([31,79,112,178,194,],[51,110,149,190,196,]),'variable':([31,56,79,80,83,88,90,93,94,96,97,98,99,112,113,114,115,116,119,121,123,159,162,178,181,194,],[53,87,53,87,87,87,87,87,87,128,87,128,87,53,87,87,87,87,87,87,87,87,183,53,87,53,]),'procedure_call':([31,79,112,178,194,],[54,54,54,54,54,]),'type':([36,106,],[67,141,]),'basic_type':([36,106,140,170,171,187,],[68,68,172,185,186,192,]),'expression':([56,80,88,93,94,97,99,121,123,159,181,],[81,111,120,125,125,125,125,125,157,182,191,]),'simple_expression':([56,80,88,93,94,97,99,113,114,121,123,159,181,],[82,82,82,82,82,82,82,150,151,82,82,82,82,]),'term':([56,80,88,93,94,97,99,113,114,115,116,121,123,159,181,],[84,84,84,84,84,84,84,84,84,152,153,84,84,84,84,]),'factor':([56,80,83,88,90,93,94,97,99,113,114,115,116,119,121,123,159,181,],[85,85,117,85,122,85,85,85,85,85,85,85,85,154,85,85,85,85,]),'id_varpart':([58,89,129,],[92,92,92,]),'subprogram_body':([63,],[100,]),'formal_parameter':([64,65,],[102,105,]),'expression_list':([93,94,97,99,121,],[124,126,130,132,156,]),'variable_list':([96,98,],[127,131,]),'parameter_list':([103,],[134,]),'parameter':([103,168,],[135,184,]),'var_parameter':([103,168,],[136,136,]),'value_parameter':([103,138,168,],[137,169,137,]),'period':([107,],[142,]),'my_period_part':([107,174,175,193,],[143,188,189,195,]),'else_part':([149,],[177,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_head SEMI program_body DOT','program',4,'p_program','pparser.py',55),
  ('program_head -> PROGRAM ID','program_head',2,'p_program_head','pparser.py',59),
  ('program_head -> PROGRAM ID LPAREN idlist RPAREN','program_head',5,'p_program_head','pparser.py',60),
  ('idlist -> idlist COMMA ID','idlist',3,'p_idlist','pparser.py',68),
  ('idlist -> ID','idlist',1,'p_idlist','pparser.py',69),
  ('idlist -> idlist error ID','idlist',3,'p_wrong_idlist','pparser.py',76),
  ('idlist -> ID error','idlist',2,'p_wrong_idlist','pparser.py',77),
  ('program_body -> const_declarations var_declarations subprogram_declarations compound_statement','program_body',4,'p_program_body','pparser.py',84),
  ('const_declarations -> CONST const_declaration SEMI','const_declarations',3,'p_const_declarations','pparser.py',88),
  ('const_declarations -> empty','const_declarations',1,'p_const_declarations','pparser.py',89),
  ('const_declaration -> ID EQU const_value','const_declaration',3,'p_const_declaration','pparser.py',96),
  ('const_declaration -> const_declaration SEMI ID EQU const_value','const_declaration',5,'p_const_declaration','pparser.py',97),
  ('const_declaration -> ID EQU error ID','const_declaration',4,'p_wrong_const_declaration','pparser.py',108),
  ('const_declaration -> const_declaration SEMI ID EQU error ID','const_declaration',6,'p_wrong_const_declaration','pparser.py',109),
  ('const_value -> ADDOP ICONST','const_value',2,'p_const_value','pparser.py',121),
  ('const_value -> ICONST','const_value',1,'p_const_value','pparser.py',122),
  ('const_value -> RCONST','const_value',1,'p_const_value','pparser.py',123),
  ('const_value -> CCONST','const_value',1,'p_const_value','pparser.py',124),
  ('const_value -> BCONST','const_value',1,'p_const_value','pparser.py',125),
  ('const_value -> string','const_value',1,'p_const_value','pparser.py',126),
  ('var_declarations -> VAR var_declaration SEMI','var_declarations',3,'p_var_declarations','pparser.py',143),
  ('var_declarations -> empty','var_declarations',1,'p_var_declarations','pparser.py',144),
  ('var_declaration -> idlist COLON type','var_declaration',3,'p_var_declaration','pparser.py',158),
  ('var_declaration -> var_declaration SEMI idlist COLON type','var_declaration',5,'p_var_declaration','pparser.py',159),
  ('type -> basic_type','type',1,'p_type','pparser.py',166),
  ('type -> ARRAY LBRACK period RBRACK OF basic_type','type',6,'p_type','pparser.py',167),
  ('basic_type -> INTEGER','basic_type',1,'p_basic_type','pparser.py',174),
  ('basic_type -> REAL','basic_type',1,'p_basic_type','pparser.py',175),
  ('basic_type -> CHAR','basic_type',1,'p_basic_type','pparser.py',176),
  ('basic_type -> BOOLEAN','basic_type',1,'p_basic_type','pparser.py',177),
  ('basic_type -> TYPE_STRING','basic_type',1,'p_basic_type','pparser.py',178),
  ('my_period_part -> ADDOP ICONST','my_period_part',2,'p_my_period_part','pparser.py',184),
  ('my_period_part -> ICONST','my_period_part',1,'p_my_period_part','pparser.py',185),
  ('my_period_part -> CCONST','my_period_part',1,'p_my_period_part','pparser.py',186),
  ('my_period_part -> ID','my_period_part',1,'p_my_period_part','pparser.py',187),
  ('period -> my_period_part DOTDOT my_period_part','period',3,'p_period','pparser.py',199),
  ('period -> period COMMA my_period_part DOTDOT my_period_part','period',5,'p_period','pparser.py',200),
  ('subprogram_declarations -> subprogram_declarations subprogram SEMI','subprogram_declarations',3,'p_subprogram_declarations','pparser.py',210),
  ('subprogram_declarations -> empty','subprogram_declarations',1,'p_subprogram_declarations','pparser.py',211),
  ('subprogram -> subprogram_head SEMI subprogram_body','subprogram',3,'p_subprogram','pparser.py',218),
  ('subprogram_head -> PROCEDURE ID formal_parameter','subprogram_head',3,'p_subprogram_head','pparser.py',222),
  ('subprogram_head -> FUNCTION ID formal_parameter COLON basic_type','subprogram_head',5,'p_subprogram_head','pparser.py',223),
  ('formal_parameter -> LPAREN parameter_list RPAREN','formal_parameter',3,'p_formal_parameter','pparser.py',230),
  ('formal_parameter -> empty','formal_parameter',1,'p_formal_parameter','pparser.py',231),
  ('parameter_list -> parameter_list SEMI parameter','parameter_list',3,'p_parameter_list','pparser.py',240),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','pparser.py',241),
  ('parameter -> var_parameter','parameter',1,'p_parameter','pparser.py',248),
  ('parameter -> value_parameter','parameter',1,'p_parameter','pparser.py',249),
  ('var_parameter -> VAR value_parameter','var_parameter',2,'p_var_parameter','pparser.py',253),
  ('value_parameter -> idlist COLON basic_type','value_parameter',3,'p_value_parameter','pparser.py',257),
  ('value_parameter -> idlist error basic_type','value_parameter',3,'p_wrong_value_parameter','pparser.py',261),
  ('subprogram_body -> const_declarations var_declarations compound_statement','subprogram_body',3,'p_subprogram_body','pparser.py',265),
  ('compound_statement -> BEGIN statement_list END','compound_statement',3,'p_compound_statement','pparser.py',269),
  ('statement_list -> statement_list SEMI statement','statement_list',3,'p_statement_list','pparser.py',273),
  ('statement_list -> statement','statement_list',1,'p_statement_list','pparser.py',274),
  ('statement -> empty','statement',1,'p_statement','pparser.py',281),
  ('statement -> variable ASSIGN expression','statement',3,'p_statement','pparser.py',282),
  ('statement -> procedure_call','statement',1,'p_statement','pparser.py',283),
  ('statement -> compound_statement','statement',1,'p_statement','pparser.py',284),
  ('statement -> IF expression THEN statement else_part','statement',5,'p_statement','pparser.py',285),
  ('statement -> FOR ID ASSIGN expression TO expression DO statement','statement',8,'p_statement','pparser.py',286),
  ('statement -> READ LPAREN variable_list RPAREN','statement',4,'p_statement','pparser.py',287),
  ('statement -> WRITE LPAREN expression_list RPAREN','statement',4,'p_statement','pparser.py',288),
  ('statement -> READLN LPAREN variable_list RPAREN','statement',4,'p_statement','pparser.py',289),
  ('statement -> WRITELN LPAREN expression_list RPAREN','statement',4,'p_statement','pparser.py',290),
  ('variable_list -> variable_list COMMA variable','variable_list',3,'p_variable_list','pparser.py',314),
  ('variable_list -> variable','variable_list',1,'p_variable_list','pparser.py',315),
  ('variable -> ID id_varpart','variable',2,'p_variable','pparser.py',322),
  ('id_varpart -> LBRACK expression_list RBRACK','id_varpart',3,'p_id_varpart','pparser.py',329),
  ('id_varpart -> empty','id_varpart',1,'p_id_varpart','pparser.py',330),
  ('procedure_call -> ID','procedure_call',1,'p_procedure_call','pparser.py',336),
  ('procedure_call -> ID LPAREN expression_list RPAREN','procedure_call',4,'p_procedure_call','pparser.py',337),
  ('else_part -> ELSE statement','else_part',2,'p_else_part','pparser.py',344),
  ('else_part -> empty','else_part',1,'p_else_part','pparser.py',345),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','pparser.py',350),
  ('expression_list -> expression','expression_list',1,'p_expression_list','pparser.py',351),
  ('expression -> simple_expression RELOP simple_expression','expression',3,'p_expression','pparser.py',358),
  ('expression -> simple_expression EQU simple_expression','expression',3,'p_expression','pparser.py',359),
  ('expression -> simple_expression','expression',1,'p_expression','pparser.py',360),
  ('simple_expression -> simple_expression ADDOP term','simple_expression',3,'p_simple_expression','pparser.py',367),
  ('simple_expression -> simple_expression OROP term','simple_expression',3,'p_simple_expression','pparser.py',368),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression','pparser.py',369),
  ('term -> term MULDIVANDOP factor','term',3,'p_term','pparser.py',376),
  ('term -> factor','term',1,'p_term','pparser.py',377),
  ('factor -> const_value','factor',1,'p_factor','pparser.py',384),
  ('factor -> variable','factor',1,'p_factor','pparser.py',385),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','pparser.py',386),
  ('factor -> ID LPAREN expression_list RPAREN','factor',4,'p_factor','pparser.py',387),
  ('factor -> NOTOP factor','factor',2,'p_factor','pparser.py',388),
  ('factor -> ADDOP factor','factor',2,'p_factor','pparser.py',389),
  ('string -> STRING','string',1,'p_string','pparser.py',404),
  ('empty -> <empty>','empty',0,'p_empty','pparser.py',408),
]
