# 4 "lexer.mll"
 
    open Lexing
    open Parser

    exception Lexing_error of char

    let kwd_tbl = ["var", VAR; "print", PRINT; "if", IF; "then", THEN; "else", ELSE; "foreach", FOREACH; "in", IN; "while", WHILE; "do", DO; "true", TRUE; "false", FALSE; "int", INT_KEYWORD; "pass", PASS]
    let id_or_kwd s = try List.assoc s kwd_tbl with _ -> IDENT s

    let newline lexbuf =
		let pos = lexbuf.lex_curr_p in
		lexbuf.lex_curr_p <-
			{ pos with pos_lnum = pos.pos_lnum + 1; pos_bol = pos.pos_cnum }


# 18 "lexer.ml"
let __ocaml_lex_tables = {
  Lexing.lex_base = 
   "\000\000\230\255\231\255\078\000\234\255\235\255\236\255\237\255\
    \238\255\239\255\017\000\003\000\030\000\031\000\032\000\249\255\
    \250\255\251\255\252\255\088\000\002\000\047\000\217\000\255\255\
    \078\001\195\001\056\002\245\255\246\255\242\255\241\255\240\255\
    ";
  Lexing.lex_backtrk = 
   "\255\255\255\255\255\255\023\000\255\255\255\255\255\255\255\255\
    \255\255\255\255\025\000\012\000\011\000\022\000\008\000\255\255\
    \255\255\255\255\255\255\002\000\001\000\007\000\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    ";
  Lexing.lex_default = 
   "\001\000\000\000\000\000\255\255\000\000\000\000\000\000\000\000\
    \000\000\000\000\255\255\255\255\255\255\255\255\255\255\000\000\
    \000\000\000\000\000\000\255\255\255\255\255\255\255\255\000\000\
    \255\255\255\255\255\255\000\000\000\000\000\000\000\000\000\000\
    ";
  Lexing.lex_trans = 
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\020\000\018\000\020\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \020\000\009\000\020\000\000\000\000\000\000\000\000\000\000\000\
    \008\000\007\000\015\000\017\000\000\000\016\000\010\000\021\000\
    \003\000\003\000\003\000\003\000\003\000\003\000\003\000\003\000\
    \003\000\003\000\013\000\004\000\011\000\014\000\012\000\031\000\
    \030\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\029\000\028\000\027\000\022\000\000\000\
    \000\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\006\000\000\000\005\000\003\000\003\000\
    \003\000\003\000\003\000\003\000\003\000\003\000\003\000\003\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\022\000\023\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\022\000\022\000\022\000\000\000\022\000\022\000\022\000\
    \002\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \024\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\025\000\022\000\
    \022\000\022\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\000\000\000\000\000\000\000\000\
    \022\000\000\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\022\000\022\000\022\000\022\000\
    \023\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\022\000\022\000\
    \022\000\000\000\022\000\022\000\022\000\000\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\024\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\025\000\022\000\022\000\022\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\000\000\000\000\000\000\000\000\022\000\000\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\022\000\022\000\022\000\022\000\023\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\023\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\022\000\022\000\022\000\000\000\022\000\
    \022\000\022\000\000\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\024\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \025\000\022\000\022\000\022\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\000\000\000\000\
    \000\000\000\000\022\000\000\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\022\000\022\000\
    \022\000\022\000\023\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\023\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \022\000\022\000\022\000\000\000\022\000\022\000\022\000\000\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\024\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\022\000\022\000\022\000\025\000\022\000\022\000\
    \022\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\000\000\000\000\000\000\000\000\022\000\
    \000\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\022\000\022\000\022\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\023\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \023\000";
  Lexing.lex_check = 
   "\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\000\000\000\000\020\000\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \000\000\000\000\020\000\255\255\255\255\255\255\255\255\255\255\
    \000\000\000\000\000\000\000\000\255\255\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\010\000\
    \011\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\012\000\013\000\014\000\021\000\255\255\
    \255\255\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\255\255\000\000\003\000\003\000\
    \003\000\003\000\003\000\003\000\003\000\003\000\003\000\003\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\255\255\255\255\255\255\255\255\255\255\
    \255\255\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\019\000\019\000\019\000\019\000\019\000\
    \019\000\019\000\019\000\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\022\000\022\000\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\022\000\022\000\022\000\255\255\022\000\022\000\022\000\
    \000\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\255\255\255\255\255\255\255\255\
    \022\000\255\255\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\022\000\
    \022\000\022\000\022\000\022\000\022\000\022\000\022\000\024\000\
    \024\000\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\024\000\024\000\
    \024\000\255\255\024\000\024\000\024\000\255\255\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\255\255\255\255\255\255\255\255\024\000\255\255\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\024\000\024\000\024\000\024\000\
    \024\000\024\000\024\000\024\000\025\000\025\000\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\022\000\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\025\000\025\000\025\000\255\255\025\000\
    \025\000\025\000\255\255\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\255\255\255\255\
    \255\255\255\255\025\000\255\255\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\025\000\025\000\025\000\025\000\025\000\025\000\025\000\
    \025\000\026\000\026\000\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\024\000\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \026\000\026\000\026\000\255\255\026\000\026\000\026\000\255\255\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\255\255\255\255\255\255\255\255\026\000\
    \255\255\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\026\000\026\000\
    \026\000\026\000\026\000\026\000\026\000\026\000\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\025\000\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \026\000";
  Lexing.lex_base_code = 
   "";
  Lexing.lex_backtrk_code = 
   "";
  Lexing.lex_default_code = 
   "";
  Lexing.lex_trans_code = 
   "";
  Lexing.lex_check_code = 
   "";
  Lexing.lex_code = 
   "";
}

