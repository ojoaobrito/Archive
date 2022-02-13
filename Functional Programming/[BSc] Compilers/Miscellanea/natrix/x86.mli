(* CÓDIGO USADO *)
(* ------------------------------------------------- *)
type label = string
type 'a asm
type text = [ `text ] asm
type data = [ `data ] asm

type program = {
  text : text;
  data : data;
}

val print_program : Format.formatter -> program -> unit
val print_in_file: file:string -> program -> unit

(* registos *)
type register = string
val rax : register
val rbx : register
val rdx : register
val rbp : register
val rdi : register
val rsi : register
val esp : register

(* utilitários *)
val start : label ->  [> ] asm
val label : label ->  [> ] asm
val syscall : text
val nop : [> ] asm
val ( ++ ) : ([< `text|`data ] asm as 'a)-> 'a -> 'a
val comment : string -> [> ] asm
val comment_data : string -> [> ] asm
val newline : text
val newline_data : data
val glabel : label ->  [> ] asm
val label_jump : label ->  [> ] asm
val ret : text
val call : string -> text
val cmp_reg_reg : register -> register -> text
val cmp_var_reg : string -> register -> text
val jmp : label ->  [> ] asm
val je : label ->  [> ] asm
val jne : label ->  [> ] asm
val jz : label ->  [> ] asm
val jg : label ->  [> ] asm
val jge : label ->  [> ] asm
val jl : label ->  [> ] asm
val jle : label ->  [> ] asm

(* dados *)
val string_type : string -> data
val byte : int -> data
val quad : int -> data
val data_definition : label ->  [> ] asm

(* mover valores *)
val mov_reg_reg : register -> register -> text
val mov_val_reg : int -> register -> text
val mov_var_reg : string -> register -> text
val movabs : string -> register -> text

(* adição *)
val add_reg_reg : register -> register -> text
val add_val_reg : int -> register -> text
val add_val_var : int -> string -> text
val add_var_reg : string -> register -> text

(* subtração *)
val sub_reg_reg : register -> register -> text
val sub_val_reg : int -> register -> text
val sub_var_reg : string -> register -> text

(* multiplicação *)
val mul_reg_reg : register -> register -> text
val mul_val_reg : int -> register -> text
val mul_var_reg : string -> register -> text

(* divisão *)
val div_reg_reg : register -> text
val div_val_reg : register -> text
val div_var_reg : register -> text

(* gestão da pilha *)
val popq : register -> text
val popq_var : string -> text
val pushq : register -> text
val pushq_var : string -> text
(* ------------------------------------------------- *)