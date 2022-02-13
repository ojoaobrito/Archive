
(* The type of tokens. *)

type token = 
  | WHILE
  | VAR_DEF
  | VAR
  | TRUE
  | TIMES
  | THEN
  | SMALLEQUAL
  | SMALL
  | SEQ
  | RP
  | RB
  | PRINT
  | PLUS
  | PASS
  | NEG
  | MINUS
  | LP
  | LB
  | INT_KEYWORD
  | INT of (int)
  | IN
  | IF
  | IDENT of (string)
  | FOREACH
  | FALSE
  | EQ
  | EOF
  | ELSE
  | DOUBLE_DOT
  | DOT_DOT
  | DO
  | DIV
  | COMP
  | BIGEQUAL
  | BIG

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val prog: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.program)
