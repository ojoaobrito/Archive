
(* lexer para Natrix *)

{
    open Lexing
    open Parser

    exception Lexing_error of char

    let kwd_tbl = ["var", VAR; "print", PRINT; "if", IF; "then", THEN; "else", ELSE; "foreach", FOREACH; "in", IN; "while", WHILE; "do", DO; "true", TRUE; "false", FALSE; "int", INT_KEYWORD; "pass", PASS]
    let id_or_kwd s = try List.assoc s kwd_tbl with _ -> IDENT s

    let newline lexbuf =
		let pos = lexbuf.lex_curr_p in
		lexbuf.lex_curr_p <-
			{ pos with pos_lnum = pos.pos_lnum + 1; pos_bol = pos.pos_cnum }

}

(* tokens compostos *)
let letter = ['a'-'z' 'A'-'Z']
let digit = ['0'-'9']
let equal = ['=']
let big = ['>']
let small = ['<']
let bigequal = big equal
let smallequal = small equal
let comparison = equal equal
let double_dot = [':']
let var_def = double_dot equal
let double_bar = ['/'] ['/']
let dot_dot = ['.'] ['.']
let ident = letter (letter | digit)*
let integer = ['0'-'9']+
let space = [' ' '\t']
let others = ['(' ')' '{' '}' '-' '!' ';' '"' '@' '$' '%' '&' '/' '=' '?' '*' '+' '|' '_' '.' ':' ',' '<' '>']
let comment = double_bar (letter | digit | space | ident | comparison | integer | others | double_bar)* (['\n'] | eof)

rule token = parse
	| comment           { newline lexbuf; token lexbuf }
	| space+            { token lexbuf }
	| ident as id       { id_or_kwd id }
	| '\n'              { token lexbuf }
	| '+'               { PLUS }
	| '-'               { MINUS }
	| '*'               { TIMES }
	| '/'               { DIV }
	| '='               { EQ }
	| var_def						{ VAR_DEF }
	| comparison        { COMP }
	| big               { BIG }
	| small             { SMALL }
	| bigequal          { BIGEQUAL }
	| smallequal        { SMALLEQUAL }
	| dot_dot						{ DOT_DOT }
	| '!'               { NEG }
	| '('               { LP }
	| ')'               { RP }
	| '{'               { LB }
	| '}'               { RB }
	| ';'               { SEQ }
	| double_dot				{ DOUBLE_DOT }
	| integer as s      { INT (int_of_string s) }
	| eof               { EOF }
	| _ as c            { raise (Lexing_error c) }