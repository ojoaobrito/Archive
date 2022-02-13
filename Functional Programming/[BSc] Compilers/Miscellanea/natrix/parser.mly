
/* parser para Natrix */

%{
  open Ast
%}

%token <int> INT
%token <string> IDENT
%token PRINT, IF, THEN, ELSE, FOREACH, IN, DO, SEQ, TRUE, FALSE, PASS, VAR_DEF, DOT_DOT, VAR, WHILE, DOUBLE_DOT, INT_KEYWORD
%token EOF
%token LP RP LB RB
%token PLUS MINUS TIMES DIV
%token EQ
%token COMP BIG BIGEQUAL SMALL SMALLEQUAL NEG

/* definição das prioridades e associatividades dos tokens */
%left PLUS MINUS
%left TIMES DIV

/* ponto de entrada da gramática */
%start prog

/* tipo dos valores devolvidos pelo parser */
%type <Ast.program> prog
%%

prog:
| p = inst* EOF { p }
;

inst:                                                          
| VAR id = IDENT DOUBLE_DOT INT_KEYWORD EQ e = expr SEQ 	 				                    { Dec (id, e) }
| id = IDENT VAR_DEF e = expr SEQ 				                                            { Set (id, e) }
| PRINT e = expr SEQ                  	 				                                      { Print e }
| IF t = test THEN LB i1 = inst* RB ELSE LB i2 = inst* RB                             { Cond (t, i1, i2) }
| WHILE t = test DO LB i = inst* RB 				                                          { While (t, i) }
| FOREACH c = IDENT IN e1 = expr DOT_DOT e2 = expr DO LB i = inst* RB	                { For (c, e1, e2, i) }
| PASS SEQ    																											                  { Nop } /* não fazer nada */ 	 
;

expr:
| ci = INT                        					                                          { I ci }
| id = IDENT                     					                                            { Var id }
| e1 = expr o = op e2 = expr     					                                            { Op (o, e1, e2) }
| LP e = expr RP                					                                            { e }
;

test:
| TRUE                                                                                { B true }  
| FALSE                                                                               { B false }     
| e1 = expr COMP e2 = expr		 					                                              { Comp (e1, e2) }
| e1 = expr BIG e2 = expr		 					                                                { Big (e1, e2) }
| e1 = expr BIGEQUAL e2 = expr		 					                                          { BigEqual (e1, e2) }
| e1 = expr SMALL e2 = expr		 					                                              { Small (e1, e2) }
| e1 = expr SMALLEQUAL e2 = expr		 					                                        { SmallEqual (e1, e2) }
| NEG t = test		 			 					                                                    { Neg t }
;

%inline op:
| PLUS  				                                                                      { Add }
| MINUS 																														                  { Sub }
| TIMES 																											                        { Mul }
| DIV 																															                  { Div }
;