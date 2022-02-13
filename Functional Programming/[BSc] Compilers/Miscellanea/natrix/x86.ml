open Format

(* registos *)
type register =  string
let rax : register = "rax"
let rbx : register = "rbx"
let rdx : register = "rdx"
let rbp : register = "rbp"
let rdi : register = "rdi"
let rsi : register = "rsi"
let esp : register = "esp"

type label = string
type 'a asm =
  | Nop
  | S of string
  | Cat of 'a asm * 'a asm

type text = [`text ] asm
type data = [`data ] asm

type program = {
  text : [ `text ] asm;
  data : [ `data ] asm;
}

let buf = Buffer.create 17
let fmt = formatter_of_buffer buf

let ins x =
  Buffer.add_char buf '\t';
  kfprintf (fun fmt ->
    fprintf fmt;
    pp_print_flush fmt ();
    let s = Buffer.contents buf in
    Buffer.clear buf;
    S s
  ) fmt x

(* CÓDIGO USADO *)
(* --------------------------------------------------------------- *)
(* utilitários *)
let start (s : label) = S (s)
let label (s : label) = S (s ^ ": ")
let syscall = S "\tsyscall\n"
let nop = Nop
let (++) x y = Cat (x, y)
let comment s = S ("\t# " ^ s)
let comment_data s = S ("\t# " ^ s)
let newline = S "\n"
let newline_data = S "\n" (* é igual ao newline mas é do tipo data *)
let glabel (s : label) = S (s ^ ":")
let label_jump (s : label) = S (s ^ ":")
let ret = ins "ret"
let call (s : label) = ins "call %s" s
let cmp_reg_reg a b = ins "cmp %%%s, %%%s" a b
let cmp_var_reg a b = ins "cmp %s, %%%s" a b
let jmp (s : label) = ins "jmp %s" s 
let jne (s : label) = ins "jne %s" s 
let je (s : label) = ins "je %s" s 
let jz (s : label) = ins "jz %s" s
let jg (s : label) = ins "jg %s" s
let jge (s : label) = ins "jge %s" s
let jl (s : label) = ins "jl %s" s 
let jle (s : label) = ins "jle %s" s 

(* dados *)
let string_type s = ins ".string %S" s
let byte l = ins ".byte %i" l
let quad l = ins ".quad %i" l
let data_definition (s : label) = S (s)

(* mover valores *)
let mov_reg_reg a b = ins "mov %%%s, %%%s" a b
let mov_val_reg a b = ins "mov $%i, %%%s" a b
let mov_var_reg a b = ins "mov %s, %%%s" a b
let movabs a b = ins "mov $%s, %%%s" a b

(* adição *)
let add_reg_reg a b = ins "add %%%s, %%%s" a b
let add_val_reg a b = ins "add $%i, %%%s" a b
let add_val_var a b = ins "add $%i, %s" a b
let add_var_reg a b = ins "add $%s, %%%s" a b

(* subtração *)
let sub_reg_reg a b = ins "sub %%%s, %%%s" a b
let sub_val_reg a b = ins "sub $%i, %%%s" a b
let sub_var_reg a b = ins "sub $%s, %%%s" a b

(* multiplicação *)
let mul_reg_reg a b = ins "imul %%%s, %%%s" a b
let mul_val_reg a b = ins "imul $%i, %%%s" a b
let mul_var_reg a b = ins "imul $%s, %%%s" a b

(* divisão *)
let div_reg_reg a = ins "idivq %%%s" a
let div_val_reg a = ins "idivq %%%s" a
let div_var_reg a = ins "idivq %%%s" a

(* gestão da pilha *)
let pushq r = ins "pushq %%%s" r
let pushq_var r = ins "pushq %s" r
let popq r = ins "popq %%%s" r
let popq_var r = ins "popq %s" r
(* --------------------------------------------------------------- *)

(* IMPRESSÃO PARA O FICHEIRO ALVO *)
(* ------------------------------------------------------------------ *)
let pr_list fmt pr = function
  | []      -> ()
  | [i]     -> pr fmt i
  | i :: ll -> pr fmt i; List.iter (fun i -> fprintf fmt ", %a" pr i) ll

let pr_ilist fmt l =
  pr_list fmt (fun fmt i -> fprintf fmt "%i" i) l

let pr_alist fmt l =
  pr_list fmt (fun fmt (a : label) -> fprintf fmt "%s" a) l

let rec pr_asm fmt = function
  | Nop          -> ()
  | S s          -> fprintf fmt "%s" s
  | Cat (a1, a2) -> pr_asm fmt a1; pr_asm fmt a2

let print_program fmt p =
  pr_asm fmt p.text;
  pr_asm fmt p.data;
  pp_print_flush fmt ()

let print_in_file ~file p =
  let c = open_out file in
  let fmt = formatter_of_out_channel c in
  print_program fmt p;
  close_out c
(* ------------------------------------------------------------------ *)