let rec token lexbuf =
    __ocaml_lex_token_rec lexbuf 0
and __ocaml_lex_token_rec lexbuf __ocaml_lex_state =
  match Lexing.engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 40 "lexer.mll"
                     ( newline lexbuf; token lexbuf )
# 269 "lexer.ml"

  | 1 ->
# 41 "lexer.mll"
                     ( token lexbuf )
# 274 "lexer.ml"

  | 2 ->
let
# 42 "lexer.mll"
            id
# 280 "lexer.ml"
= Lexing.sub_lexeme lexbuf lexbuf.Lexing.lex_start_pos lexbuf.Lexing.lex_curr_pos in
# 42 "lexer.mll"
                     ( id_or_kwd id )
# 284 "lexer.ml"

  | 3 ->
# 43 "lexer.mll"
                     ( token lexbuf )
# 289 "lexer.ml"

  | 4 ->
# 44 "lexer.mll"
                     ( PLUS )
# 294 "lexer.ml"

  | 5 ->
# 45 "lexer.mll"
                     ( MINUS )
# 299 "lexer.ml"

  | 6 ->
# 46 "lexer.mll"
                     ( TIMES )
# 304 "lexer.ml"

  | 7 ->
# 47 "lexer.mll"
                     ( DIV )
# 309 "lexer.ml"

  | 8 ->
# 48 "lexer.mll"
                     ( EQ )
# 314 "lexer.ml"

  | 9 ->
# 49 "lexer.mll"
                ( VAR_DEF )
# 319 "lexer.ml"

  | 10 ->
# 50 "lexer.mll"
                     ( COMP )
# 324 "lexer.ml"

  | 11 ->
# 51 "lexer.mll"
                     ( BIG )
# 329 "lexer.ml"

  | 12 ->
# 52 "lexer.mll"
                     ( SMALL )
# 334 "lexer.ml"

  | 13 ->
# 53 "lexer.mll"
                     ( BIGEQUAL )
# 339 "lexer.ml"

  | 14 ->
# 54 "lexer.mll"
                     ( SMALLEQUAL )
# 344 "lexer.ml"

  | 15 ->
# 55 "lexer.mll"
                ( DOT_DOT )
# 349 "lexer.ml"

  | 16 ->
# 56 "lexer.mll"
                     ( NEG )
# 354 "lexer.ml"

  | 17 ->
# 57 "lexer.mll"
                     ( LP )
# 359 "lexer.ml"

  | 18 ->
# 58 "lexer.mll"
                     ( RP )
# 364 "lexer.ml"

  | 19 ->
# 59 "lexer.mll"
                     ( LB )
# 369 "lexer.ml"

  | 20 ->
# 60 "lexer.mll"
                     ( RB )
# 374 "lexer.ml"

  | 21 ->
# 61 "lexer.mll"
                     ( SEQ )
# 379 "lexer.ml"

  | 22 ->
# 62 "lexer.mll"
                 ( DOUBLE_DOT )
# 384 "lexer.ml"

  | 23 ->
let
# 63 "lexer.mll"
              s
# 390 "lexer.ml"
= Lexing.sub_lexeme lexbuf lexbuf.Lexing.lex_start_pos lexbuf.Lexing.lex_curr_pos in
# 63 "lexer.mll"
                     ( INT (int_of_string s) )
# 394 "lexer.ml"

  | 24 ->
# 64 "lexer.mll"
                     ( EOF )
# 399 "lexer.ml"

  | 25 ->
let
# 65 "lexer.mll"
        c
# 405 "lexer.ml"
= Lexing.sub_lexeme_char lexbuf lexbuf.Lexing.lex_start_pos in
# 65 "lexer.mll"
                     ( raise (Lexing_error c) )
# 409 "lexer.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf; 
      __ocaml_lex_token_rec lexbuf __ocaml_lex_state

;;
